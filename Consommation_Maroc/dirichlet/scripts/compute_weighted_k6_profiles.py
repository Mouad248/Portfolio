from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables" / "profils_ponderees_K6"


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

S_FAMILIES = {
    "Alimentaire": [f"w_S{i}" for i in range(1, 7)],
    "Habillement": ["w_S7"],
    "Logement": ["w_S8", "w_S9", "w_S11"],
    "Equipement": ["w_S10"],
    "Sante": ["w_S12", "w_S13"],
    "Transport-comm.": ["w_S14", "w_S15", "w_S16"],
    "Culture-ens.": ["w_S17", "w_S18"],
    "Autres": ["w_S19", "w_S20", "w_S21", "w_S22", "w_S23"],
}

S_FAMILY_BY_COL = {col: family for family, cols in S_FAMILIES.items() for col in cols}


CASES = [
    {
        "label": "2007_9postes",
        "path": ROOT / "outputs" / "tables" / "dmm_ennvm_9" / "ennvm_2007_dmm_membership_K6.xlsx",
        "share_cols": [f"w_G{i}" for i in range(1, 10)],
    },
    {
        "label": "2014_9postes",
        "path": ROOT / "outputs" / "tables" / "dmm_encdm_9" / "encdm_2014_dmm_membership_K6.xlsx",
        "share_cols": [f"w_G{i}" for i in range(1, 10)],
    },
    {
        "label": "2007_23postes",
        "path": ROOT / "outputs" / "tables" / "dmm_ennvm_23" / "ennvm_2007_23_dmm_membership_K6.xlsx",
        "share_cols": [f"w_S{i}" for i in range(1, 24)],
    },
    {
        "label": "2014_23postes",
        "path": ROOT / "outputs" / "tables" / "dmm_encdm_23" / "encdm_2014_23_dmm_membership_K6.xlsx",
        "share_cols": [f"w_S{i}" for i in range(1, 24)],
    },
]


def weighted_mean(group: pd.DataFrame, value_col: str, weight_col: str = "coef_menage") -> float:
    weights = group[weight_col].astype(float)
    values = group[value_col].astype(float)
    return float((values * weights).sum() / weights.sum())


def compute_case(case: dict[str, object]) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_excel(case["path"])
    share_cols = list(case["share_cols"])

    rows_prop = []
    rows_pct = []
    total_weight = float(df["coef_menage"].sum())

    for cluster, group in df.groupby("cluster_dmm", sort=True):
        weight_sum = float(group["coef_menage"].sum())
        base = {
            "cluster_dmm": int(cluster),
            "n_menages": int(len(group)),
            "poids_total": weight_sum,
            "part_cluster_ponderee_pct": 100 * weight_sum / total_weight,
            "DAM_moyenne_ponderee": weighted_mean(group, "DAM"),
        }
        means_prop = {col: weighted_mean(group, col) for col in share_cols}
        means_pct = {col: 100 * val for col, val in means_prop.items()}

        rows_prop.append({**base, **means_prop})
        rows_pct.append({**base, **means_pct})

    prop = pd.DataFrame(rows_prop)
    pct = pd.DataFrame(rows_pct)

    numeric_cols = [col for col in prop.columns if col not in {"cluster_dmm", "n_menages"}]
    prop[numeric_cols] = prop[numeric_cols].round(6)
    pct[numeric_cols] = pct[numeric_cols].round(3)
    pct["poids_total"] = pct["poids_total"].round(0).astype("int64")
    prop["poids_total"] = prop["poids_total"].round(0).astype("int64")

    return prop, pct


def to_long(case: dict[str, object], wide: pd.DataFrame, value_name: str) -> pd.DataFrame:
    label = str(case["label"])
    year, posts = label.split("_")
    share_cols = list(case["share_cols"])
    id_cols = [
        "cluster_dmm",
        "n_menages",
        "poids_total",
        "part_cluster_ponderee_pct",
        "DAM_moyenne_ponderee",
    ]
    long = wide.melt(
        id_vars=id_cols,
        value_vars=share_cols,
        var_name="poste",
        value_name=value_name,
    )
    long.insert(0, "annee", int(year))
    long.insert(1, "n_postes", int(posts.replace("postes", "")))
    long["poste_libelle"] = long["poste"].map(G_LABELS).fillna(long["poste"])
    long["famille_budgetaire"] = long["poste"].map(S_FAMILY_BY_COL).fillna(long["poste_libelle"])
    return long


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    workbook = OUT / "profils_dmm_K6_moyennes_ponderees_coef_menage.xlsx"
    all_long_prop = []
    all_long_pct = []

    with pd.ExcelWriter(workbook, engine="openpyxl") as writer:
        for case in CASES:
            prop, pct = compute_case(case)
            label = str(case["label"])
            prop.to_excel(writer, sheet_name=f"{label}_prop", index=False)
            pct.to_excel(writer, sheet_name=f"{label}_pct", index=False)
            pct.to_csv(OUT / f"profils_dmm_K6_ponderees_{label}_pct.csv", index=False, encoding="utf-8-sig")
            prop.to_csv(OUT / f"profils_dmm_K6_ponderees_{label}_prop.csv", index=False, encoding="utf-8-sig")
            all_long_prop.append(to_long(case, prop, "moyenne_ponderee"))
            all_long_pct.append(to_long(case, pct, "moyenne_ponderee_pct"))

        long_prop = pd.concat(all_long_prop, ignore_index=True)
        long_pct = pd.concat(all_long_pct, ignore_index=True)
        long_prop.to_excel(writer, sheet_name="tous_cas_long_prop", index=False)
        long_pct.to_excel(writer, sheet_name="tous_cas_long_pct", index=False)

    long_prop.to_csv(OUT / "profils_dmm_K6_ponderees_tous_cas_long_prop.csv", index=False, encoding="utf-8-sig")
    long_pct.to_csv(OUT / "profils_dmm_K6_ponderees_tous_cas_long_pct.csv", index=False, encoding="utf-8-sig")

    print(workbook)


if __name__ == "__main__":
    main()
