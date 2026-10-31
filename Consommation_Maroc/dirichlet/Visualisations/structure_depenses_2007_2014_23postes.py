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

OUTPUT_PDF = OUTPUT_DIR / "structure_depenses_2007_2014_23postes_echantillon.pdf"

DAM_COL = "DAM"

# Mapping identique aux scripts matrix_creation/matrice_*_23.py.
S_MAPPING_ENNVM = {
    "S1":  ["DAM_G01"],
    "S2":  ["DAM_G02", "DAM_G04", "DAM_G05"],
    "S3":  ["DAM_G06", "DAM_G07", "DAM_G08"],
    "S4":  ["DAM_G09", "DAM_G10"],
    "S5":  ["DAM_G13", "DAM_G14"],
    "S6":  ["DAM_G03", "DAM_G11", "DAM_G12", "DAM_G15", "DAM_G17", "DAM_G18"],
    "S7":  ["DAM_G21", "DAM_G22", "DAM_G23", "DAM_G24", "DAM_G25", "DAM_G26", "DAM_G27", "DAM_G28"],
    "S8":  ["DAM_G31"],
    "S9":  ["DAM_G32", "DAM_G34"],
    "S10": ["DAM_G41", "DAM_G42", "DAM_G43", "DAM_G44", "DAM_G45", "DAM_G46", "DAM_G47"],
    "S11": ["DAM_G33"],
    "S12": ["DAM_G51"],
    "S13": ["DAM_G52", "DAM_G53"],
    "S14": ["DAM_G61"],
    "S15": ["DAM_G62"],
    "S16": ["DAM_G63"],
    "S17": ["DAM_G71", "DAM_G72", "DAM_G73", "DAM_G74"],
    "S18": ["DAM_G75", "DAM_G76"],
    "S19": ["DAM_G81", "DAM_G82", "DAM_G83", "DAM_G84"],
    "S20": ["DAM_G87", "DAM_G88"],
    "S21": ["DAM_G85", "DAM_G86"],
    "S22": ["DAM_G89"],
    "S23": ["DAM_G91", "DAM_G92", "DAM_G93", "DAM_G94"],
}

S_MAPPING_ENCDM = {
    **S_MAPPING_ENNVM,
    "S18": ["DAM_G75", "DAM_G76", "DAM_G77"],
}

S_MAPPINGS = {
    "ENNVM 2007": S_MAPPING_ENNVM,
    "ENCDM 2014": S_MAPPING_ENCDM,
}

S_LABELS = {
    s: f"{s} ({', '.join(cols)})"
    for s, cols in S_MAPPING_ENCDM.items()
}

SURVEY_COLORS = {
    "ENNVM 2007": "#176D35",
    "ENCDM 2014": "#E95A0C",
}


# =====================================================
# 2. Calcul des parts budgetaires dans l'echantillon
# =====================================================

def required_columns(mapping):
    cols = [DAM_COL]
    for group_cols in mapping.values():
        cols.extend(group_cols)
    return list(dict.fromkeys(cols))


def load_required_columns(path, mapping):
    required = required_columns(mapping)
    header = pd.read_excel(path, nrows=0).columns.tolist()
    missing = [col for col in required if col not in header]
    if missing:
        raise ValueError(f"Colonnes manquantes dans {path}: {missing}")
    return pd.read_excel(path, usecols=required)


def sample_budget_shares(survey, path):
    mapping = S_MAPPINGS[survey]
    df = load_required_columns(path, mapping)
    cols = required_columns(mapping)

    for col in cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    valid = df[DAM_COL].notna() & (df[DAM_COL] > 0)
    df = df.loc[valid].copy()

    for col in cols:
        if col != DAM_COL:
            df[col] = df[col].fillna(0).clip(lower=0)

    total = df[DAM_COL].sum()
    rows = []
    for s, group_cols in mapping.items():
        group_total = df[group_cols].sum(axis=1).sum()
        rows.append({
            "poste": s,
            "libelle": S_LABELS[s],
            "part_pct": group_total / total * 100,
            "n_menages_valides": len(df),
            "depense_totale_echantillon": total,
        })

    return pd.DataFrame(rows)


def build_table():
    rows = []
    for survey, path in RAW_FILES.items():
        part = sample_budget_shares(survey, path)
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

    fig, ax = plt.subplots(figsize=(14.5, 11.5))
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
    ax.set_xlim(0, max_x + 3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.7)
    ax.tick_params(axis="x", labelsize=9.5, length=0)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.grid(True, color="#E7E7E7", linewidth=0.9)
    ax.set_axisbelow(True)

    for idx, row in wide_df.iterrows():
        pos = wide_df.index.get_loc(idx)
        x_2014 = row["ENCDM 2014"]
        x_2007 = row["ENNVM 2007"]
        ax.text(x_2014 + 0.12, pos + bar_h / 2, f"{x_2014:.1f}%", va="center", fontsize=8.2)
        ax.text(x_2007 + 0.12, pos - bar_h / 2, f"{x_2007:.1f}%", va="center", fontsize=8.2)

    ax.set_xlabel("Part dans les depenses totales (%)", fontsize=11)
    ax.set_title(
        "Structure des depenses de consommation des menages - 23 postes",
        fontsize=16,
        pad=18,
    )
    ax.text(
        0,
        1.01,
        "Parts agregees non ponderees, calculees depuis la structure de l'echantillon",
        transform=ax.transAxes,
        fontsize=10,
        color="#555555",
    )

    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, -0.08),
        ncol=2,
        frameon=False,
        fontsize=10,
        handlelength=1.8,
    )

    ax.text(
        1,
        -0.08,
        "Source : HCP, calculs de l'auteur",
        transform=ax.transAxes,
        ha="right",
        va="center",
        fontsize=8.3,
        color="#666666",
    )

    fig.tight_layout(rect=(0.17, 0.05, 0.98, 0.97))
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
