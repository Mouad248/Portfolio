import math
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, f_oneway, kruskal


# =====================================================
# 1. Configuration du cas etudie
# =====================================================

CASE_NAME = "ENNVM_2007_9postes"
PREFIX = "ennvm_2007"
K_VALUES = range(2, 10)

RAW_BASE = Path("data/raw/menage_ennvm_propre.xlsx")
OUTPUT_TABLES = Path("outputs/tables")
OUTPUT_ANALYSIS = Path("outputs/analysis_dmm_ennvm_9_diagnostic")
OUTPUT_ANALYSIS.mkdir(parents=True, exist_ok=True)

PROFILE_PATTERN = OUTPUT_TABLES / "dmm_ennvm_9/{prefix}_dmm_profiles_K{K}.xlsx"
MEMBERSHIP_PATTERN = OUTPUT_TABLES / "dmm_ennvm_9/{prefix}_dmm_membership_K{K}.xlsx"

SHARE_COLS = [f"w_G{i}" for i in range(1, 10)]
CLUSTER_COL = "cluster_dmm"

ID_CANDIDATES = ["N_menage", "N_ménage", "n_menage", "ident_menage", "id_menage"]
WEIGHT_CANDIDATES = ["coef_menage", "coef_ménage", "COEF_MENAGE", "coeff_menage"]

PRIORITY_CATEGORICAL = [
    "Milieu",
    "region",
    "region_code",
    "Strate_habitat",
    "Quintiles",
    "Sexe_CM",
    "Age_quin_CM",
    "Etat_matrimonial_CM",
    "Niveau_scolaire_CM",
    "Type_activité_CM",
    "Profession_CM",
    "Secteur_activité_CM",
    "Statut_professionnel_CM",
    "quintile_DAM",
]

PRIORITY_QUANTITATIVE = [
    "DAM",
    "log_DAM",
    "Taille_ménage",
    "Taille_menage",
    "Age_CM",
    "p_children",
    "p_active",
]

MAX_CATEGORICAL_MODALITIES = 40
MIN_NON_MISSING_SHARE = 0.50


# =====================================================
# 2. Helpers generaux
# =====================================================

def norm_col(x):
    x = str(x)
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode("utf-8")
    x = x.lower()
    x = re.sub(r"[^a-z0-9]+", "_", x)
    return x.strip("_")


def find_col(df, candidates):
    norm_map = {norm_col(c): c for c in df.columns}
    for cand in candidates:
        key = norm_col(cand)
        if key in norm_map:
            return norm_map[key]
    return None


def safe_numeric(s):
    return pd.to_numeric(s, errors="coerce")


def weighted_mean(x, w):
    x = safe_numeric(x)
    w = safe_numeric(w)
    mask = x.notna() & w.notna() & (w > 0)
    if mask.sum() == 0:
        return np.nan
    return np.average(x[mask], weights=w[mask])


def weighted_std(x, w):
    x = safe_numeric(x)
    w = safe_numeric(w)
    mask = x.notna() & w.notna() & (w > 0)
    if mask.sum() <= 1:
        return np.nan
    avg = np.average(x[mask], weights=w[mask])
    var = np.average((x[mask] - avg) ** 2, weights=w[mask])
    return math.sqrt(var)


def cramers_v_from_table(table):
    if table.shape[0] < 2 or table.shape[1] < 2:
        return np.nan, np.nan, np.nan, np.nan, True
    chi2, pvalue, _, expected = chi2_contingency(table)
    n = table.to_numpy().sum()
    denom = n * (min(table.shape[0] - 1, table.shape[1] - 1))
    v = math.sqrt(chi2 / denom) if denom > 0 else np.nan
    low_expected = bool((expected < 5).any())
    return chi2, pvalue, v, n, low_expected


def eta_squared(groups):
    clean = []
    for g in groups:
        if isinstance(g, pd.Series):
            values = safe_numeric(g).dropna().to_numpy(dtype=float)
        else:
            values = pd.Series(g).dropna().to_numpy(dtype=float)
        clean.append(values)
    clean = [g for g in clean if len(g) > 0]
    if len(clean) < 2:
        return np.nan
    all_values = np.concatenate(clean)
    grand_mean = all_values.mean()
    ss_between = sum(len(g) * (g.mean() - grand_mean) ** 2 for g in clean)
    ss_total = ((all_values - grand_mean) ** 2).sum()
    return ss_between / ss_total if ss_total > 0 else np.nan


def epsilon_squared_kruskal(h_stat, n, k):
    if n <= k:
        return np.nan
    return max((h_stat - k + 1) / (n - k), 0)


def clean_category(s):
    return s.astype("string").fillna("Missing").str.strip().replace("", "Missing")


def weighted_distribution(df, variable, weight_col):
    data = df[[variable, weight_col]].copy()
    data[variable] = clean_category(data[variable])
    data[weight_col] = safe_numeric(data[weight_col])
    data = data[data[weight_col].notna() & (data[weight_col] > 0)]
    total = data[weight_col].sum()
    if total <= 0:
        return pd.Series(dtype=float)
    return data.groupby(variable)[weight_col].sum() / total


# =====================================================
# 3. Detection des variables
# =====================================================

def build_merged_membership(membership, raw_df):
    merged = membership.copy()
    if raw_df is None:
        return merged

    id_membership = find_col(merged, ID_CANDIDATES)
    id_raw = find_col(raw_df, ID_CANDIDATES)
    if id_membership is None or id_raw is None:
        print("Identifiant menage non trouve. Fusion brute ignoree.")
        return merged

    raw_extra_cols = [c for c in raw_df.columns if c not in merged.columns or c == id_raw]
    return merged.merge(
        raw_df[raw_extra_cols],
        left_on=id_membership,
        right_on=id_raw,
        how="left",
        suffixes=("", "_raw"),
    )


def add_derived_variables(df):
    dam_col = find_col(df, ["DAM", "DEPAN", "depense_totale", "dépense_totale"])
    if dam_col is not None:
        dam = safe_numeric(df[dam_col])
        df["log_DAM"] = np.where(dam > 0, np.log(dam), np.nan)
        try:
            df["quintile_DAM"] = pd.qcut(
                dam,
                5,
                labels=[1, 2, 3, 4, 5],
                duplicates="drop",
            )
        except Exception:
            pass
    return df


def detect_categorical_vars(df):
    excluded_prefixes = ("DAM_G", "DAP_G", "prob_cluster_")
    excluded = set(SHARE_COLS + [
        CLUSTER_COL,
        "max_prob",
        "ambiguous_060",
        "sum_w",
        "sum_w_normalized",
        "sum_w_23",
        "sum_w_23_normalized",
    ])
    excluded.update(c for c in df.columns if str(c).startswith(excluded_prefixes))
    excluded.update(c for c in df.columns if norm_col(c) in {norm_col(x) for x in ID_CANDIDATES})
    excluded.update(c for c in df.columns if norm_col(c) in {norm_col(x) for x in WEIGHT_CANDIDATES})

    out = []
    for cand in PRIORITY_CATEGORICAL:
        col = find_col(df, [cand])
        if col is not None and col not in out and col not in excluded:
            out.append(col)

    for col in df.columns:
        if col in out or col in excluded:
            continue
        non_missing_share = df[col].notna().mean()
        if non_missing_share < MIN_NON_MISSING_SHARE:
            continue
        nunique = df[col].nunique(dropna=True)
        if 2 <= nunique <= MAX_CATEGORICAL_MODALITIES:
            if df[col].dtype == "object" or df[col].dtype.name == "category" or nunique <= 15:
                out.append(col)
    return out


def detect_quantitative_vars(df):
    excluded_prefixes = ("DAM_G", "DAP_G", "prob_cluster_")
    excluded = set([CLUSTER_COL, "max_prob", "ambiguous_060", "sum_w", "sum_w_normalized"])
    excluded.update(SHARE_COLS)
    excluded.update(c for c in df.columns if str(c).startswith(excluded_prefixes))
    excluded.update(c for c in df.columns if norm_col(c) in {norm_col(x) for x in ID_CANDIDATES})
    excluded.update(c for c in df.columns if norm_col(c) in {norm_col(x) for x in WEIGHT_CANDIDATES})

    out = []
    for cand in PRIORITY_QUANTITATIVE:
        col = find_col(df, [cand])
        if col is not None and col not in out and col not in excluded:
            if safe_numeric(df[col]).notna().mean() >= MIN_NON_MISSING_SHARE:
                out.append(col)

    # Garder le diagnostic concis: pas d'ajout massif des composantes de depenses.
    return out


# =====================================================
# 4. Diagnostics qualitatifs
# =====================================================

def qualitative_diagnostics(df, k, categorical_vars, weight_col):
    count_rows = []
    pct_rows = []
    delta_rows = []
    test_rows = []
    global_rows = []

    for var in categorical_vars:
        temp = df[[CLUSTER_COL, var] + ([weight_col] if weight_col else [])].copy()
        temp[var] = clean_category(temp[var])

        valid = temp[temp[CLUSTER_COL].notna() & temp[var].notna()]
        if valid[var].nunique(dropna=True) < 2:
            continue

        counts = pd.crosstab(valid[CLUSTER_COL], valid[var])
        row_pct = pd.crosstab(valid[CLUSTER_COL], valid[var], normalize="index")
        global_pct = valid[var].value_counts(normalize=True)

        weighted_counts = None
        weighted_row_pct = None
        weighted_global_pct = None
        if weight_col is not None:
            wvalid = valid.copy()
            wvalid[weight_col] = safe_numeric(wvalid[weight_col])
            wvalid = wvalid[wvalid[weight_col].notna() & (wvalid[weight_col] > 0)]
            if not wvalid.empty:
                weighted_counts = pd.pivot_table(
                    wvalid,
                    values=weight_col,
                    index=CLUSTER_COL,
                    columns=var,
                    aggfunc="sum",
                    fill_value=0,
                )
                weighted_row_pct = weighted_counts.div(weighted_counts.sum(axis=1), axis=0)
                weighted_global_pct = weighted_distribution(wvalid, var, weight_col)

        chi2, pvalue, cramer_v, n_valid, low_expected = cramers_v_from_table(counts)
        test_rows.append({
            "K": k,
            "variable": var,
            "n_valid": n_valid,
            "n_modalities": valid[var].nunique(dropna=True),
            "chi2": chi2,
            "pvalue": pvalue,
            "cramer_v": cramer_v,
            "low_expected_cell_lt5": low_expected,
        })

        for modality in counts.columns:
            global_rows.append({
                "K": k,
                "variable": var,
                "modalite": modality,
                "global_pct": global_pct.get(modality, 0),
                "weighted_global_pct": (
                    weighted_global_pct.get(modality, np.nan)
                    if weighted_global_pct is not None else np.nan
                ),
            })

        for cluster in counts.index:
            for modality in counts.columns:
                count = counts.loc[cluster, modality]
                rp = row_pct.loc[cluster, modality]
                gp = global_pct.get(modality, 0)

                wc = (
                    weighted_counts.loc[cluster, modality]
                    if weighted_counts is not None and modality in weighted_counts.columns
                    else np.nan
                )
                wrp = (
                    weighted_row_pct.loc[cluster, modality]
                    if weighted_row_pct is not None and modality in weighted_row_pct.columns
                    else np.nan
                )
                wgp = (
                    weighted_global_pct.get(modality, np.nan)
                    if weighted_global_pct is not None else np.nan
                )

                base = {
                    "K": k,
                    "variable": var,
                    "cluster": cluster,
                    "modalite": modality,
                }
                count_rows.append({
                    **base,
                    "count": count,
                    "weighted_count": wc,
                })
                pct_rows.append({
                    **base,
                    "row_pct": rp,
                    "weighted_row_pct": wrp,
                })
                delta_rows.append({
                    **base,
                    "row_pct": rp,
                    "global_pct": gp,
                    "delta_vs_global": rp - gp,
                    "weighted_row_pct": wrp,
                    "weighted_global_pct": wgp,
                    "weighted_delta_vs_global": (
                        wrp - wgp if pd.notna(wrp) and pd.notna(wgp) else np.nan
                    ),
                })

    return count_rows, pct_rows, delta_rows, test_rows, global_rows


# =====================================================
# 5. Diagnostics quantitatifs
# =====================================================

def quantitative_diagnostics(df, k, quantitative_vars, weight_col):
    stat_rows = []
    test_rows = []
    global_rows = []

    for var in quantitative_vars:
        x = safe_numeric(df[var])
        valid = df[[CLUSTER_COL]].copy()
        valid[var] = x
        if weight_col is not None:
            valid[weight_col] = safe_numeric(df[weight_col])
        valid = valid[valid[CLUSTER_COL].notna() & valid[var].notna()]

        if valid[var].nunique(dropna=True) < 2:
            continue

        global_mean = valid[var].mean()
        global_median = valid[var].median()
        global_std = valid[var].std()
        global_weighted_mean = (
            weighted_mean(valid[var], valid[weight_col]) if weight_col is not None else np.nan
        )

        global_rows.append({
            "K": k,
            "variable": var,
            "n_valid": len(valid),
            "mean": global_mean,
            "median": global_median,
            "std": global_std,
            "weighted_mean": global_weighted_mean,
        })

        groups = []
        for cluster, g in valid.groupby(CLUSTER_COL):
            groups.append(g[var])
            mean_cluster = g[var].mean()
            weighted_cluster = (
                weighted_mean(g[var], g[weight_col]) if weight_col is not None else np.nan
            )
            stat_rows.append({
                "K": k,
                "variable": var,
                "cluster": cluster,
                "n": len(g),
                "mean": mean_cluster,
                "median": g[var].median(),
                "std": g[var].std(),
                "min": g[var].min(),
                "max": g[var].max(),
                "weighted_mean": weighted_cluster,
                "weighted_std": (
                    weighted_std(g[var], g[weight_col]) if weight_col is not None else np.nan
                ),
                "global_mean": global_mean,
                "delta_mean_vs_global": mean_cluster - global_mean,
                "relative_delta_mean_vs_global": (
                    (mean_cluster - global_mean) / global_mean
                    if global_mean not in [0, np.nan] else np.nan
                ),
                "global_weighted_mean": global_weighted_mean,
                "weighted_delta_vs_global": (
                    weighted_cluster - global_weighted_mean
                    if pd.notna(weighted_cluster) and pd.notna(global_weighted_mean)
                    else np.nan
                ),
            })

        clean_groups = [safe_numeric(g).dropna().to_numpy(dtype=float) for g in groups]
        clean_groups = [g for g in clean_groups if len(g) > 1]
        if len(clean_groups) >= 2:
            f_stat, f_p = f_oneway(*clean_groups)
            h_stat, h_p = kruskal(*clean_groups)
            n_total = sum(len(g) for g in clean_groups)
            test_rows.append({
                "K": k,
                "variable": var,
                "n_valid": n_total,
                "anova_F": f_stat,
                "anova_pvalue": f_p,
                "eta_squared": eta_squared(clean_groups),
                "kruskal_H": h_stat,
                "kruskal_pvalue": h_p,
                "epsilon_squared": epsilon_squared_kruskal(h_stat, n_total, len(clean_groups)),
            })

    return stat_rows, test_rows, global_rows


# =====================================================
# 6. Vue compacte par K
# =====================================================

def build_k_overview(k, membership, chi2_rows, quant_test_rows, categorical_vars, quantitative_vars):
    sizes = membership[CLUSTER_COL].value_counts()
    max_prob = safe_numeric(membership["max_prob"]) if "max_prob" in membership.columns else pd.Series(dtype=float)

    chi2_k = pd.DataFrame(chi2_rows)
    qtest_k = pd.DataFrame(quant_test_rows)

    def get_cramer(var):
        if chi2_k.empty:
            return np.nan
        row = chi2_k[chi2_k["variable"].map(norm_col) == norm_col(var)]
        return row["cramer_v"].iloc[0] if not row.empty else np.nan

    def get_eta(var):
        if qtest_k.empty:
            return np.nan
        row = qtest_k[qtest_k["variable"].map(norm_col) == norm_col(var)]
        return row["eta_squared"].iloc[0] if not row.empty else np.nan

    top_assoc = []
    if not chi2_k.empty:
        top_assoc = (
            chi2_k.sort_values("cramer_v", ascending=False)
            .head(5)[["variable", "cramer_v"]]
            .apply(lambda r: f"{r['variable']}={r['cramer_v']:.3f}", axis=1)
            .tolist()
        )

    return {
        "K": k,
        "n_households": len(membership),
        "min_cluster_size": sizes.min(),
        "max_cluster_size": sizes.max(),
        "mean_cluster_size": sizes.mean(),
        "mean_max_prob": max_prob.mean() if not max_prob.empty else np.nan,
        "share_ambiguous_prob_lt_0_60": (max_prob < 0.60).mean() if not max_prob.empty else np.nan,
        "n_categorical_variables": len(categorical_vars),
        "n_quantitative_variables": len(quantitative_vars),
        "cramer_milieu": get_cramer("Milieu"),
        "cramer_region": max(get_cramer("region"), get_cramer("region_code")),
        "cramer_quintile_DAM": get_cramer("quintile_DAM"),
        "eta2_DAM": get_eta("DAM"),
        "eta2_log_DAM": get_eta("log_DAM"),
        "top_qualitative_associations": " ; ".join(top_assoc),
    }


# =====================================================
# 7. Execution
# =====================================================

def main():
    raw_df = pd.read_excel(RAW_BASE) if RAW_BASE.exists() else None
    if raw_df is not None:
        print("Base originale chargee :", RAW_BASE, raw_df.shape)
    else:
        print("Base originale non trouvee. Diagnostic limite aux memberships.")

    all_counts = []
    all_row_pct = []
    all_delta = []
    all_chi2 = []
    all_quant = []
    all_qtests = []
    all_global_cat = []
    all_global_quant = []
    all_overview = []

    for k in K_VALUES:
        print(f"\nDiagnostic K={k}")
        profile_file = Path(str(PROFILE_PATTERN).format(prefix=PREFIX, K=k))
        membership_file = Path(str(MEMBERSHIP_PATTERN).format(prefix=PREFIX, K=k))
        if not profile_file.exists() or not membership_file.exists():
            print("Fichiers DMM manquants, K ignore.")
            continue

        membership = pd.read_excel(membership_file)
        if CLUSTER_COL not in membership.columns:
            raise ValueError(f"{CLUSTER_COL} absent dans {membership_file}")

        merged = build_merged_membership(membership, raw_df)
        merged = add_derived_variables(merged)
        weight_col = find_col(merged, WEIGHT_CANDIDATES)

        categorical_vars = detect_categorical_vars(merged)
        quantitative_vars = detect_quantitative_vars(merged)

        print(f"Variables qualitatives detectees : {len(categorical_vars)}")
        print(f"Variables quantitatives detectees : {len(quantitative_vars)}")
        if weight_col:
            print("Ponderation detectee :", weight_col)

        count_rows, pct_rows, delta_rows, chi2_rows, global_cat_rows = qualitative_diagnostics(
            merged, k, categorical_vars, weight_col
        )
        quant_rows, qtest_rows, global_quant_rows = quantitative_diagnostics(
            merged, k, quantitative_vars, weight_col
        )

        all_counts.extend(count_rows)
        all_row_pct.extend(pct_rows)
        all_delta.extend(delta_rows)
        all_chi2.extend(chi2_rows)
        all_quant.extend(quant_rows)
        all_qtests.extend(qtest_rows)
        all_global_cat.extend(global_cat_rows)
        all_global_quant.extend(global_quant_rows)
        all_overview.append(
            build_k_overview(k, membership, chi2_rows, qtest_rows, categorical_vars, quantitative_vars)
        )

    global_descriptives = pd.concat(
        [
            pd.DataFrame(all_global_cat).assign(type="qualitative"),
            pd.DataFrame(all_global_quant).assign(type="quantitative"),
        ],
        ignore_index=True,
        sort=False,
    )

    output_file = OUTPUT_ANALYSIS / f"{CASE_NAME}_diagnostic_K.xlsx"
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        global_descriptives.to_excel(writer, sheet_name="01_global_descriptives", index=False)
        pd.DataFrame(all_counts).to_excel(writer, sheet_name="02_crosstab_counts", index=False)
        pd.DataFrame(all_row_pct).to_excel(writer, sheet_name="03_crosstab_row_pct", index=False)
        pd.DataFrame(all_delta).to_excel(writer, sheet_name="04_crosstab_global_delta", index=False)
        pd.DataFrame(all_chi2).to_excel(writer, sheet_name="05_chi2_cramerv", index=False)
        pd.DataFrame(all_quant).to_excel(writer, sheet_name="06_quantitative_by_cluster", index=False)
        pd.DataFrame(all_qtests).to_excel(writer, sheet_name="07_anova_kruskal", index=False)
        pd.DataFrame(all_overview).to_excel(writer, sheet_name="08_K_overview", index=False)

    print("\nDiagnostic termine.")
    print("Fichier central :", output_file)


if __name__ == "__main__":
    main()
