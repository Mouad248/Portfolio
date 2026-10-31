from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from figures_interpretation_dirichlet import (
    G_COLS,
    G_LABELS,
    PALETTE,
    PROJECT_ROOT,
    cluster_id,
    dmm_profile_path,
    family_values,
    read_xlsx,
)


OUT_DIR = PROJECT_ROOT / "outputs" / "figures" / "profils_minimalistes"
OUT_DIR.mkdir(parents=True, exist_ok=True)

G_SHORT = {
    "Alim.": "Alim.",
    "Habill.": "Hab.",
    "Logement": "Log.",
    "Tabac": "Tabac",
    "Equip.": "Equip.",
    "Sante": "Sante",
    "Transport": "Transp.",
    "Comm.": "Comm.",
    "Culture/ens.": "Cult.",
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

FAMILY_SHORT = {
    "Alimentaire": "Alim.",
    "Logement-energie": "Log.-en.",
    "Sante": "Sante",
    "Transp.-comm.": "Transp.",
    "Culture-ens.": "Cult.",
    "Habillement": "Hab.",
    "Equipement": "Equip.",
    "Autres": "Autres",
}


def setup_style():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 14,
            "xtick.labelsize": 12,
            "ytick.labelsize": 14,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.bbox": "tight",
        }
    )


def cluster_label(row, total):
    share = 100 * float(row["cluster_size"]) / total
    return f"C{cluster_id(row)}   {share:.0f}%"


def annotate_segment(ax, y, left, width, text):
    if width < 10:
        return
    ax.text(
        left + width / 2,
        y,
        f"{text}\n{width:.0f}%",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="white",
    )


def clean_axes(ax):
    ax.set_xlim(0, 100)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100"])
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors="#555555")
    ax.grid(axis="x", color="#ededed", linewidth=0.8)


def dmm9_page(case_key):
    rows = read_xlsx(dmm_profile_path(case_key, 9, 6))
    rows = sorted(rows, key=lambda r: float(r["w_G1"]), reverse=True)
    total = sum(float(r["cluster_size"]) for r in rows)

    fig, ax = plt.subplots(figsize=(15.5, 8.6))
    y = np.arange(len(rows))
    left = np.zeros(len(rows))

    for col in G_COLS:
        values = np.array([100 * float(r[col]) for r in rows])
        label = G_LABELS[col]
        short = G_SHORT[label]
        ax.barh(y, values, left=left, color=PALETTE[label], edgecolor="white", linewidth=0.85)
        for i, value in enumerate(values):
            annotate_segment(ax, y[i], left[i], value, short)
        left += values

    ax.set_yticks(y)
    ax.set_yticklabels([cluster_label(r, total) for r in rows])
    ax.invert_yaxis()
    clean_axes(ax)
    fig.subplots_adjust(left=0.12, right=0.98, top=0.98, bottom=0.10)
    return fig


def dmm23_page(case_key):
    rows = read_xlsx(dmm_profile_path(case_key, 23, 7))
    rows = sorted(rows, key=lambda r: family_values(r)["Alimentaire"], reverse=True)
    total = sum(float(r["cluster_size"]) for r in rows)

    fig, ax = plt.subplots(figsize=(15.5, 9.0))
    y = np.arange(len(rows))
    left = np.zeros(len(rows))

    for fam in FAMILY_ORDER:
        values = np.array([100 * family_values(r)[fam] for r in rows])
        short = FAMILY_SHORT[fam]
        ax.barh(y, values, left=left, color=PALETTE[fam], edgecolor="white", linewidth=0.85)
        for i, value in enumerate(values):
            annotate_segment(ax, y[i], left[i], value, short)
        left += values

    ax.set_yticks(y)
    ax.set_yticklabels([cluster_label(r, total) for r in rows])
    ax.invert_yaxis()
    clean_axes(ax)
    fig.subplots_adjust(left=0.12, right=0.98, top=0.98, bottom=0.10)
    return fig


def color_code_page(kind):
    if kind == "g9":
        items = [(G_SHORT[G_LABELS[c]], PALETTE[G_LABELS[c]]) for c in G_COLS]
    else:
        items = [(FAMILY_SHORT[f], PALETTE[f]) for f in FAMILY_ORDER]

    n = len(items)
    fig, ax = plt.subplots(figsize=(12.0, 1.8))
    ax.set_axis_off()
    for i, (label, color) in enumerate(items):
        x = i / n
        ax.add_patch(plt.Rectangle((x + 0.01, 0.42), 0.055, 0.22, transform=ax.transAxes, color=color, clip_on=False))
        ax.text(x + 0.072, 0.53, label, transform=ax.transAxes, ha="left", va="center", fontsize=13)
    return fig


def save(fig, pdf, filename):
    fig.savefig(OUT_DIR / filename)
    pdf.savefig(fig)
    plt.close(fig)


def main():
    setup_style()
    pages = [
        (lambda: dmm9_page("2007"), "fig_02A_DMM9_K6_2007_minimal.pdf"),
        (lambda: dmm9_page("2014"), "fig_02B_DMM9_K6_2014_minimal.pdf"),
        (lambda: dmm23_page("2007"), "fig_03A_DMM23_K7_2007_minimal.pdf"),
        (lambda: dmm23_page("2014"), "fig_03B_DMM23_K7_2014_minimal.pdf"),
        (lambda: color_code_page("g9"), "code_couleurs_9postes.pdf"),
        (lambda: color_code_page("families"), "code_couleurs_familles_23postes.pdf"),
    ]
    combined = OUT_DIR / "figures_profils_DMM_minimalistes.pdf"
    with PdfPages(combined) as pdf:
        for maker, filename in pages:
            save(maker(), pdf, filename)

    print(combined)
    for _, filename in pages:
        print(OUT_DIR / filename)


if __name__ == "__main__":
    main()
