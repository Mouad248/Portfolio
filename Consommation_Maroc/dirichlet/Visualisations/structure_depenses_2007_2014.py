from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# =====================================================
# 1. Configuration
# =====================================================

RAW_FILES = {
    "ENNVM 2007": Path("data/raw/menage_ennvm_propre.xlsx"),
    "ENCDM 2014": Path("data/raw/menage_encdm_propre.xlsx"),
}

OUTPUT_DIR = Path("outputs/visualisations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PDF = OUTPUT_DIR / "structure_depenses_2007_2014_echantillon.pdf"

DAM_COL = "DAM"
POST_COLS = [f"DAM_G{i}" for i in range(1, 10)]

POST_LABELS = {
    "DAM_G1": "Alimentation & boissons",
    "DAM_G2": "Habillement & chaussures",
    "DAM_G3": "Logement, eau, energie",
    "DAM_G4": "Boissons alcool. & tabac",
    "DAM_G5": "Ameublement & equipement",
    "DAM_G6": "Sante",
    "DAM_G7": "Transport",
    "DAM_G8": "Communication",
    "DAM_G9": "Loisirs, culture & enseignement",
}

SURVEY_COLORS = {
    "ENNVM 2007": "#176D35",
    "ENCDM 2014": "#E95A0C",
}


# =====================================================
# 2. Calcul des parts budgetaires dans l'echantillon
# =====================================================

def load_required_columns(path):
    required = [DAM_COL] + POST_COLS
    header = pd.read_excel(path, nrows=0).columns.tolist()
    missing = [col for col in required if col not in header]
    if missing:
        raise ValueError(f"Colonnes manquantes dans {path}: {missing}")
    return pd.read_excel(path, usecols=required)


def sample_budget_shares(path):
    df = load_required_columns(path)
    numeric_cols = [DAM_COL] + POST_COLS
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    valid = df[[DAM_COL] + POST_COLS].notna().all(axis=1)
    valid &= df[DAM_COL] > 0
    valid &= (df[POST_COLS] >= 0).all(axis=1)
    df = df.loc[valid].copy()

    post_totals = df[POST_COLS].sum()
    total = df[DAM_COL].sum()
    shares = post_totals / total * 100

    return pd.DataFrame({
        "poste": shares.index,
        "libelle": [POST_LABELS[col] for col in shares.index],
        "part_pct": shares.values,
        "n_menages_valides": len(df),
        "depense_totale_echantillon": total,
    })


def build_table():
    rows = []
    for survey, path in RAW_FILES.items():
        part = sample_budget_shares(path)
        part.insert(0, "enquete", survey)
        rows.append(part)

    long_df = pd.concat(rows, ignore_index=True)
    wide_df = (
        long_df.pivot(index=["poste", "libelle"], columns="enquete", values="part_pct")
        .reset_index()
    )
    wide_df["evolution_2014_moins_2007"] = wide_df["ENCDM 2014"] - wide_df["ENNVM 2007"]
    wide_df["moyenne_2007_2014"] = wide_df[["ENNVM 2007", "ENCDM 2014"]].mean(axis=1)
    wide_df = wide_df.sort_values("ENNVM 2007", ascending=True)
    return long_df, wide_df


# =====================================================
# 3. Visualisation
# =====================================================

def draw_chart(wide_df):
    plt.rcParams.update({
        "figure.dpi": 140,
        "savefig.dpi": 320,
        "font.family": "DejaVu Sans",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.spines.bottom": False,
        "axes.titleweight": "bold",
    })

    labels = wide_df["libelle"].tolist()
    y = np.arange(len(wide_df))
    bar_h = 0.34

    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    ax.barh(
        y + bar_h / 2,
        wide_df["ENCDM 2014"],
        height=bar_h,
        color=SURVEY_COLORS["ENCDM 2014"],
        label="ENCDM 2014",
    )
    ax.barh(
        y - bar_h / 2,
        wide_df["ENNVM 2007"],
        height=bar_h,
        color=SURVEY_COLORS["ENNVM 2007"],
        label="ENNVM 2007",
    )

    max_x = max(wide_df["ENNVM 2007"].max(), wide_df["ENCDM 2014"].max())
    ax.set_xlim(0, max_x + 6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.tick_params(axis="x", labelsize=10, length=0)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.grid(True, color="#E7E7E7", linewidth=0.9)
    ax.set_axisbelow(True)

    for idx, row in wide_df.iterrows():
        pos = wide_df.index.get_loc(idx)
        x_2014 = row["ENCDM 2014"]
        x_2007 = row["ENNVM 2007"]
        ax.text(x_2014 + 0.35, pos + bar_h / 2, f"{x_2014:.1f}%", va="center", fontsize=9.5)
        ax.text(x_2007 + 0.35, pos - bar_h / 2, f"{x_2007:.1f}%", va="center", fontsize=9.5)

    ax.set_xlabel("Part dans les depenses totales (%)", fontsize=11.5)
    ax.set_title(
        "Structure des depenses de consommation des menages",
        fontsize=16,
        pad=18,
    )
    ax.text(
        0,
        1.01,
        "Parts agregees non ponderees, calculees depuis la structure de l'echantillon",
        transform=ax.transAxes,
        fontsize=10.5,
        color="#555555",
    )

    legend = ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, -0.17),
        ncol=2,
        frameon=False,
        fontsize=10.5,
        handlelength=1.8,
    )
    for handle in legend.legend_handles:
        handle.set_height(8)

    ax.text(
        1,
        -0.17,
        "Source : HCP, calculs de l'auteur",
        transform=ax.transAxes,
        ha="right",
        va="center",
        fontsize=8.5,
        color="#666666",
    )

    fig.tight_layout(rect=(0.06, 0.08, 0.98, 0.96))
    fig.savefig(OUTPUT_PDF, bbox_inches="tight")
    plt.close(fig)


def main():
    long_df, wide_df = build_table()

    draw_chart(wide_df)

    print("PDF saved:", OUTPUT_PDF)
    print()
    print(wide_df.sort_values("ENNVM 2007", ascending=False).round(2).to_string(index=False))


if __name__ == "__main__":
    main()
