from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D

from figures_interpretation_dirichlet import (
    G_COLS,
    G_LABELS,
    OUT_DIR as OLD_OUT_DIR,
    PALETTE,
    PROJECT_ROOT,
    S_FAMILIES,
    cluster_id,
    dmm_profile_path,
    dominant_deviation,
    dominant_family,
    dpmm_diag_path,
    dpmm_profile_path,
    family_values,
    family_weighted_mean,
    read_xlsx,
    weighted_mean,
)


OUT_DIR = PROJECT_ROOT / "outputs" / "figures" / "interpretation_dirichlet_claires"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PRIOR_LABELS = {
    "gamma_1_1": "G(1,1)",
    "gamma_1_2": "G(1,2)",
    "gamma_0p5_2": "G(.5,2)",
    "gamma_0p25_2": "G(.25,2)",
}

FAMILY_ORDER = [
    "Alimentaire",
    "Logement-energie",
    "Sante",
    "Transp.-comm.",
    "Culture-ens.",
    "Habillement",
    "Equipement",
    "Autres",
]


def setup_style():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "axes.titlesize": 15,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.bbox": "tight",
        }
    )


def save(fig, pdf, filename):
    fig.savefig(OUT_DIR / filename)
    pdf.savefig(fig)
    plt.close(fig)


def short_title(fig, title, note=None):
    fig.suptitle(title, x=0.02, y=0.985, ha="left", va="top", fontsize=18, fontweight="bold")
    if note:
        fig.text(0.02, 0.94, note, ha="left", va="top", fontsize=11, color="#555555")


def figure_1_k_landscape():
    fig, axes = plt.subplots(1, 2, figsize=(15.2, 7.4), sharey=True, constrained_layout=True)
    short_title(fig, "DMM 9 postes : comment les profils se fragmentent", "Chaque point est un cluster ; plus il est grand, plus le cluster pese dans l'echantillon.")
    used = set()
    for ax, (case_key, title) in zip(axes, [("2007", "ENNVM 2007"), ("2014", "ENCDM 2014")]):
        for k in range(2, 10):
            rows = read_xlsx(dmm_profile_path(case_key, 9, k))
            gm = weighted_mean(rows, G_COLS)
            total = sum(float(r["cluster_size"]) for r in rows)
            rows = sorted(rows, key=lambda r: float(r["w_G1"]))
            for rank, row in enumerate(rows):
                col, _ = dominant_deviation(row, gm, G_COLS)
                label = G_LABELS[col]
                used.add(label)
                x = k + (rank - (len(rows) - 1) / 2) * 0.052
                y = 100 * float(row["w_G1"])
                size = 80 + 1050 * float(row["cluster_size"]) / total
                ax.scatter(x, y, s=size, color=PALETTE[label], alpha=0.82, edgecolor="white", linewidth=1.0)
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_xlabel("K")
        ax.set_xticks(range(2, 10))
        ax.grid(axis="y", color="#e9e9e9", linewidth=0.9)
        ax.set_xlim(1.6, 9.4)
    axes[0].set_ylabel("Part alimentaire G1 (%)")
    handles = [
        Line2D([0], [0], marker="o", linestyle="", markersize=9, markerfacecolor=PALETTE[k], markeredgecolor="white", label=k)
        for k in sorted(used)
    ]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.02))
    return fig


def stacked_g9(ax, rows, title):
    rows = sorted(rows, key=lambda r: float(r["w_G1"]), reverse=True)
    y = np.arange(len(rows))
    left = np.zeros(len(rows))
    for col in G_COLS:
        values = np.array([100 * float(r[col]) for r in rows])
        label = G_LABELS[col]
        ax.barh(y, values, left=left, color=PALETTE[label], edgecolor="white", linewidth=0.6, label=label)
        left += values
    total = sum(float(r["cluster_size"]) for r in rows)
    ax.set_yticks(y)
    ax.set_yticklabels([f"C{cluster_id(r)}  {100*float(r['cluster_size'])/total:.0f}%" for r in rows])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Part budgetaire du cluster (%)")
    ax.set_title(title, loc="left", fontweight="bold")
    ax.grid(axis="x", color="#eeeeee")
    ax.invert_yaxis()


def figure_2_dmm9_stacked_k6():
    fig, axes = plt.subplots(1, 2, figsize=(15.2, 8.2), sharex=True, constrained_layout=True)
    short_title(fig, "DMM 9 postes : profils retenus en K=6", "Barres empilees : composition budgetaire moyenne de chaque cluster.")
    rows_2007 = read_xlsx(dmm_profile_path("2007", 9, 6))
    rows_2014 = read_xlsx(dmm_profile_path("2014", 9, 6))
    stacked_g9(axes[0], rows_2007, "ENNVM 2007")
    stacked_g9(axes[1], rows_2014, "ENCDM 2014")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.02))
    return fig


def stacked_families(ax, rows, title):
    rows = sorted(rows, key=lambda r: family_values(r)["Alimentaire"], reverse=True)
    y = np.arange(len(rows))
    left = np.zeros(len(rows))
    total = sum(float(r["cluster_size"]) for r in rows)
    for fam in FAMILY_ORDER:
        values = np.array([100 * family_values(r)[fam] for r in rows])
        ax.barh(y, values, left=left, color=PALETTE[fam], edgecolor="white", linewidth=0.6, label=fam)
        left += values
    ax.set_yticks(y)
    ax.set_yticklabels([f"C{cluster_id(r)}  {100*float(r['cluster_size'])/total:.0f}%" for r in rows])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Part budgetaire du cluster (%)")
    ax.set_title(title, loc="left", fontweight="bold")
    ax.grid(axis="x", color="#eeeeee")
    ax.invert_yaxis()


def figure_3_dmm23_family_stacked_k7():
    fig, axes = plt.subplots(1, 2, figsize=(15.2, 8.6), sharex=True, constrained_layout=True)
    short_title(fig, "DMM 23 postes : lecture par grandes familles", "K=7, avec les 23 postes regroupes en familles economiques lisibles.")
    rows_2007 = read_xlsx(dmm_profile_path("2007", 23, 7))
    rows_2014 = read_xlsx(dmm_profile_path("2014", 23, 7))
    stacked_families(axes[0], rows_2007, "ENNVM 2007")
    stacked_families(axes[1], rows_2014, "ENCDM 2014")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.03))
    return fig


def figure_4_dpmm_prior_dotplot():
    priors = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]
    cases = [
        ("2007", 9, "2007, 9 postes"),
        ("2014", 9, "2014, 9 postes"),
        ("2007", 23, "2007, 23 postes"),
        ("2014", 23, "2014, 23 postes"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(15.2, 8.6), sharey=True, constrained_layout=True)
    short_title(fig, "DPMM : sensibilite aux priors", "Deux indicateurs seulement : ambiguite des affectations et taille du plus petit cluster.")
    for ax, (case_key, posts, title) in zip(axes.ravel(), cases):
        diag = dpmm_diag_path(case_key, posts)
        p_summary = read_xlsx(diag, "01_prior_summary")
        c_summary = read_xlsx(diag, "02_cluster_summary")
        x = np.arange(len(priors))
        ambiguous = []
        min_cluster = []
        k_eff = []
        for prior in priors:
            pr = [r for r in p_summary if r["prior"] == prior][0]
            cc = [r for r in c_summary if r["prior"] == prior]
            ambiguous.append(100 * float(pr["share_ambiguous_full_lt_0_60"]))
            min_cluster.append(100 * min(float(r["assigned_share_full"]) for r in cc))
            k_eff.append(sum(float(r["posterior_weight_mean"]) >= 0.02 for r in cc))
        ax.plot(x, ambiguous, marker="o", lw=2.2, color="#e76f51", label="Ambigus")
        ax.plot(x, min_cluster, marker="o", lw=2.2, color="#2a9d8f", label="Cluster min.")
        for xi, ke in zip(x, k_eff):
            ax.text(xi, 25.4, f"K{ke}", ha="center", va="center", fontsize=9, color="#333333")
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels([PRIOR_LABELS[p] for p in priors])
        ax.set_ylim(0, 28)
        ax.grid(axis="y", color="#eeeeee")
    axes[0, 0].set_ylabel("%")
    axes[1, 0].set_ylabel("%")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.015))
    return fig


def figure_5_dpmm23_socio_clear():
    cases = [
        ("2007", "ENNVM 2007", "gamma_0p25_2"),
        ("2014", "ENCDM 2014", "gamma_1_1"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(15.2, 7.8), constrained_layout=True)
    short_title(fig, "DPMM 23 postes : gradient socio-economique", "Position des clusters selon le niveau de depense et la part rurale.")
    used_families = set()
    for ax, (case_key, title, prior) in zip(axes, cases):
        diag = dpmm_diag_path(case_key, 23)
        q = [r for r in read_xlsx(diag, "08_quant_by_cluster") if r["prior"] == prior and r["variable"] == "DAM"]
        ctab = [r for r in read_xlsx(diag, "06_crosstab_delta") if r["prior"] == prior and r["variable"] == "Milieu"]
        clusters = [r for r in read_xlsx(diag, "02_cluster_summary") if r["prior"] == prior]
        profiles = read_xlsx(dpmm_profile_path(case_key, 23, prior))
        fg = family_weighted_mean(profiles)
        rural_global = None
        for row in ctab:
            if str(row["modalite"]).lower() == "rural":
                rural_global = 100 * float(row["global_pct"])
                break
        points = []
        for row in q:
            cluster = int(row["cluster"])
            prof = [p for p in profiles if cluster_id(p) == cluster][0]
            fam = dominant_family(prof, fg)
            used_families.add(fam)
            rural_rows = [r for r in ctab if int(r["cluster"]) == cluster and str(r["modalite"]).lower() == "rural"]
            c_rows = [r for r in clusters if int(r["cluster"]) == cluster]
            x = 100 * float(row["relative_delta_mean_vs_global"])
            y = 100 * float(rural_rows[0]["row_pct"]) if rural_rows else 0
            share = 100 * float(c_rows[0]["assigned_share_full"]) if c_rows else 3
            points.append((x, y, share, cluster, fam))
        for x, y, share, cluster, fam in points:
            ax.scatter(x, y, s=120 + 35 * share, color=PALETTE[fam], alpha=0.86, edgecolor="white", linewidth=1.1)
            ax.text(x, y, str(cluster), ha="center", va="center", fontsize=10, fontweight="bold")
        ax.axvline(0, color="#9a9a9a", lw=1, ls="--")
        if rural_global is not None:
            ax.axhline(rural_global, color="#9a9a9a", lw=1, ls="--")
        ax.set_title(f"{title} - {PRIOR_LABELS[prior]}", loc="left", fontweight="bold")
        ax.set_xlabel("Ecart de DAM moyenne (%)")
        ax.set_ylabel("Part rurale (%)")
        ax.grid(color="#eeeeee")
    handles = [
        Line2D([0], [0], marker="o", linestyle="", markersize=9, markerfacecolor=PALETTE[f], markeredgecolor="white", label=f)
        for f in sorted(used_families)
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.02))
    return fig


def main():
    setup_style()
    combined = OUT_DIR / "figures_interpretation_dirichlet_claires_2007_2014.pdf"
    figures = [
        (figure_1_k_landscape, "fig_01_DMM9_fragmentation_K_clair.pdf"),
        (figure_2_dmm9_stacked_k6, "fig_02_DMM9_K6_barres_clair.pdf"),
        (figure_3_dmm23_family_stacked_k7, "fig_03_DMM23_K7_familles_clair.pdf"),
        (figure_4_dpmm_prior_dotplot, "fig_04_DPMM_priors_clair.pdf"),
        (figure_5_dpmm23_socio_clear, "fig_05_DPMM23_gradient_clair.pdf"),
    ]
    with PdfPages(combined) as pdf:
        for maker, filename in figures:
            fig = maker()
            save(fig, pdf, filename)
    print(combined)
    for _, filename in figures:
        print(OUT_DIR / filename)
    print(f"Ancien dossier conserve si besoin: {OLD_OUT_DIR}")


if __name__ == "__main__":
    main()
