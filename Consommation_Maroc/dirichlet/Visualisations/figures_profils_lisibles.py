from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from figures_interpretation_dirichlet import (
    G_COLS,
    G_LABELS,
    PALETTE,
    PROJECT_ROOT,
    S_FAMILIES,
    cluster_id,
    dmm_profile_path,
    family_values,
    read_xlsx,
)


OUT_DIR = PROJECT_ROOT / "outputs" / "figures" / "profils_lisibles"
OUT_DIR.mkdir(parents=True, exist_ok=True)

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

FAMILY_SHORT = {
    "Alimentaire": "Alimentaire",
    "Logement-energie": "Logement-energie",
    "Sante": "Sante",
    "Transp.-comm.": "Transport-comm.",
    "Culture-ens.": "Culture-ens.",
    "Habillement": "Habillement",
    "Equipement": "Equipement",
    "Autres": "Autres",
}


def setup_style():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 14,
            "axes.titlesize": 19,
            "axes.labelsize": 14,
            "xtick.labelsize": 12,
            "ytick.labelsize": 13,
            "legend.fontsize": 12,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.bbox": "tight",
        }
    )


def cluster_label(row, total):
    share = 100 * float(row["cluster_size"]) / total
    return f"C{cluster_id(row)}   {share:.0f}%"


def annotate_big_segments(ax, y, left, width, text, color="white"):
    if width < 8:
        return
    ax.text(
        left + width / 2,
        y,
        text,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color=color,
    )


def make_dmm9_page(case_key, title):
    rows = read_xlsx(dmm_profile_path(case_key, 9, 6))
    rows = sorted(rows, key=lambda r: float(r["w_G1"]), reverse=True)
    total = sum(float(r["cluster_size"]) for r in rows)

    fig, ax = plt.subplots(figsize=(15.5, 9.2))
    y = np.arange(len(rows))
    left = np.zeros(len(rows))

    for col in G_COLS:
        values = np.array([100 * float(r[col]) for r in rows])
        label = G_LABELS[col]
        bars = ax.barh(
            y,
            values,
            left=left,
            color=PALETTE[label],
            edgecolor="white",
            linewidth=0.8,
            label=label,
        )
        for i, value in enumerate(values):
            annotate_big_segments(ax, y[i], left[i], value, f"{label}\n{value:.0f}%")
        left += values

    ax.set_yticks(y)
    ax.set_yticklabels([cluster_label(r, total) for r in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Composition budgetaire moyenne du cluster (%)")
    ax.set_title(title, loc="left", fontweight="bold", pad=18)
    ax.grid(axis="x", color="#e7e7e7", linewidth=0.9)
    ax.text(
        0,
        1.02,
        "DMM 9 postes, K = 6. Les segments non annotes sont volontairement laisses sans texte pour garder la figure lisible.",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=12,
        color="#555555",
    )
    ax.legend(
        loc="center left",
        bbox_to_anchor=(1.015, 0.5),
        frameon=False,
        title="Postes",
        title_fontsize=13,
    )
    fig.subplots_adjust(left=0.13, right=0.78, top=0.84, bottom=0.12)
    return fig


def make_dmm23_page(case_key, title):
    rows = read_xlsx(dmm_profile_path(case_key, 23, 7))
    rows = sorted(rows, key=lambda r: family_values(r)["Alimentaire"], reverse=True)
    total = sum(float(r["cluster_size"]) for r in rows)

    fig, ax = plt.subplots(figsize=(15.5, 9.8))
    y = np.arange(len(rows))
    left = np.zeros(len(rows))

    for fam in FAMILY_ORDER:
        values = np.array([100 * family_values(r)[fam] for r in rows])
        label = FAMILY_SHORT[fam]
        ax.barh(
            y,
            values,
            left=left,
            color=PALETTE[fam],
            edgecolor="white",
            linewidth=0.8,
            label=label,
        )
        for i, value in enumerate(values):
            annotate_big_segments(ax, y[i], left[i], value, f"{label}\n{value:.0f}%")
        left += values

    ax.set_yticks(y)
    ax.set_yticklabels([cluster_label(r, total) for r in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Composition budgetaire moyenne du cluster (%)")
    ax.set_title(title, loc="left", fontweight="bold", pad=18)
    ax.grid(axis="x", color="#e7e7e7", linewidth=0.9)
    ax.text(
        0,
        1.02,
        "DMM 23 postes, K = 7. Les 23 postes sont regroupes en familles pour faciliter l'interpretation.",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=12,
        color="#555555",
    )
    ax.legend(
        loc="center left",
        bbox_to_anchor=(1.015, 0.5),
        frameon=False,
        title="Familles",
        title_fontsize=13,
    )
    fig.subplots_adjust(left=0.13, right=0.76, top=0.84, bottom=0.12)
    return fig


def save(fig, pdf, filename):
    fig.savefig(OUT_DIR / filename)
    pdf.savefig(fig)
    plt.close(fig)


def main():
    setup_style()
    pages = [
        (lambda: make_dmm9_page("2007", "ENNVM 2007 - profils DMM 9 postes"), "fig_02A_DMM9_K6_2007_lisible.pdf"),
        (lambda: make_dmm9_page("2014", "ENCDM 2014 - profils DMM 9 postes"), "fig_02B_DMM9_K6_2014_lisible.pdf"),
        (lambda: make_dmm23_page("2007", "ENNVM 2007 - profils DMM 23 postes"), "fig_03A_DMM23_K7_2007_lisible.pdf"),
        (lambda: make_dmm23_page("2014", "ENCDM 2014 - profils DMM 23 postes"), "fig_03B_DMM23_K7_2014_lisible.pdf"),
    ]
    combined = OUT_DIR / "figures_profils_DMM_lisibles.pdf"
    with PdfPages(combined) as pdf:
        for maker, filename in pages:
            save(maker(), pdf, filename)

    print(combined)
    for _, filename in pages:
        print(OUT_DIR / filename)


if __name__ == "__main__":
    main()
