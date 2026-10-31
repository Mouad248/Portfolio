import math
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, f_oneway, kruskal


# =====================================================
# 1. Configuration
# =====================================================

CASE_NAME = "ENNVM_2007_DPMM_9postes"
PREFIX = "ennvm_2007_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain"

RAW_BASE = Path("data/raw/menage_ennvm_propre.xlsx")
OUTPUT_TABLES = Path("outputs/tables/dpmm_ennvm_9")
OUTPUT_ANALYSIS = Path("outputs/analysis_dpmm_ennvm_9")
OUTPUT_ANALYSIS.mkdir(parents=True, exist_ok=True)

PRIOR_COMPARISON_FILE = OUTPUT_TABLES / f"{PREFIX}_prior_comparison.xlsx"
PRIOR_FILE_PATTERN = OUTPUT_TABLES / f"{PREFIX}_{{prior}}_{{kind}}.xlsx"

CLUSTER_COL = "cluster_dpmm_nuts"
WEIGHT_CANDIDATES = ["coef_menage", "coef_ménage", "COEF_MENAGE", "coeff_menage"]
ID_CANDIDATES = ["N_menage", "N_ménage", "n_menage", "ident_menage", "id_menage"]
SHARE_COLS = [f"w_G{i}" for i in range(1, 10)]

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
SMALL_COMPONENT_SHARE = 0.01
SMALL_COMPONENT_SIZE = 100


# =====================================================
# 2. Helpers
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


def clean_category(s):
    return s.astype("string").fillna("Missing").str.strip().replace("", "Missing")


def cramers_v_from_table(table):
    if table.shape[0] < 2 or table.shape[1] < 2:
        return np.nan, np.nan, np.nan, np.nan, True
    chi2, pvalue, _, expected = chi2_contingency(table)
    n = table.to_numpy().sum()
    denom = n * min(table.shape[0] - 1, table.shape[1] - 1)
    v = math.sqrt(chi2 / denom) if denom > 0 else np.nan
    return chi2, pvalue, v, n, bool((expected < 5).any())


def eta_squared(groups):
    clean = [safe_numeric(g).dropna().to_numpy(dtype=float) for g in groups]
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


def weighted_distribution(df, variable, weight_col):
    data = df[[variable, weight_col]].copy()
    data[variable] = clean_category(data[variable])
    data[weight_col] = safe_numeric(data[weight_col])
    data = data[data[weight_col].notna() & (data[weight_col] > 0)]
    total = data[weight_col].sum()
    if total <= 0:
        return pd.Series(dtype=float)
    return data.groupby(variable)[weight_col].sum() / total


def weighted_std(x, w):
    x = safe_numeric(x)
    w = safe_numeric(w)
    mask = x.notna() & w.notna() & (w > 0)
    if mask.sum() <= 1:
        return np.nan
    avg = np.average(x[mask], weights=w[mask])
    var = np.average((x[mask] - avg) ** 2, weights=w[mask])
    return math.sqrt(var)


# =====================================================
# 3. Data prep
# =====================================================

def merge_raw(membership, raw_df):
    if raw_df is None:
        return membership.copy()

    merged = membership.copy()
    id_membership = find_col(merged, ID_CANDIDATES)
    id_raw = find_col(raw_df, ID_CANDIDATES)
    if id_membership is None or id_raw is None:
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
        "max_prob_dpmm_nuts",
        "ambiguous_060_dpmm_nuts",
        "sum_w",
        "sum_w_normalized",
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
        if df[col].notna().mean() < MIN_NON_MISSING_SHARE:
            continue
        nunique = df[col].nunique(dropna=True)
        if 2 <= nunique <= MAX_CATEGORICAL_MODALITIES:
            if df[col].dtype == "object" or df[col].dtype.name == "category" or nunique <= 15:
                out.append(col)
    return out


def detect_quantitative_vars(df):
    excluded_prefixes = ("DAM_G", "DAP_G", "prob_cluster_")
    excluded = set(SHARE_COLS + [
        CLUSTER_COL,
        "max_prob_dpmm_nuts",
        "ambiguous_060_dpmm_nuts",
        "sum_w",
        "sum_w_normalized",
    ])
    excluded.update(c for c in df.columns if str(c).startswith(excluded_prefixes))
    excluded.update(c for c in df.columns if norm_col(c) in {norm_col(x) for x in ID_CANDIDATES})
    excluded.update(c for c in df.columns if norm_col(c) in {norm_col(x) for x in WEIGHT_CANDIDATES})

    out = []
    for cand in PRIORITY_QUANTITATIVE:
        col = find_col(df, [cand])
        if col is not None and col not in out and col not in excluded:
            if safe_numeric(df[col]).notna().mean() >= MIN_NON_MISSING_SHARE:
                out.append(col)
    return out


# =====================================================
# 4. Diagnostics
# =====================================================

def qualitative_diagnostics(df, prior, categorical_vars, weight_col):
    count_rows = []
    delta_rows = []
    test_rows = []

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
        if weight_col:
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
            "prior": prior,
            "variable": var,
            "n_valid": n_valid,
            "n_modalities": valid[var].nunique(dropna=True),
            "chi2": chi2,
            "pvalue": pvalue,
            "cramer_v": cramer_v,
            "low_expected_cell_lt5": low_expected,
        })

        for cluster in counts.index:
            for modality in counts.columns:
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
                rp = row_pct.loc[cluster, modality]
                gp = global_pct.get(modality, 0)
                base = {
                    "prior": prior,
                    "variable": var,
                    "cluster": cluster,
                    "modalite": modality,
                }
                count_rows.append({**base, "count": counts.loc[cluster, modality], "weighted_count": wc})
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

    return count_rows, delta_rows, test_rows


def quantitative_diagnostics(df, prior, quantitative_vars, weight_col):
    stat_rows = []
    test_rows = []

    for var in quantitative_vars:
        valid = df[[CLUSTER_COL]].copy()
        valid[var] = safe_numeric(df[var])
        if weight_col:
            valid[weight_col] = safe_numeric(df[weight_col])
        valid = valid[valid[CLUSTER_COL].notna() & valid[var].notna()]
        if valid[var].nunique(dropna=True) < 2:
            continue

        global_mean = valid[var].mean()
        global_weighted_mean = weighted_mean(valid[var], valid[weight_col]) if weight_col else np.nan

        groups = []
        for cluster, g in valid.groupby(CLUSTER_COL):
            groups.append(g[var])
            mean_cluster = g[var].mean()
            weighted_cluster = weighted_mean(g[var], g[weight_col]) if weight_col else np.nan
            stat_rows.append({
                "prior": prior,
                "variable": var,
                "cluster": cluster,
                "n": len(g),
                "mean": mean_cluster,
                "median": g[var].median(),
                "std": g[var].std(),
                "min": g[var].min(),
                "max": g[var].max(),
                "weighted_mean": weighted_cluster,
                "weighted_std": weighted_std(g[var], g[weight_col]) if weight_col else np.nan,
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
                "prior": prior,
                "variable": var,
                "n_valid": n_total,
                "anova_F": f_stat,
                "anova_pvalue": f_p,
                "eta_squared": eta_squared(groups),
                "kruskal_H": h_stat,
                "kruskal_pvalue": h_p,
                "epsilon_squared": epsilon_squared_kruskal(h_stat, n_total, len(clean_groups)),
            })

    return stat_rows, test_rows


def profile_long(prior, profiles):
    rows = []
    for _, row in profiles.iterrows():
        cluster = row[CLUSTER_COL] if CLUSTER_COL in row else row.iloc[0]
        for col in SHARE_COLS:
            rows.append({
                "prior": prior,
                "cluster": cluster,
                "poste": col,
                "share": row[col],
                "cluster_size": row["cluster_size"] if "cluster_size" in profiles.columns else np.nan,
            })
    return rows


def build_prior_overview(prior_summary, cluster_summary, chi2_rows, qtest_rows):
    out = []
    chi2_df = pd.DataFrame(chi2_rows)
    qtest_df = pd.DataFrame(qtest_rows)

    for _, row in prior_summary.iterrows():
        prior = row["prior"]
        clusters = cluster_summary[cluster_summary["prior"] == prior]
        chi = chi2_df[chi2_df["prior"] == prior] if not chi2_df.empty else pd.DataFrame()
        qt = qtest_df[qtest_df["prior"] == prior] if not qtest_df.empty else pd.DataFrame()

        top_assoc = ""
        if not chi.empty:
            top_assoc = " ; ".join(
                chi.sort_values("cramer_v", ascending=False)
                .head(5)[["variable", "cramer_v"]]
                .apply(lambda r: f"{r['variable']}={r['cramer_v']:.3f}", axis=1)
                .tolist()
            )

        eta_dam = np.nan
        eta_log = np.nan
        if not qt.empty:
            dam_row = qt[qt["variable"].map(norm_col) == "dam"]
            log_row = qt[qt["variable"].map(norm_col) == "log_dam"]
            eta_dam = dam_row["eta_squared"].iloc[0] if not dam_row.empty else np.nan
            eta_log = log_row["eta_squared"].iloc[0] if not log_row.empty else np.nan

        out.append({
            "prior": prior,
            "full_n": row.get("full_n", np.nan),
            "alpha_dp_mean": row.get("alpha_dp_mean", np.nan),
            "occupied_weight_gt_1pct": row.get("occupied_weight_gt_1pct", np.nan),
            "occupied_size_full_gt20": row.get("occupied_size_full_gt20", np.nan),
            "mean_max_prob_full": row.get("mean_max_prob_full", np.nan),
            "share_ambiguous_full_lt_0_60": row.get("share_ambiguous_full_lt_0_60", np.nan),
            "n_divergences": row.get("n_divergences", np.nan),
            "min_cluster_size": clusters["assigned_size_full"].min(),
            "min_cluster_share": clusters["assigned_share_full"].min(),
            "n_small_share_lt_1pct": int((clusters["assigned_share_full"] < SMALL_COMPONENT_SHARE).sum()),
            "n_small_size_lt_100": int((clusters["assigned_size_full"] < SMALL_COMPONENT_SIZE).sum()),
            "eta2_DAM": eta_dam,
            "eta2_log_DAM": eta_log,
            "top_qualitative_associations": top_assoc,
        })
    return pd.DataFrame(out)


# =====================================================
# 5. Main
# =====================================================

def main():
    if not PRIOR_COMPARISON_FILE.exists():
        raise FileNotFoundError(f"Missing DPMM prior comparison: {PRIOR_COMPARISON_FILE}")

    raw_df = pd.read_excel(RAW_BASE) if RAW_BASE.exists() else None
    prior_summary = pd.read_excel(PRIOR_COMPARISON_FILE, sheet_name="prior_global_summary")
    cluster_summary = pd.read_excel(PRIOR_COMPARISON_FILE, sheet_name="cluster_summary")

    all_profiles = []
    all_counts = []
    all_delta = []
    all_chi2 = []
    all_quant = []
    all_qtests = []
    all_membership_quality = []

    for prior in prior_summary["prior"].tolist():
        print("Diagnostic DPMM prior:", prior)
        membership_file = Path(str(PRIOR_FILE_PATTERN).format(prior=prior, kind="membership_full"))
        profiles_file = Path(str(PRIOR_FILE_PATTERN).format(prior=prior, kind="profiles_full"))

        if not membership_file.exists() or not profiles_file.exists():
            print("  Missing files, skipped.")
            continue

        membership = pd.read_excel(membership_file)
        profiles = pd.read_excel(profiles_file)
        merged = add_derived_variables(merge_raw(membership, raw_df))
        weight_col = find_col(merged, WEIGHT_CANDIDATES)

        categorical_vars = detect_categorical_vars(merged)
        quantitative_vars = detect_quantitative_vars(merged)

        counts, delta, chi2_rows = qualitative_diagnostics(
            merged, prior, categorical_vars, weight_col
        )
        quant_rows, qtest_rows = quantitative_diagnostics(
            merged, prior, quantitative_vars, weight_col
        )

        all_profiles.extend(profile_long(prior, profiles))
        all_counts.extend(counts)
        all_delta.extend(delta)
        all_chi2.extend(chi2_rows)
        all_quant.extend(quant_rows)
        all_qtests.extend(qtest_rows)

        max_prob = safe_numeric(membership["max_prob_dpmm_nuts"])
        all_membership_quality.append({
            "prior": prior,
            "n": len(membership),
            "mean_max_prob": max_prob.mean(),
            "median_max_prob": max_prob.median(),
            "p25_max_prob": max_prob.quantile(0.25),
            "p75_max_prob": max_prob.quantile(0.75),
            "share_max_prob_lt_0_60": (max_prob < 0.60).mean(),
            "share_max_prob_gt_0_80": (max_prob > 0.80).mean(),
            "share_max_prob_gt_0_90": (max_prob > 0.90).mean(),
        })

    overview = build_prior_overview(
        prior_summary,
        cluster_summary,
        all_chi2,
        all_qtests,
    )

    output_file = OUTPUT_ANALYSIS / f"{CASE_NAME}_diagnostic.xlsx"
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        prior_summary.to_excel(writer, sheet_name="01_prior_summary", index=False)
        cluster_summary.to_excel(writer, sheet_name="02_cluster_summary", index=False)
        pd.DataFrame(all_profiles).to_excel(writer, sheet_name="03_profiles_long", index=False)
        pd.DataFrame(all_membership_quality).to_excel(writer, sheet_name="04_membership_quality", index=False)
        pd.DataFrame(all_counts).to_excel(writer, sheet_name="05_crosstab_counts", index=False)
        pd.DataFrame(all_delta).to_excel(writer, sheet_name="06_crosstab_delta", index=False)
        pd.DataFrame(all_chi2).to_excel(writer, sheet_name="07_chi2_cramerv", index=False)
        pd.DataFrame(all_quant).to_excel(writer, sheet_name="08_quant_by_cluster", index=False)
        pd.DataFrame(all_qtests).to_excel(writer, sheet_name="09_anova_kruskal", index=False)
        overview.to_excel(writer, sheet_name="10_prior_overview", index=False)

    print("DPMM diagnostic saved:", output_file)
    print(overview.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
