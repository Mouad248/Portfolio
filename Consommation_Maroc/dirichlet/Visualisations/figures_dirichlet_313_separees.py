from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
from scipy.optimize import linear_sum_assignment

from figures_interpretation_dirichlet import read_xlsx


ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "outputs" / "figures" / "dirichlet_313_separees"
OUT_ROOT.mkdir(parents=True, exist_ok=True)

PRIORS = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]
PRIOR_LABELS = {
    "gamma_1_1": "Gamma(1,1)",
    "gamma_1_2": "Gamma(1,2)",
    "gamma_0p5_2": "Gamma(0.5,2)",
    "gamma_0p25_2": "Gamma(0.25,2)",
}

PREFERRED_PRIOR = {
    (2007, 9): "gamma_1_1",
    (2014, 9): "gamma_0p25_2",
    (2007, 23): "gamma_0p25_2",
    (2014, 23): "gamma_1_1",
}


def setup_style():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 14,
            "axes.titlesize": 15,
            "axes.labelsize": 15,
            "xtick.labelsize": 13,
            "ytick.labelsize": 13,
            "legend.fontsize": 24,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "savefig.bbox": "tight",
        }
    )


def cols_for(posts):
    prefix = "G" if posts == 9 else "S"
    return [f"w_{prefix}{i}" for i in range(1, posts + 1)]


def labels_for(posts):
    prefix = "G" if posts == 9 else "S"
    return [f"{prefix}{i}" for i in range(1, posts + 1)]


def color_map(posts):
    cmap_names = ["tab20", "tab20b", "tab20c"]
    colors = []
    for name in cmap_names:
        cmap = plt.get_cmap(name)
        colors.extend([cmap(i) for i in range(cmap.N)])
    return {label: colors[i] for i, label in enumerate(labels_for(posts))}


FRAGMENTATION_COLORS = {
    "Alimentation": "#1f77b4",
    "Boissons-tabac": "#8c564b",
    "Habillement": "#9467bd",
    "Logement-energie": "#2ca02c",
    "Ameublement": "#17becf",
    "Sante": "#d62728",
    "Transport-communication": "#ff7f0e",
    "Culture-enseignement": "#e377c2",
    "Autres": "#7f7f7f",
}


def fragmentation_groups(posts):
    if posts == 9:
        return [
            ("Alimentation", ["w_G1"]),
            ("Boissons-tabac", ["w_G2"]),
            ("Logement-energie", ["w_G3"]),
            ("Habillement", ["w_G4"]),
            ("Ameublement", ["w_G5"]),
            ("Sante", ["w_G6"]),
            ("Transport-communication", ["w_G7"]),
            ("Culture-enseignement", ["w_G8"]),
            ("Autres", ["w_G9"]),
        ]
    return [
        ("Alimentation", [f"w_S{i}" for i in range(1, 7)]),
        ("Habillement", ["w_S7"]),
        ("Logement-energie", [f"w_S{i}" for i in range(8, 12)]),
        ("Ameublement", ["w_S12"]),
        ("Sante", ["w_S13"]),
        ("Transport-communication", [f"w_S{i}" for i in range(14, 19)]),
        ("Culture-enseignement", ["w_S19", "w_S20"]),
        ("Autres", ["w_S21", "w_S22", "w_S23"]),
    ]


def fragmentation_profile(row, posts):
    shares = {
        label: sum(float(row[col]) for col in cols)
        for label, cols in fragmentation_groups(posts)
    }
    label = max(shares, key=shares.get)
    return label, shares[label], shares


def cluster_id(row):
    for key in ("cluster", "cluster_dmm", "cluster_dpmm_nuts"):
        if key in row and row[key] != "":
            return int(row[key])
    raise KeyError("cluster id not found")


def dmm_profile_path(year, posts, k):
    if year == 2007 and posts == 9:
        return Path("outputs/tables/dmm_ennvm_9") / f"ennvm_2007_dmm_profiles_K{k}.xlsx"
    if year == 2014 and posts == 9:
        return Path("outputs/tables/dmm_encdm_9") / f"encdm_2014_dmm_profiles_K{k}.xlsx"
    if year == 2007 and posts == 23:
        return Path("outputs/tables/dmm_ennvm_23") / f"ennvm_2007_23_dmm_profiles_K{k}.xlsx"
    return Path("outputs/tables/dmm_encdm_23") / f"encdm_2014_23_dmm_profiles_K{k}.xlsx"


def dmm_summary_path(year, posts):
    if year == 2007 and posts == 9:
        return Path("outputs/tables/dmm_ennvm_9/ennvm_2007_dmm_k2_to_k9_summary.xlsx")
    if year == 2014 and posts == 9:
        return Path("outputs/tables/dmm_encdm_9/encdm_2014_dmm_k2_to_k9_summary.xlsx")
    if year == 2007 and posts == 23:
        return Path("outputs/tables/dmm_ennvm_23/ennvm_2007_23_dmm_k2_to_k9_summary.xlsx")
    return Path("outputs/tables/dmm_encdm_23/encdm_2014_23_dmm_k2_to_k9_summary.xlsx")


def dmm_diag_path(year, posts):
    if year == 2007 and posts == 9:
        return Path("outputs/analysis_dmm_ennvm_9_diagnostic/ENNVM_2007_9postes_diagnostic_K.xlsx")
    if year == 2014 and posts == 9:
        return Path("outputs/analysis_dmm_encdm_9_diagnostic/ENCDM_2014_9postes_diagnostic_K.xlsx")
    if year == 2007 and posts == 23:
        return Path("outputs/analysis_dmm_ennvm_23_diagnostic/ENNVM_2007_23postes_diagnostic_K.xlsx")
    return Path("outputs/analysis_dmm_encdm_23_diagnostic/ENCDM_2014_23postes_diagnostic_K.xlsx")


def dpmm_diag_path(year, posts):
    if year == 2007 and posts == 9:
        return Path("outputs/analysis_dpmm_ennvm_9/ENNVM_2007_DPMM_9postes_diagnostic.xlsx")
    if year == 2014 and posts == 9:
        return Path("outputs/analysis_dpmm_encdm_9/ENCDM_2014_DPMM_9postes_diagnostic.xlsx")
    if year == 2007 and posts == 23:
        return Path("outputs/analysis_dpmm_ennvm_23/ENNVM_2007_DPMM_23postes_diagnostic.xlsx")
    return Path("outputs/analysis_dpmm_encdm_23/ENCDM_2014_DPMM_23postes_diagnostic.xlsx")


def dpmm_profile_path(year, posts, prior):
    if year == 2007 and posts == 9:
        prefix = "ennvm_2007_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain"
        return Path("outputs/tables/dpmm_ennvm_9") / f"{prefix}_{prior}_profiles_full.xlsx"
    if year == 2014 and posts == 9:
        prefix = "encdm_2014_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain"
        return Path("outputs/tables/dpmm_encdm_9") / f"{prefix}_{prior}_profiles_full.xlsx"
    if year == 2007 and posts == 23:
        prefix = "ennvm_2007_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"
        return Path("outputs/tables/dpmm_ennvm_23") / f"{prefix}_{prior}_profiles_full.xlsx"
    prefix = "encdm_2014_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"
    return Path("outputs/tables/dpmm_encdm_23") / f"{prefix}_{prior}_profiles_full.xlsx"


def weighted_mean(rows, cols):
    total = sum(float(r["cluster_size"]) for r in rows)
    return {c: sum(float(r["cluster_size"]) * float(r[c]) for r in rows) / total for c in cols}


def dominant_post(row, rows, posts):
    cols = cols_for(posts)
    gm = weighted_mean(rows, cols)
    deltas = {c: float(row[c]) - gm[c] for c in cols}
    col = max(deltas, key=deltas.get)
    label = col.replace("w_", "")
    return label, float(row[col]), deltas[col]


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
        bbox={"boxstyle": "round,pad=0.22", "facecolor": "white", "edgecolor": "#d0d0d0", "alpha": 0.94},
    )


def add_post_legend(fig, posts, used=None, y=-0.12):
    cmap = color_map(posts)
    labels = labels_for(posts)
    if used:
        labels = [x for x in labels if x in used]
    handles = [
        Line2D([0], [0], marker="s", linestyle="", markersize=22, markerfacecolor=cmap[label], markeredgecolor="white", label=label)
        for label in labels
    ]
    ncol = 3 if posts == 9 else 5
    fig.legend(
        handles=handles,
        loc="lower center",
        ncol=ncol,
        frameon=True,
        fancybox=False,
        edgecolor="#d0d0d0",
        facecolor="white",
        bbox_to_anchor=(0.5, y),
        columnspacing=1.4,
        handletextpad=0.6,
        labelspacing=1.05,
        borderpad=0.7,
        fontsize=24,
    )


def save(fig, pdf, path):
    fig.savefig(path)
    pdf.savefig(fig)
    plt.close(fig)


def fig1_fragmentation(posts):
    cmap = FRAGMENTATION_COLORS
    fig, axes = plt.subplots(1, 2, figsize=(19.5, 10.2), sharex=True, sharey=True, constrained_layout=True)
    used = set()
    for ax, year in zip(axes, [2007, 2014]):
        for k in range(2, 10):
            rows = read_xlsx(dmm_profile_path(year, posts, k))
            total = sum(float(r["cluster_size"]) for r in rows)
            ranked = sorted(rows, key=lambda r: fragmentation_profile(r, posts)[1])
            for i, r in enumerate(ranked):
                label, share, _ = fragmentation_profile(r, posts)
                used.add(label)
                x = k + (i - (len(ranked) - 1) / 2) * 0.06
                y = 100 * share
                size = 35 + 1050 * float(r["cluster_size"]) / total
                ax.scatter(x, y, s=size, color=cmap[label], alpha=0.83, edgecolor="white", linewidth=0.8)
        panel_label(ax, str(year))
        ax.set_xticks(range(2, 10))
        ax.set_xlabel("K")
        ax.grid(axis="y", color="#ececec", linewidth=0.8)
        ax.set_ylim(0, 70 if posts == 9 else 85)
    axes[0].set_ylabel("Part du groupe dominant (%)")
    subtitle = "9 postes: postes originaux" if posts == 9 else "23 postes: sous-postes agreges en familles"
    fig.suptitle(f"Fragmentation des profils DMM selon K - {subtitle}", y=1.03, fontsize=12, fontweight="bold")
    labels = [label for label, _ in fragmentation_groups(posts) if label in used]
    handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markersize=22,
            markerfacecolor=cmap[label],
            markeredgecolor="white",
            label=label,
        )
        for label in labels
    ]
    size_handles = [
        plt.scatter([], [], s=35 + 1050 * share, color="#b8b8b8", alpha=0.55, edgecolor="white", label=label)
        for share, label in [(0.05, "5% des menages"), (0.20, "20% des menages")]
    ]
    fig.legend(
        handles=handles + size_handles,
        loc="lower center",
        ncol=3,
        frameon=True,
        fancybox=False,
        edgecolor="#d0d0d0",
        facecolor="white",
        bbox_to_anchor=(0.5, -0.18),
        columnspacing=1.4,
        handletextpad=0.6,
        labelspacing=1.05,
        borderpad=0.7,
        fontsize=24,
    )
    return fig


def fig2_stacked_k6(posts):
    cmap = color_map(posts)
    labels = labels_for(posts)
    cols = cols_for(posts)
    fig, axes = plt.subplots(1, 2, figsize=(23.0 if posts == 23 else 19.5, 11.0), sharex=True, constrained_layout=True)
    for ax, year in zip(axes, [2007, 2014]):
        rows = read_xlsx(dmm_profile_path(year, posts, 6))
        rows = sorted(rows, key=lambda r: float(r[cols[0]]), reverse=True)
        total = sum(float(r["cluster_size"]) for r in rows)
        y = np.arange(len(rows))
        left = np.zeros(len(rows))
        for label, col in zip(labels, cols):
            vals = np.array([100 * float(r[col]) for r in rows])
            ax.barh(y, vals, left=left, color=cmap[label], edgecolor="white", linewidth=0.45)
            left += vals
        ax.set_yticks(y)
        ax.set_yticklabels([f"C{cluster_id(r)}  {100*float(r['cluster_size'])/total:.0f}%" for r in rows])
        ax.invert_yaxis()
        ax.set_xlim(0, 100)
        ax.set_xlabel("%")
        ax.grid(axis="x", color="#eeeeee", linewidth=0.8)
        panel_label(ax, str(year))
    add_post_legend(fig, posts, y=-0.18 if posts == 23 else -0.16)
    return fig


def fig3_quality_k(posts):
    fig, axes = plt.subplots(1, 2, figsize=(18.0, 8.2), sharex=True, sharey=True, constrained_layout=True)
    for ax, year in zip(axes, [2007, 2014]):
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
        ax.axvline(6, color="#333333", lw=1, ls="--", label="K=6")
        ax.set_xticks(range(2, 10))
        ax.set_ylim(0, 105)
        ax.set_xlabel("K")
        ax.grid(axis="y", color="#eeeeee", linewidth=0.8)
        panel_label(ax, str(year))
    axes[0].set_ylabel("%")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="lower center",
        ncol=4,
        frameon=True,
        fancybox=False,
        edgecolor="#d0d0d0",
        facecolor="white",
        bbox_to_anchor=(0.5, -0.12),
        columnspacing=1.4,
        handletextpad=0.65,
        borderpad=0.7,
        fontsize=24,
    )
    return fig


def rows_where(rows, **kwargs):
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


def quant_row(rows, variable, cluster):
    matches = [r for r in rows if r["variable"] == variable and int(r["cluster"]) == cluster]
    return matches[0] if matches else None


def find_size_variable(rows):
    variables = sorted(set(r["variable"] for r in rows))
    for v in variables:
        if str(v).startswith("Taille"):
            return v
    return None


def global_quant(diag, k, variable):
    rows = read_xlsx(diag, "01_global_descriptives")
    matches = [
        r for r in rows
        if int(r["K"]) == k and r["variable"] == variable and r.get("type") == "quantitative"
    ]
    return matches[0] if matches else None


def avg_quintile_delta(rows, cluster):
    vals = []
    for r in rows:
        if r["variable"] != "quintile_DAM" or int(r["cluster"]) != cluster:
            continue
        try:
            q = float(r["modalite"])
        except Exception:
            continue
        row_pct = float(r.get("weighted_row_pct", r.get("row_pct", 0)))
        global_pct = float(r.get("weighted_global_pct", r.get("global_pct", 0)))
        vals.append((q, row_pct, global_pct))
    if not vals:
        return 0.0
    return sum(q * p for q, p, _ in vals) - sum(q * g for q, _, g in vals)


def education_delta(rows, year, cluster):
    if year == 2007:
        variables = ["Niveau_scolaire_CM"]
    else:
        variables = ["Niveau_scolaire_agreg_CM", "Diplome_agrege_CM", "Diplôme_agregé_CM"]
    for variable in variables:
        for r in rows:
            if r["variable"] == variable and int(r["cluster"]) == cluster and "Sup" in str(r["modalite"]):
                return 100 * float(r["delta_vs_global"])
    return 0.0


def aligned_cluster_orders(posts):
    cols = cols_for(posts)
    rows_2007 = read_xlsx(dmm_profile_path(2007, posts, 6))
    rows_2014 = read_xlsx(dmm_profile_path(2014, posts, 6))
    vectors_2007 = np.array([[float(r[c]) for c in cols] for r in rows_2007])
    vectors_2014 = np.array([[float(r[c]) for c in cols] for r in rows_2014])
    cost = np.linalg.norm(vectors_2007[:, None, :] - vectors_2014[None, :, :], axis=2)
    row_ind, col_ind = linear_sum_assignment(cost)
    match_2014 = {cluster_id(rows_2007[i]): cluster_id(rows_2014[j]) for i, j in zip(row_ind, col_ind)}
    order_2007 = [cluster_id(r) for r in rows_2007]
    order_2014 = [match_2014[c] for c in order_2007]
    return {2007: order_2007, 2014: order_2014}, match_2014


def socio_matrix(year, posts, cluster_order=None):
    diag = dmm_diag_path(year, posts)
    k = 6
    q = [r for r in read_xlsx(diag, "06_quantitative_by_cluster") if int(r["K"]) == k]
    d = [r for r in read_xlsx(diag, "04_crosstab_global_delta") if int(r["K"]) == k]
    prof = read_xlsx(dmm_profile_path(year, posts, k))
    clusters = cluster_order if cluster_order is not None else [cluster_id(r) for r in prof]
    size_var = find_size_variable(q)
    dam_global = global_quant(diag, k, "DAM")
    size_global = global_quant(diag, k, size_var) if size_var else None
    data, labels = [], []
    for cluster in clusters:
        dam = quant_row(q, "DAM", cluster)
        size = quant_row(q, size_var, cluster) if size_var else None
        rural = rows_where(d, variable="Milieu", cluster=cluster, modalite="Rural")
        urban = rows_where(d, variable="Milieu", cluster=cluster, modalite="Urbain")
        row = [
            100 * float(dam["relative_delta_mean_vs_global"]) if dam else 0,
            100 * (float(dam["median"]) / float(dam_global["median"]) - 1) if dam and dam_global else 0,
            100 * float(rural[0]["delta_vs_global"]) if rural else 0,
            100 * float(urban[0]["delta_vs_global"]) if urban else 0,
            20 * avg_quintile_delta(d, cluster),
            100 * (float(size["mean"]) / float(size_global["mean"]) - 1) if size and size_global else 0,
            education_delta(d, year, cluster),
        ]
        data.append(row)
        labels.append(f"C{cluster}")
    return np.array(data), labels


def fig4_socio_heatmap(posts):
    # Kept as a compatibility wrapper for callers that expect a single figure.
    return fig4_all_crosstabs(2007, posts)


def cat_delta(rows, cluster, variable, modalite):
    for r in rows:
        if int(r["cluster"]) == cluster and str(r["variable"]) == variable and str(r["modalite"]) == modalite:
            metric = r.get("weighted_delta_vs_global", r.get("delta_vs_global", 0))
            return 100 * float(metric)
    return 0.0


def quant_delta(rows, cluster, variable, mode="relative"):
    r = quant_row(rows, variable, cluster)
    if not r:
        return 0.0
    if mode == "points":
        return 100 * float(r.get("weighted_delta_vs_global", r.get("delta_mean_vs_global", 0)))
    return 100 * float(r.get("relative_delta_mean_vs_global", 0))


def popular_modalite(rows, variable):
    candidates = {}
    for r in rows:
        if str(r["variable"]) != variable:
            continue
        modalite = str(r["modalite"])
        pct = r.get("weighted_global_pct", r.get("global_pct", 0))
        candidates[modalite] = max(candidates.get(modalite, -np.inf), float(pct))
    if not candidates:
        return ""
    return max(candidates, key=candidates.get)


def crosstab_explanatory_matrix(year, posts):
    q = [r for r in read_xlsx(dmm_diag_path(year, posts), "06_quantitative_by_cluster") if int(r["K"]) == 6]
    d = [r for r in read_xlsx(dmm_diag_path(year, posts), "04_crosstab_global_delta") if int(r["K"]) == 6]
    try:
        clusters = aligned_cluster_orders(posts)[0][year]
    except Exception:
        clusters = sorted({int(r["cluster"]) for r in d})

    education_var = "Niveau_scolaire_CM" if year == 2007 else "Niveau_scolaire_agreg_CM"
    education_modalite = popular_modalite(d, education_var)
    columns = [
        "DAM moy.",
        "Quintile DAM",
        "Urbain",
        "Rural",
        "Chef feminin",
        "Chef masculin",
        "Taille menage",
        "% enfants",
        f"Etudes: {education_modalite}",
    ]

    data = []
    for cluster in clusters:
        row = [
            quant_delta(q, cluster, "DAM", "relative"),
            20 * avg_quintile_delta(d, cluster),
            cat_delta(d, cluster, "Milieu", "Urbain"),
            cat_delta(d, cluster, "Milieu", "Rural"),
            cat_delta(d, cluster, "Sexe_CM", "Féminin"),
            cat_delta(d, cluster, "Sexe_CM", "Masculin"),
            quant_delta(q, cluster, "Taille_ménage", "relative"),
            quant_delta(q, cluster, "p_children", "points"),
            cat_delta(d, cluster, education_var, education_modalite),
        ]
        data.append(row)
    return np.array(data), clusters, columns


def short_label(text, max_len=28):
    text = str(text).replace("_", " ")
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "."


def fig4_all_crosstabs(year, posts):
    mat, clusters, columns = crosstab_explanatory_matrix(year, posts)
    n_cols = mat.shape[1]
    fig_w = 17.5
    fig_h = 8.8
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), constrained_layout=True)
    vmax = min(55, max(10, float(np.nanpercentile(np.abs(mat), 98))))
    im = ax.imshow(mat, cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto")

    ax.set_xticks(range(n_cols))
    ax.set_xticklabels(columns, rotation=35, ha="right", fontsize=14)
    ax.set_yticks(range(len(clusters)))
    ax.set_yticklabels([f"C{c}" for c in clusters], fontsize=18)
    ax.tick_params(length=0)

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if abs(mat[i, j]) >= 8:
                ax.text(j, i, f"{mat[i, j]:+.0f}", ha="center", va="center", fontsize=12)

    ax.set_title(f"Ancrage socio-economique enrichi - {year} - K=6 - {posts} postes", fontsize=24, pad=18)
    ax.set_ylabel("Clusters DMM", fontsize=20)
    cbar = fig.colorbar(im, ax=ax, shrink=0.82, location="right")
    cbar.set_label("Ecart au global (% / points)", fontsize=24)
    cbar.ax.tick_params(labelsize=18)
    return fig


def fig5_dpmm_prior_weights(posts):
    fig, axes = plt.subplots(2, 4, figsize=(21.5, 10.2), sharex=True, sharey=True, constrained_layout=True)
    for row_idx, year in enumerate([2007, 2014]):
        diag = dpmm_diag_path(year, posts)
        cluster_rows = read_xlsx(diag, "02_cluster_summary")
        for col_idx, prior in enumerate(PRIORS):
            ax = axes[row_idx, col_idx]
            rows = [r for r in cluster_rows if r["prior"] == prior]
            rows = sorted(rows, key=lambda r: int(r["cluster"]))
            x = [int(r["cluster"]) for r in rows]
            y = [100 * float(r["posterior_weight_mean"]) for r in rows]
            ax.bar(x, y, color="#457b9d", edgecolor="white", linewidth=0.6)
            for thr in [1, 2, 3]:
                ax.axhline(thr, color="#777777", lw=0.8, ls="--", alpha=0.65)
            if row_idx == 0:
                ax.set_title(PRIOR_LABELS[prior])
            if col_idx == 0:
                ax.set_ylabel(f"{year}\n%")
            ax.set_xticks(range(1, 8))
            ax.set_ylim(0, 55)
            ax.grid(axis="y", color="#eeeeee", linewidth=0.7)
    handles = [Line2D([0], [0], color="#777777", lw=0.8, ls="--", label="1 %, 2 %, 3 %")]
    fig.legend(
        handles=handles,
        loc="lower center",
        frameon=True,
        fancybox=False,
        edgecolor="#d0d0d0",
        facecolor="white",
        bbox_to_anchor=(0.5, -0.1),
        borderpad=0.7,
        fontsize=24,
    )
    return fig


def dominant_counts(rows, posts):
    labels = labels_for(posts)
    counts = {label: 0 for label in labels}
    for r in rows:
        label, _, delta = dominant_post(r, rows, posts)
        if delta > 0:
            counts[label] += 1
    return counts


def convergence_matrix(posts):
    specs = []
    for year in [2007, 2014]:
        specs.append((f"DMM {year}", read_xlsx(dmm_profile_path(year, posts, 6))))
        prior = PREFERRED_PRIOR[(year, posts)]
        specs.append((f"DPMM {year}", read_xlsx(dpmm_profile_path(year, posts, prior))))
    labels = labels_for(posts)
    mat = np.zeros((len(labels), len(specs)))
    for j, (_, rows) in enumerate(specs):
        counts = dominant_counts(rows, posts)
        for i, label in enumerate(labels):
            mat[i, j] = counts[label]
    return mat, labels, [name for name, _ in specs]


def fig6_convergence(posts):
    mat, row_labels, col_labels = convergence_matrix(posts)
    height = 5.6 if posts == 9 else 8.6
    fig, ax = plt.subplots(figsize=(12.5, height + 2.4), constrained_layout=True)
    im = ax.imshow(mat, cmap="YlGnBu", vmin=0, vmax=max(1, np.nanmax(mat)), aspect="auto")
    ax.set_xticks(range(len(col_labels)))
    ax.set_xticklabels(col_labels, rotation=20, ha="right")
    ax.set_yticks(range(len(row_labels)))
    ax.set_yticklabels(row_labels)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, str(int(mat[i, j])), ha="center", va="center", fontsize=13)
    ax.tick_params(length=0)
    fig.colorbar(im, ax=ax, shrink=0.82, location="right")
    return fig


def generate_for(posts):
    out_dir = OUT_ROOT / f"{posts}postes"
    out_dir.mkdir(parents=True, exist_ok=True)
    figures_before_socio = [
        (fig1_fragmentation, f"fig_01_fragmentation_K_{posts}postes.pdf"),
        (fig2_stacked_k6, f"fig_02_barres_empilees_K6_{posts}postes.pdf"),
        (fig3_quality_k, f"fig_03_qualite_stabilite_K_{posts}postes.pdf"),
    ]
    figures_after_socio = [
        (fig5_dpmm_prior_weights, f"fig_05_poids_DPMM_prior_{posts}postes.pdf"),
        (fig6_convergence, f"fig_06_convergence_DMM_DPMM_{posts}postes.pdf"),
    ]
    combined = out_dir / f"figures_dirichlet_313_{posts}postes.pdf"
    with PdfPages(combined) as pdf:
        print(combined)
        for maker, filename in figures_before_socio:
            path = out_dir / filename
            save(maker(posts), pdf, path)
            print(path)
        for year in [2007, 2014]:
            path = out_dir / f"fig_04_ancrage_socioeconomique_K6_{year}_{posts}postes.pdf"
            save(fig4_all_crosstabs(year, posts), pdf, path)
            print(path)
        for maker, filename in figures_after_socio:
            path = out_dir / filename
            save(maker(posts), pdf, path)
            print(path)


def main():
    setup_style()
    generate_for(9)
    generate_for(23)


if __name__ == "__main__":
    main()
