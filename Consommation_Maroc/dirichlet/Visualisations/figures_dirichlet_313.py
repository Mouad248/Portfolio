from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D

from figures_interpretation_dirichlet import read_xlsx


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "figures" / "dirichlet_313"
OUT_DIR.mkdir(parents=True, exist_ok=True)

G_COLS = [f"w_G{i}" for i in range(1, 10)]
S_COLS = [f"w_S{i}" for i in range(1, 24)]

G_LABELS = {
    "w_G1": "Alimentaire",
    "w_G2": "Habillement",
    "w_G3": "Logement",
    "w_G4": "Tabac",
    "w_G5": "Equipement",
    "w_G6": "Sante",
    "w_G7": "Transport",
    "w_G8": "Communication",
    "w_G9": "Culture-ens.",
}

FAMILIES_23 = {
    "Alimentaire": [f"w_S{i}" for i in range(1, 7)],
    "Habillement": ["w_S7"],
    "Logement": ["w_S8", "w_S9", "w_S11"],
    "Equipement": ["w_S10"],
    "Sante": ["w_S12", "w_S13"],
    "Transport-comm.": ["w_S14", "w_S15", "w_S16"],
    "Culture-ens.": ["w_S17", "w_S18"],
    "Autres": ["w_S19", "w_S20", "w_S21", "w_S22", "w_S23"],
}

FAMILY_ORDER = [
    "Alimentaire",
    "Logement",
    "Sante",
    "Transport-comm.",
    "Culture-ens.",
    "Habillement",
    "Equipement",
    "Autres",
]

BEHAVIOR_ORDER = [
    "Alimentaire",
    "Logement",
    "Sante",
    "Transport-comm.",
    "Intermediaire",
    "Diversifie",
]

COLORS = {
    "Alimentaire": "#2a9d8f",
    "Habillement": "#8ab17d",
    "Logement": "#457b9d",
    "Tabac": "#6d597a",
    "Equipement": "#b56576",
    "Sante": "#e76f51",
    "Transport": "#f4a261",
    "Communication": "#5e60ce",
    "Transport-comm.": "#f4a261",
    "Culture-ens.": "#d4a373",
    "Autres": "#6d597a",
    "Intermediaire": "#9aa0a6",
    "Diversifie": "#264653",
}

PRIORS = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]
PRIOR_LABELS = {
    "gamma_1_1": "Gamma(1,1)",
    "gamma_1_2": "Gamma(1,2)",
    "gamma_0p5_2": "Gamma(0.5,2)",
    "gamma_0p25_2": "Gamma(0.25,2)",
}


def setup_style():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 9,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "savefig.bbox": "tight",
        }
    )


def cluster_id(row):
    for key in ("cluster", "cluster_dmm", "cluster_dpmm_nuts"):
        if key in row and row[key] != "":
            return int(row[key])
    raise KeyError("cluster id not found")


def dmm_profile_path(year, posts, k):
    if year == "2007" and posts == 9:
        return Path("outputs/tables/dmm_ennvm_9") / f"ennvm_2007_dmm_profiles_K{k}.xlsx"
    if year == "2014" and posts == 9:
        return Path("outputs/tables/dmm_encdm_9") / f"encdm_2014_dmm_profiles_K{k}.xlsx"
    if year == "2007" and posts == 23:
        return Path("outputs/tables/dmm_ennvm_23") / f"ennvm_2007_23_dmm_profiles_K{k}.xlsx"
    return Path("outputs/tables/dmm_encdm_23") / f"encdm_2014_23_dmm_profiles_K{k}.xlsx"


def dmm_summary_path(year, posts):
    if year == "2007" and posts == 9:
        return Path("outputs/tables/dmm_ennvm_9/ennvm_2007_dmm_k2_to_k9_summary.xlsx")
    if year == "2014" and posts == 9:
        return Path("outputs/tables/dmm_encdm_9/encdm_2014_dmm_k2_to_k9_summary.xlsx")
    if year == "2007" and posts == 23:
        return Path("outputs/tables/dmm_ennvm_23/ennvm_2007_23_dmm_k2_to_k9_summary.xlsx")
    return Path("outputs/tables/dmm_encdm_23/encdm_2014_23_dmm_k2_to_k9_summary.xlsx")


def dmm_diag_path(year, posts):
    if year == "2007" and posts == 9:
        return Path("outputs/analysis_dmm_ennvm_9_diagnostic/ENNVM_2007_9postes_diagnostic_K.xlsx")
    if year == "2014" and posts == 9:
        return Path("outputs/analysis_dmm_encdm_9_diagnostic/ENCDM_2014_9postes_diagnostic_K.xlsx")
    if year == "2007" and posts == 23:
        return Path("outputs/analysis_dmm_ennvm_23_diagnostic/ENNVM_2007_23postes_diagnostic_K.xlsx")
    return Path("outputs/analysis_dmm_encdm_23_diagnostic/ENCDM_2014_23postes_diagnostic_K.xlsx")


def dpmm_diag_path(year, posts):
    if year == "2007" and posts == 9:
        return Path("outputs/analysis_dpmm_ennvm_9/ENNVM_2007_DPMM_9postes_diagnostic.xlsx")
    if year == "2014" and posts == 9:
        return Path("outputs/analysis_dpmm_encdm_9/ENCDM_2014_DPMM_9postes_diagnostic.xlsx")
    if year == "2007" and posts == 23:
        return Path("outputs/analysis_dpmm_ennvm_23/ENNVM_2007_DPMM_23postes_diagnostic.xlsx")
    return Path("outputs/analysis_dpmm_encdm_23/ENCDM_2014_DPMM_23postes_diagnostic.xlsx")


def dpmm_profile_path(year, posts, prior):
    if year == "2007" and posts == 9:
        prefix = "ennvm_2007_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain"
        return Path("outputs/tables/dpmm_ennvm_9") / f"{prefix}_{prior}_profiles_full.xlsx"
    if year == "2014" and posts == 9:
        prefix = "encdm_2014_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain"
        return Path("outputs/tables/dpmm_encdm_9") / f"{prefix}_{prior}_profiles_full.xlsx"
    if year == "2007" and posts == 23:
        prefix = "ennvm_2007_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"
        return Path("outputs/tables/dpmm_ennvm_23") / f"{prefix}_{prior}_profiles_full.xlsx"
    prefix = "encdm_2014_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"
    return Path("outputs/tables/dpmm_encdm_23") / f"{prefix}_{prior}_profiles_full.xlsx"


def weighted_mean(rows, cols):
    total = sum(float(r["cluster_size"]) for r in rows)
    return {c: sum(float(r["cluster_size"]) * float(r[c]) for r in rows) / total for c in cols}


def family_values_23(row):
    return {fam: sum(float(row[c]) for c in cols) for fam, cols in FAMILIES_23.items()}


def family_weighted_mean_23(rows):
    gm = weighted_mean(rows, S_COLS)
    return {fam: sum(gm[c] for c in cols) for fam, cols in FAMILIES_23.items()}


def g_family_values(row):
    return {
        "Alimentaire": float(row["w_G1"]),
        "Habillement": float(row["w_G2"]),
        "Logement": float(row["w_G3"]),
        "Tabac": float(row["w_G4"]),
        "Equipement": float(row["w_G5"]),
        "Sante": float(row["w_G6"]),
        "Transport-comm.": float(row["w_G7"]) + float(row["w_G8"]),
        "Culture-ens.": float(row["w_G9"]),
    }


def g_family_mean(rows):
    gm = weighted_mean(rows, G_COLS)
    return {
        "Alimentaire": gm["w_G1"],
        "Habillement": gm["w_G2"],
        "Logement": gm["w_G3"],
        "Tabac": gm["w_G4"],
        "Equipement": gm["w_G5"],
        "Sante": gm["w_G6"],
        "Transport-comm.": gm["w_G7"] + gm["w_G8"],
        "Culture-ens.": gm["w_G9"],
    }


def dominant_family(row, rows, posts):
    if posts == 9:
        values = g_family_values(row)
        means = g_family_mean(rows)
    else:
        values = family_values_23(row)
        means = family_weighted_mean_23(rows)
    deltas = {fam: values[fam] - means[fam] for fam in values}
    fam = max(deltas, key=deltas.get)
    return fam, values[fam]


def panel_label(ax, text):
    ax.text(
        0.02,
        0.98,
        text,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        fontweight="bold",
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "edgecolor": "#dddddd", "alpha": 0.9},
    )


def legend_for_families(fig, families, ncol=4):
    handles = [
        Line2D([0], [0], marker="o", linestyle="", markersize=7, markerfacecolor=COLORS[f], markeredgecolor="white", label=f)
        for f in families
    ]
    fig.legend(handles=handles, loc="lower center", ncol=ncol, frameon=False, bbox_to_anchor=(0.5, -0.01))


def fig1_fragmentation():
    fig, axes = plt.subplots(2, 2, figsize=(14.5, 8.6), sharex=True, sharey=True, constrained_layout=True)
    used = []
    for row_idx, posts in enumerate([9, 23]):
        for col_idx, year in enumerate(["2007", "2014"]):
            ax = axes[row_idx, col_idx]
            for k in range(2, 10):
                rows = read_xlsx(dmm_profile_path(year, posts, k))
                total = sum(float(r["cluster_size"]) for r in rows)
                rows_sorted = sorted(rows, key=lambda r: dominant_family(r, rows, posts)[1])
                for i, r in enumerate(rows_sorted):
                    fam, share = dominant_family(r, rows, posts)
                    if fam not in used:
                        used.append(fam)
                    x = k + (i - (len(rows_sorted) - 1) / 2) * 0.05
                    y = 100 * share
                    size = 45 + 900 * float(r["cluster_size"]) / total
                    ax.scatter(x, y, s=size, color=COLORS[fam], alpha=0.82, edgecolor="white", linewidth=0.8)
            panel_label(ax, f"{year} - {posts} postes")
            ax.set_xticks(range(2, 10))
            ax.grid(axis="y", color="#ededed", linewidth=0.8)
            if row_idx == 1:
                ax.set_xlabel("K")
            if col_idx == 0:
                ax.set_ylabel("Famille dominante (%)")
    legend_for_families(fig, used, ncol=4)
    return fig


def stacked_bar_panel(ax, rows, posts, label):
    total = sum(float(r["cluster_size"]) for r in rows)
    if posts == 9:
        cols = G_COLS
        names = [G_LABELS[c] for c in cols]
        rows = sorted(rows, key=lambda r: float(r["w_G1"]), reverse=True)
        values = {name: [100 * float(r[col]) for r in rows] for name, col in zip(names, cols)}
    else:
        names = FAMILY_ORDER
        rows = sorted(rows, key=lambda r: family_values_23(r)["Alimentaire"], reverse=True)
        values = {fam: [100 * family_values_23(r)[fam] for r in rows] for fam in names}
    y = np.arange(len(rows))
    left = np.zeros(len(rows))
    for name in names:
        vals = np.array(values[name])
        ax.barh(y, vals, left=left, color=COLORS[name], edgecolor="white", linewidth=0.5, label=name)
        left += vals
    ax.set_yticks(y)
    ax.set_yticklabels([f"C{cluster_id(r)}  {100*float(r['cluster_size'])/total:.0f}%" for r in rows], fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.grid(axis="x", color="#ededed", linewidth=0.8)
    panel_label(ax, label)


def fig2_stacked_k6():
    fig, axes = plt.subplots(2, 2, figsize=(15.5, 9.2), sharex=True, constrained_layout=True)
    for row_idx, posts in enumerate([9, 23]):
        for col_idx, year in enumerate(["2007", "2014"]):
            ax = axes[row_idx, col_idx]
            rows = read_xlsx(dmm_profile_path(year, posts, 6))
            stacked_bar_panel(ax, rows, posts, f"{year} - {posts} postes")
            if row_idx == 1:
                ax.set_xlabel("%")
    handles_9, labels_9 = axes[0, 0].get_legend_handles_labels()
    handles_23, labels_23 = axes[1, 0].get_legend_handles_labels()
    fig.legend(handles_9, labels_9, loc="lower left", ncol=5, frameon=False, bbox_to_anchor=(0.03, -0.03))
    fig.legend(handles_23, labels_23, loc="lower right", ncol=4, frameon=False, bbox_to_anchor=(0.98, -0.03))
    return fig


def fig3_quality_k():
    fig, axes = plt.subplots(2, 2, figsize=(14.5, 8.4), sharex=True, sharey=True, constrained_layout=True)
    for row_idx, posts in enumerate([9, 23]):
        for col_idx, year in enumerate(["2007", "2014"]):
            ax = axes[row_idx, col_idx]
            rows = read_xlsx(dmm_summary_path(year, posts))
            ks = [int(r["K"]) for r in rows]
            mean_prob = [100 * float(r["mean_max_prob"]) for r in rows]
            ambiguous = [100 * float(r["share_ambiguous_prob_lt_0_60"]) for r in rows]
            min_share = []
            for k, r in zip(ks, rows):
                prof = read_xlsx(dmm_profile_path(year, posts, k))
                total = sum(float(x["cluster_size"]) for x in prof)
                min_share.append(100 * float(r["min_cluster_size"]) / total)
            ax.plot(ks, mean_prob, marker="o", color="#457b9d", lw=2, label="Prob. max moy.")
            ax.plot(ks, ambiguous, marker="o", color="#e76f51", lw=2, label="Ambigus <60%")
            ax.plot(ks, min_share, marker="o", color="#2a9d8f", lw=2, label="Cluster min.")
            ax.axvline(6, color="#333333", lw=1, ls="--")
            panel_label(ax, f"{year} - {posts} postes")
            ax.set_xticks(range(2, 10))
            ax.set_ylim(0, 105)
            ax.grid(axis="y", color="#ededed", linewidth=0.8)
            if row_idx == 1:
                ax.set_xlabel("K")
            if col_idx == 0:
                ax.set_ylabel("%")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.01))
    return fig


def get_global_quant(diag, k, variable):
    rows = read_xlsx(diag, "01_global_descriptives")
    candidates = [r for r in rows if int(r["K"]) == k and r["variable"] == variable and r["type"] == "quantitative"]
    return candidates[0] if candidates else None


def row_for(rows, **kwargs):
    out = []
    for r in rows:
        ok = True
        for key, value in kwargs.items():
            if r.get(key) != value:
                ok = False
                break
        if ok:
            out.append(r)
    return out


def avg_quintile(rows, cluster=None):
    vals = []
    for r in rows:
        if r["variable"] != "quintile_DAM":
            continue
        if cluster is not None and int(r["cluster"]) != cluster:
            continue
        try:
            q = float(r["modalite"])
        except Exception:
            continue
        vals.append((q, float(r["row_pct"]), float(r["global_pct"])))
    if not vals:
        return 0
    row_avg = sum(q * p for q, p, _ in vals)
    global_avg = sum(q * g for q, _, g in vals)
    return row_avg - global_avg


def socio_matrix(year):
    diag = dmm_diag_path(year, 23)
    k = 6
    q = [r for r in read_xlsx(diag, "06_quantitative_by_cluster") if int(r["K"]) == k]
    d = [r for r in read_xlsx(diag, "04_crosstab_global_delta") if int(r["K"]) == k]
    prof = read_xlsx(dmm_profile_path(year, 23, k))
    clusters = [cluster_id(r) for r in prof]
    dam_global = get_global_quant(diag, k, "DAM")
    size_global = get_global_quant(diag, k, "Taille_ménage")
    education_var = "Niveau_scolaire_CM" if year == "2007" else "Niveau_scolaire_agreg_CM"
    data = []
    labels = []
    for cluster in clusters:
        dam = row_for(q, variable="DAM", cluster=cluster)[0]
        size = row_for(q, variable="Taille_ménage", cluster=cluster)[0]
        rural = row_for(d, variable="Milieu", cluster=cluster, modalite="Rural")
        urban = row_for(d, variable="Milieu", cluster=cluster, modalite="Urbain")
        sup = row_for(d, variable=education_var, cluster=cluster, modalite="Supérieur")
        dam_med_rel = 100 * (float(dam["median"]) / float(dam_global["median"]) - 1) if dam_global else 0
        row = [
            100 * float(dam["relative_delta_mean_vs_global"]),
            dam_med_rel,
            100 * float(rural[0]["delta_vs_global"]) if rural else 0,
            100 * float(urban[0]["delta_vs_global"]) if urban else 0,
            20 * avg_quintile(d, cluster=cluster),
            100 * (float(size["mean"]) / float(size_global["mean"]) - 1) if size_global else 0,
            100 * float(sup[0]["delta_vs_global"]) if sup else 0,
        ]
        data.append(row)
        labels.append(f"C{cluster}")
    return np.array(data), labels


def fig4_socio_heatmap():
    fig, axes = plt.subplots(1, 2, figsize=(13.8, 6.4), constrained_layout=True)
    cols = ["DAM moy.", "DAM med.", "Rural", "Urbain", "Quintile", "Taille", "Sup."]
    vmax = 0
    matrices = []
    labels_all = []
    for year in ["2007", "2014"]:
        mat, labels = socio_matrix(year)
        matrices.append(mat)
        labels_all.append(labels)
        vmax = max(vmax, np.nanmax(np.abs(mat)))
    vmax = max(12, min(vmax, 80))
    for ax, year, mat, labels in zip(axes, ["2007", "2014"], matrices, labels_all):
        im = ax.imshow(mat, cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto")
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels(cols, rotation=30, ha="right")
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                if abs(mat[i, j]) >= 8:
                    ax.text(j, i, f"{mat[i,j]:+.0f}", ha="center", va="center", fontsize=8)
        panel_label(ax, year)
        ax.tick_params(length=0)
    fig.colorbar(im, ax=axes, shrink=0.78, location="right")
    return fig


def fig5_dpmm_prior_weights():
    cases = [
        ("2007", 9, "2007-9"),
        ("2014", 9, "2014-9"),
        ("2007", 23, "2007-23"),
        ("2014", 23, "2014-23"),
    ]
    fig, axes = plt.subplots(4, 4, figsize=(15.8, 11.2), sharex=True, sharey=True, constrained_layout=True)
    for row_idx, (year, posts, case_label) in enumerate(cases):
        diag = dpmm_diag_path(year, posts)
        cluster_rows = read_xlsx(diag, "02_cluster_summary")
        for col_idx, prior in enumerate(PRIORS):
            ax = axes[row_idx, col_idx]
            rows = [r for r in cluster_rows if r["prior"] == prior]
            rows = sorted(rows, key=lambda r: int(r["cluster"]))
            x = [int(r["cluster"]) for r in rows]
            h = [100 * float(r["posterior_weight_mean"]) for r in rows]
            ax.bar(x, h, color="#457b9d", edgecolor="white", linewidth=0.6)
            for thr in [1, 2, 3]:
                ax.axhline(thr, color="#777777", lw=0.8, ls="--", alpha=0.65)
            if row_idx == 0:
                ax.set_title(PRIOR_LABELS[prior], fontsize=10)
            if col_idx == 0:
                ax.set_ylabel(f"{case_label}\n%")
            ax.set_xticks(range(1, 8))
            ax.set_ylim(0, 55)
            ax.grid(axis="y", color="#eeeeee", linewidth=0.7)
    handles = [Line2D([0], [0], color="#777777", lw=0.8, ls="--", label="1 %, 2 %, 3 %")]
    fig.legend(handles=handles, loc="lower center", frameon=False, bbox_to_anchor=(0.5, -0.01))
    return fig


def classify_counts(rows, posts):
    if posts == 9:
        means = g_family_mean(rows)
        getvals = g_family_values
    else:
        means = family_weighted_mean_23(rows)
        getvals = family_values_23
    counts = {fam: 0 for fam in BEHAVIOR_ORDER}
    for r in rows:
        vals = getvals(r)
        deltas = {fam: vals.get(fam, 0) - means.get(fam, 0) for fam in vals}
        max_fam = max(deltas, key=deltas.get)
        max_delta = deltas[max_fam]
        if vals.get("Alimentaire", 0) <= means.get("Alimentaire", 0) - 0.07:
            counts["Diversifie"] += 1
        if max_delta < 0.035:
            counts["Intermediaire"] += 1
        if max_fam == "Alimentaire" and max_delta >= 0.03:
            counts["Alimentaire"] += 1
        if max_fam == "Logement" and max_delta >= 0.025:
            counts["Logement"] += 1
        if max_fam == "Sante" and max_delta >= 0.025:
            counts["Sante"] += 1
        if max_fam in ("Transport-comm.", "Transport", "Communication") and max_delta >= 0.025:
            counts["Transport-comm."] += 1
    return counts


def convergence_matrix(year):
    specs = [
        ("DMM 9", read_xlsx(dmm_profile_path(year, 9, 6)), 9),
        ("DMM 23", read_xlsx(dmm_profile_path(year, 23, 6)), 23),
        ("DPMM 9", read_xlsx(dpmm_profile_path(year, 9, "gamma_1_1" if year == "2007" else "gamma_0p25_2")), 9),
        ("DPMM 23", read_xlsx(dpmm_profile_path(year, 23, "gamma_0p25_2" if year == "2007" else "gamma_1_1")), 23),
    ]
    mat = []
    for fam in BEHAVIOR_ORDER:
        row = []
        for _, rows, posts in specs:
            row.append(classify_counts(rows, posts)[fam])
        mat.append(row)
    return np.array(mat), [s[0] for s in specs]


def fig6_convergence():
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.8), constrained_layout=True)
    vmax = 0
    mats = []
    cols = None
    for year in ["2007", "2014"]:
        mat, cols = convergence_matrix(year)
        mats.append(mat)
        vmax = max(vmax, int(mat.max()))
    for ax, year, mat in zip(axes, ["2007", "2014"], mats):
        im = ax.imshow(mat, cmap="YlGnBu", vmin=0, vmax=max(1, vmax), aspect="auto")
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels(cols, rotation=20, ha="right")
        ax.set_yticks(range(len(BEHAVIOR_ORDER)))
        ax.set_yticklabels(BEHAVIOR_ORDER)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                ax.text(j, i, str(int(mat[i, j])), ha="center", va="center", fontsize=9)
        panel_label(ax, year)
        ax.tick_params(length=0)
    fig.colorbar(im, ax=axes, shrink=0.72, location="right")
    return fig


def save(fig, pdf, filename):
    path = OUT_DIR / filename
    fig.savefig(path)
    pdf.savefig(fig)
    plt.close(fig)
    return path


def main():
    setup_style()
    figures = [
        (fig1_fragmentation, "fig_01_fragmentation_selon_K.pdf"),
        (fig2_stacked_k6, "fig_02_barres_empilees_K6.pdf"),
        (fig3_quality_k, "fig_03_qualite_stabilite_K.pdf"),
        (fig4_socio_heatmap, "fig_04_ancrage_socioeconomique_DMM23_K6.pdf"),
        (fig5_dpmm_prior_weights, "fig_05_poids_DPMM_selon_prior.pdf"),
        (fig6_convergence, "fig_06_convergence_DMM_DPMM.pdf"),
    ]
    combined = OUT_DIR / "figures_dirichlet_313.pdf"
    with PdfPages(combined) as pdf:
        print(combined)
        for maker, filename in figures:
            print(save(maker(), pdf, filename))


if __name__ == "__main__":
    main()
