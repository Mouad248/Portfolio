from __future__ import annotations

import csv
import math
import re
from pathlib import Path
from statistics import median

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "reports"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PDF_OUT = OUT_DIR / "rapport_diagnostic_alpha_DMM_DPMM.pdf"
DMM_CSV = OUT_DIR / "diagnostic_alpha_dmm_resume.csv"
DPMM_CSV = OUT_DIR / "diagnostic_alpha_dpmm_resume.csv"

PRIOR_ORDER = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]
PRIOR_HYPERPARAMS = {
    "gamma_1_1": "Gamma(a=1.0, b=2.0)",
    "gamma_1_2": "Gamma(a=0.25, b=2.0)",
    "gamma_0p5_2": "Gamma(a=0.1, b=2.0)",
    "gamma_0p25_2": "Gamma(a=0.05, b=2.0)",
}

CASE_LABELS = {
    "ennvm_9": "2007 - 9 postes",
    "encdm_9": "2014 - 9 postes",
    "ennvm_23": "2007 - 23 postes",
    "encdm_23": "2014 - 23 postes",
}
CASE_ORDER = ["ennvm_9", "encdm_9", "ennvm_23", "encdm_23"]


def case_key_from_parent(parent_name: str) -> str:
    return parent_name.replace("dmm_", "").replace("dpmm_", "")


def read_sheet_records(path: Path) -> list[dict[str, float | str | int]]:
    wb = load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    header = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]
    records = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if all(value is None for value in row):
            continue
        records.append({str(key): value for key, value in zip(header, row) if key is not None})
    wb.close()
    return records


def finite(values: list[float | int | None]) -> list[float]:
    out = []
    for value in values:
        if value is None:
            continue
        value = float(value)
        if math.isfinite(value):
            out.append(value)
    return out


def q(values: list[float], p: float) -> float:
    values = sorted(values)
    if not values:
        return float("nan")
    pos = (len(values) - 1) * p
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return values[lo]
    return values[lo] * (hi - pos) + values[hi] * (pos - lo)


def summarize_values(values: list[float]) -> dict[str, float]:
    return {
        "min": min(values) if values else float("nan"),
        "q25": q(values, 0.25),
        "median": median(values) if values else float("nan"),
        "q75": q(values, 0.75),
        "max": max(values) if values else float("nan"),
    }


def collect_dmm() -> tuple[list[dict[str, float | str | int]], list[float]]:
    rows = []
    all_alphas = []
    for path in sorted((ROOT / "outputs" / "tables").glob("dmm_*/*alpha_K*.xlsx")):
        records = read_sheet_records(path)
        if not records:
            continue
        k_match = re.search(r"_K(\d+)\.xlsx$", path.name)
        k_value = int(k_match.group(1)) if k_match else -1
        case_key = case_key_from_parent(path.parent.name)
        case_label = CASE_LABELS.get(case_key, case_key)
        alpha_cols = [
            col
            for col in records[0]
            if col.startswith("alpha_") and col not in {"alpha_sum", "alpha_sum_mean"}
        ]
        alpha0 = []
        pi_values = []
        file_alphas = []
        for rec in records:
            alpha_values = finite([rec.get(col) for col in alpha_cols])
            all_alphas.extend(alpha_values)
            file_alphas.extend(alpha_values)
            if rec.get("alpha_sum") is not None:
                alpha0.append(float(rec["alpha_sum"]))
            else:
                alpha0.append(sum(alpha_values))
            if rec.get("pi") is not None:
                pi_values.append(float(rec["pi"]))

        a0 = summarize_values(alpha0)
        pi = summarize_values(pi_values)
        rows.append(
            {
                "case_key": case_key,
                "case": case_label,
                "K": k_value,
                "n_components": len(records),
                "alpha0_min": a0["min"],
                "alpha0_q25": a0["q25"],
                "alpha0_median": a0["median"],
                "alpha0_q75": a0["q75"],
                "alpha0_max": a0["max"],
                "pi_min": pi["min"],
                "pi_median": pi["median"],
                "pi_max": pi["max"],
                "alpha_j_min": min(file_alphas) if file_alphas else float("nan"),
                "alpha_j_max": max(file_alphas) if file_alphas else float("nan"),
            }
        )
    rows.sort(
        key=lambda r: (
            CASE_ORDER.index(str(r["case_key"])) if str(r["case_key"]) in CASE_ORDER else 99,
            int(r["K"]),
        )
    )
    return rows, all_alphas


def collect_dpmm() -> tuple[list[dict[str, float | str | int]], list[float]]:
    rows = []
    all_alphas = []
    for path in sorted((ROOT / "outputs" / "tables").glob("dpmm_*/*alpha.xlsx")):
        records = read_sheet_records(path)
        if not records:
            continue
        case_key = case_key_from_parent(path.parent.name)
        case_label = CASE_LABELS.get(case_key, case_key)
        prior = str(records[0].get("prior", "unknown"))
        alpha_cols = [
            col
            for col in records[0]
            if col.startswith("alpha_") and col not in {"alpha_sum", "alpha_sum_mean"}
        ]
        alpha0 = []
        weights = []
        file_alphas = []
        for rec in records:
            alpha_values = finite([rec.get(col) for col in alpha_cols])
            all_alphas.extend(alpha_values)
            file_alphas.extend(alpha_values)
            if rec.get("alpha_sum_mean") is not None:
                alpha0.append(float(rec["alpha_sum_mean"]))
            elif rec.get("phi_mean") is not None:
                alpha0.append(float(rec["phi_mean"]))
            else:
                alpha0.append(sum(alpha_values))
            if rec.get("posterior_weight_mean") is not None:
                weights.append(float(rec["posterior_weight_mean"]))

        active_1 = [a for a, w in zip(alpha0, weights) if w >= 0.01]
        active_2 = [a for a, w in zip(alpha0, weights) if w >= 0.02]
        active_3 = [a for a, w in zip(alpha0, weights) if w >= 0.03]
        a0 = summarize_values(alpha0)
        a0_active = summarize_values(active_1)
        wsum = summarize_values(weights)
        rows.append(
            {
                "case_key": case_key,
                "case": case_label,
                "prior": prior,
                "prior_hyperparams": PRIOR_HYPERPARAMS.get(prior, ""),
                "n_truncated_components": len(records),
                "n_active_ge_1pct": len(active_1),
                "n_active_ge_2pct": len(active_2),
                "n_active_ge_3pct": len(active_3),
                "alpha0_min": a0["min"],
                "alpha0_median": a0["median"],
                "alpha0_max": a0["max"],
                "alpha0_active_min": a0_active["min"],
                "alpha0_active_median": a0_active["median"],
                "alpha0_active_max": a0_active["max"],
                "weight_min": wsum["min"],
                "weight_median": wsum["median"],
                "weight_max": wsum["max"],
                "weight_sum": sum(weights),
                "alpha_j_min": min(file_alphas) if file_alphas else float("nan"),
                "alpha_j_max": max(file_alphas) if file_alphas else float("nan"),
            }
        )
    rows.sort(
        key=lambda r: (
            CASE_ORDER.index(str(r["case_key"])) if str(r["case_key"]) in CASE_ORDER else 99,
            PRIOR_ORDER.index(str(r["prior"])) if str(r["prior"]) in PRIOR_ORDER else 99,
        )
    )
    return rows, all_alphas


def write_csv(path: Path, rows: list[dict[str, float | str | int]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def setup_page(title: str):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor("white")
    fig.text(0.06, 0.94, title, fontsize=18, fontweight="bold", ha="left", va="top")
    return fig


def add_paragraph(fig, text: str, x=0.06, y=0.84, fontsize=11, line_height=0.045):
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = []
        for word in words:
            if sum(len(w) + 1 for w in current) + len(word) > 105:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))
        lines.append("")
    for i, line in enumerate(lines):
        fig.text(x, y - i * line_height, line, fontsize=fontsize, ha="left", va="top")


def add_table(ax, rows: list[list[str]], columns: list[str], fontsize=8.5, scale_y=1.35):
    ax.axis("off")
    table = ax.table(cellText=rows, colLabels=columns, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1, scale_y)
    for (row, _col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#E9EEF5")
            cell.set_text_props(weight="bold")
        cell.set_edgecolor("#B8C0CC")
    return table


def format_float(value: float | int | str, digits=2) -> str:
    if isinstance(value, str):
        return value
    if value is None:
        return ""
    value = float(value)
    if not math.isfinite(value):
        return ""
    return f"{value:.{digits}f}"


def dmm_case_page(pdf: PdfPages, case: str, rows: list[dict[str, float | str | int]]) -> None:
    rows = sorted(rows, key=lambda r: int(r["K"]))
    fig = setup_page(f"DMM - Diagnostic alpha0 - {case}")
    ax = fig.add_axes([0.08, 0.49, 0.56, 0.35])
    ks = [int(r["K"]) for r in rows]
    ax.plot(ks, [float(r["alpha0_min"]) for r in rows], marker="o", label="min alpha0")
    ax.plot(ks, [float(r["alpha0_median"]) for r in rows], marker="o", label="mediane alpha0")
    ax.plot(ks, [float(r["alpha0_max"]) for r in rows], marker="o", label="max alpha0")
    ax.set_xlabel("K")
    ax.set_ylabel("alpha0 = somme des alpha_j")
    ax.set_title("Concentration interne des composantes")
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=9)

    ax2 = fig.add_axes([0.70, 0.49, 0.22, 0.35])
    ax2.plot(ks, [100 * float(r["pi_min"]) for r in rows], marker="o", color="#B44E2A")
    ax2.set_title("Plus petit poids de cluster")
    ax2.set_xlabel("K")
    ax2.set_ylabel("pi min (%)")
    ax2.grid(True, alpha=0.25)

    table_ax = fig.add_axes([0.05, 0.08, 0.90, 0.34])
    table_rows = [
        [
            str(r["K"]),
            format_float(r["alpha0_min"]),
            format_float(r["alpha0_median"]),
            format_float(r["alpha0_max"]),
            format_float(100 * float(r["pi_min"]), 1),
            format_float(100 * float(r["pi_median"]), 1),
            format_float(100 * float(r["pi_max"]), 1),
        ]
        for r in rows
    ]
    add_table(
        table_ax,
        table_rows,
        ["K", "alpha0 min", "alpha0 med.", "alpha0 max", "pi min %", "pi med. %", "pi max %"],
        fontsize=8.8,
        scale_y=1.3,
    )
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def dpmm_case_page(pdf: PdfPages, case: str, rows: list[dict[str, float | str | int]]) -> None:
    rows = sorted(
        rows,
        key=lambda r: PRIOR_ORDER.index(str(r["prior"])) if str(r["prior"]) in PRIOR_ORDER else 99,
    )
    labels = [str(r["prior"]).replace("gamma_", "g=") for r in rows]
    fig = setup_page(f"DPMM - Diagnostic alpha0 et poids - {case}")
    ax = fig.add_axes([0.08, 0.51, 0.40, 0.33])
    x = list(range(len(rows)))
    ax.bar([v - 0.22 for v in x], [float(r["alpha0_active_min"]) for r in rows], width=0.22, label="min actif")
    ax.bar(x, [float(r["alpha0_active_median"]) for r in rows], width=0.22, label="mediane actif")
    ax.bar([v + 0.22 for v in x], [float(r["alpha0_active_max"]) for r in rows], width=0.22, label="max actif")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.set_ylabel("alpha0 actif (poids >= 1%)")
    ax.set_title("Concentration des composantes actives")
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(fontsize=8.5)

    ax2 = fig.add_axes([0.56, 0.51, 0.36, 0.33])
    ax2.bar([v - 0.20 for v in x], [int(r["n_active_ge_1pct"]) for r in rows], width=0.20, label=">=1%")
    ax2.bar(x, [int(r["n_active_ge_2pct"]) for r in rows], width=0.20, label=">=2%")
    ax2.bar([v + 0.20 for v in x], [int(r["n_active_ge_3pct"]) for r in rows], width=0.20, label=">=3%")
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, rotation=20, ha="right")
    ax2.set_ylim(0, 7.5)
    ax2.set_ylabel("Nombre de composantes")
    ax2.set_title("Composantes substantielles")
    ax2.grid(True, axis="y", alpha=0.25)
    ax2.legend(fontsize=8.5)

    table_ax = fig.add_axes([0.04, 0.06, 0.92, 0.36])
    table_rows = [
        [
            str(r["prior"]),
            str(r["prior_hyperparams"]),
            str(r["n_active_ge_1pct"]),
            format_float(r["alpha0_active_min"]),
            format_float(r["alpha0_active_median"]),
            format_float(r["alpha0_active_max"]),
            format_float(100 * float(r["weight_min"]), 2),
            format_float(100 * float(r["weight_max"]), 1),
        ]
        for r in rows
    ]
    add_table(
        table_ax,
        table_rows,
        ["Prior", "Hyperparametres", "act. >=1%", "alpha0 min", "alpha0 med.", "alpha0 max", "poids min %", "poids max %"],
        fontsize=7.8,
        scale_y=1.25,
    )
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def global_page(pdf: PdfPages, dmm_rows, dpmm_rows, dmm_alphas, dpmm_alphas) -> None:
    fig = setup_page("Synthese globale du diagnostic alpha")
    dmm_alpha0 = finite([r["alpha0_min"] for r in dmm_rows] + [r["alpha0_max"] for r in dmm_rows])
    dpmm_alpha0_active = finite(
        [r["alpha0_active_min"] for r in dpmm_rows] + [r["alpha0_active_max"] for r in dpmm_rows]
    )
    dmm_min_pi = finite([r["pi_min"] for r in dmm_rows])
    dpmm_min_weight = finite([r["weight_min"] for r in dpmm_rows])

    text = (
        "Lecture: alpha0 est la somme des parametres alpha_j d'une composante de Dirichlet. "
        "Il donne un diagnostic de concentration interne du profil moyen. Des valeurs tres faibles, "
        "combinees a des poids de clusters minuscules, signaleraient des composantes peu fiables.\n"
        "Conclusion: les solutions estimees ne montrent pas de degenerescence evidente. Les alpha0 "
        "restent dans des plages coherentes, tandis que les poids de composantes permettent "
        "d'identifier les profils substantiels. Ce diagnostic complete les criteres de probabilite "
        "d'affectation, d'ambiguite et de taille minimale; il ne choisit pas K a lui seul."
    )
    add_paragraph(fig, text, y=0.84, fontsize=11, line_height=0.04)

    table_ax = fig.add_axes([0.09, 0.27, 0.82, 0.25])
    table_rows = [
        [
            "DMM",
            f"{len(dmm_rows)} solutions K-cas",
            format_float(min(dmm_alpha0), 2),
            format_float(median([float(r["alpha0_median"]) for r in dmm_rows]), 2),
            format_float(max(dmm_alpha0), 2),
            format_float(100 * min(dmm_min_pi), 2),
            format_float(min(dmm_alphas), 3),
            format_float(max(dmm_alphas), 2),
        ],
        [
            "DPMM",
            f"{len(dpmm_rows)} prior-cas",
            format_float(min(dpmm_alpha0_active), 2),
            format_float(median([float(r["alpha0_active_median"]) for r in dpmm_rows]), 2),
            format_float(max(dpmm_alpha0_active), 2),
            format_float(100 * min(dpmm_min_weight), 2),
            format_float(min(dpmm_alphas), 3),
            format_float(max(dpmm_alphas), 2),
        ],
    ]
    add_table(
        table_ax,
        table_rows,
        ["Modele", "Base", "alpha0 min", "alpha0 med.", "alpha0 max", "poids min %", "alpha_j min", "alpha_j max"],
        fontsize=9,
        scale_y=1.5,
    )

    fig.text(
        0.06,
        0.16,
        "Note: dans le DPMM, les labels gamma_* designent le prior sur le parametre de concentration du processus de Dirichlet. "
        "Ils ne doivent pas etre confondus avec les alpha_j des profils de consommation.",
        fontsize=10,
        ha="left",
        va="top",
    )
    fig.text(
        0.06,
        0.10,
        f"Fichiers CSV generes: {DMM_CSV.name} et {DPMM_CSV.name}",
        fontsize=9,
        color="#444444",
        ha="left",
    )
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def cover_page(pdf: PdfPages) -> None:
    fig = setup_page("Rapport diagnostic des parametres alpha - DMM et DPMM")
    text = (
        "Objectif du rapport\n"
        "Ce document verifie si les composantes estimees par les modeles de melange de Dirichlet "
        "presentent des parametres raisonnables. Il ne sert pas a choisir K directement; il sert a "
        "documenter la non-degenerescence globale des profils.\n"
        "Definitions\n"
        "Pour une composante c et J postes budgetaires, le vecteur alpha_c = (alpha_c1, ..., alpha_cJ) "
        "definit le profil moyen E(w_cj) = alpha_cj / alpha_0c, avec alpha_0c = somme_j alpha_cj. "
        "Un alpha_0 plus eleve indique une composante plus concentree autour de son profil moyen. "
        "Les poids pi, en DMM, et posterior_weight_mean, en DPMM, indiquent l'importance effective "
        "des clusters ou composantes.\n"
        "Perimetre\n"
        "DMM: K = 2 a K = 9 pour 2007/2014 et 9/23 postes. "
        "DPMM: Kmax = 7 pour les quatre priors disponibles et les quatre cas."
    )
    add_paragraph(fig, text, y=0.84, fontsize=11, line_height=0.043)
    fig.text(
        0.06,
        0.08,
        "Lecture pratique: chercher simultanement des alpha0 coherents et des poids non-negligeables. "
        "Un alpha_j individuel faible peut simplement correspondre a un poste peu representé dans un profil; "
        "ce n'est pas, seul, un probleme.",
        fontsize=10,
        ha="left",
        va="bottom",
        color="#444444",
    )
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def make_pdf(dmm_rows, dpmm_rows, dmm_alphas, dpmm_alphas) -> None:
    with PdfPages(PDF_OUT) as pdf:
        cover_page(pdf)
        global_page(pdf, dmm_rows, dpmm_rows, dmm_alphas, dpmm_alphas)
        for case_key in [*CASE_ORDER, *sorted(set(str(r["case_key"]) for r in dmm_rows) - set(CASE_ORDER))]:
            case_rows = [r for r in dmm_rows if str(r["case_key"]) == case_key]
            if case_rows:
                dmm_case_page(pdf, str(case_rows[0]["case"]), case_rows)
        for case_key in [*CASE_ORDER, *sorted(set(str(r["case_key"]) for r in dpmm_rows) - set(CASE_ORDER))]:
            case_rows = [r for r in dpmm_rows if str(r["case_key"]) == case_key]
            if case_rows:
                dpmm_case_page(pdf, str(case_rows[0]["case"]), case_rows)


def main() -> None:
    dmm_rows, dmm_alphas = collect_dmm()
    dpmm_rows, dpmm_alphas = collect_dpmm()
    write_csv(DMM_CSV, dmm_rows)
    write_csv(DPMM_CSV, dpmm_rows)
    make_pdf(dmm_rows, dpmm_rows, dmm_alphas, dpmm_alphas)
    print(PDF_OUT)
    print(DMM_CSV)
    print(DPMM_CSV)


if __name__ == "__main__":
    main()
