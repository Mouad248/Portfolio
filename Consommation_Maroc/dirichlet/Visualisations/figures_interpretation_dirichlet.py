from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = PROJECT_ROOT / "outputs" / "figures" / "interpretation_dirichlet"
OUT_DIR.mkdir(parents=True, exist_ok=True)

G_COLS = [f"w_G{i}" for i in range(1, 10)]
S_COLS = [f"w_S{i}" for i in range(1, 24)]

G_LABELS = {
    "w_G1": "Alim.",
    "w_G2": "Habill.",
    "w_G3": "Logement",
    "w_G4": "Tabac",
    "w_G5": "Equip.",
    "w_G6": "Sante",
    "w_G7": "Transport",
    "w_G8": "Comm.",
    "w_G9": "Culture/ens.",
}

S_FAMILIES = {
    "Alimentaire": [f"w_S{i}" for i in range(1, 7)],
    "Habillement": ["w_S7"],
    "Logement-energie": ["w_S8", "w_S9", "w_S11"],
    "Equipement": ["w_S10"],
    "Sante": ["w_S12", "w_S13"],
    "Transp.-comm.": ["w_S14", "w_S15", "w_S16"],
    "Culture-ens.": ["w_S17", "w_S18"],
    "Autres": ["w_S19", "w_S20", "w_S21", "w_S22", "w_S23"],
}

PALETTE = {
    "Alim.": "#2a9d8f",
    "Habill.": "#8ab17d",
    "Logement": "#457b9d",
    "Tabac": "#6d597a",
    "Equip.": "#b56576",
    "Sante": "#e76f51",
    "Transport": "#f4a261",
    "Comm.": "#5e60ce",
    "Culture/ens.": "#d4a373",
    "Alimentaire": "#2a9d8f",
    "Habillement": "#8ab17d",
    "Logement-energie": "#457b9d",
    "Equipement": "#b56576",
    "Transp.-comm.": "#f4a261",
    "Culture-ens.": "#d4a373",
    "Autres": "#6d597a",
}

NS_MAIN = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
NS_REL = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}


def setup_style():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 12,
            "axes.labelsize": 9,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.bbox": "tight",
        }
    )


def col_index(cell_ref):
    letters = "".join(ch for ch in cell_ref if ch.isalpha())
    idx = 0
    for ch in letters:
        idx = idx * 26 + ord(ch.upper()) - ord("A") + 1
    return idx - 1


def parse_scalar(value):
    if value is None:
        return ""
    value = str(value)
    if value == "":
        return ""
    try:
        number = float(value)
    except ValueError:
        return value
    if number.is_integer():
        return int(number)
    return number


def shared_strings(zf):
    try:
        xml = zf.read("xl/sharedStrings.xml")
    except KeyError:
        return []
    root = ET.fromstring(xml)
    strings = []
    for si in root.findall("m:si", NS_MAIN):
        texts = [node.text or "" for node in si.findall(".//m:t", NS_MAIN)]
        strings.append("".join(texts))
    return strings


def workbook_sheets(zf):
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels.findall("r:Relationship", NS_REL)}
    sheets = []
    for sheet in wb.findall("m:sheets/m:sheet", NS_MAIN):
        name = sheet.attrib["name"]
        rid = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
        target = rel_map[rid].replace("\\", "/").lstrip("/")
        if not target.startswith("xl/"):
            target = "xl/" + target
        sheets.append((name, target))
    return sheets


def cell_value(cell, strings):
    ctype = cell.attrib.get("t")
    if ctype == "inlineStr":
        texts = [node.text or "" for node in cell.findall(".//m:t", NS_MAIN)]
        return "".join(texts)
    value_node = cell.find("m:v", NS_MAIN)
    value = value_node.text if value_node is not None else ""
    if ctype == "s":
        return strings[int(value)] if value != "" else ""
    return parse_scalar(value)


def read_xlsx(path, sheet_name=None):
    path = PROJECT_ROOT / path if not Path(path).is_absolute() else Path(path)
    with ZipFile(path) as zf:
        strings = shared_strings(zf)
        sheets = workbook_sheets(zf)
        if sheet_name is None:
            target = sheets[0][1]
        else:
            matches = [target for name, target in sheets if name == sheet_name]
            if not matches:
                raise ValueError(f"Sheet not found in {path}: {sheet_name}")
            target = matches[0]
        root = ET.fromstring(zf.read(target))
        raw_rows = []
        for row in root.findall("m:sheetData/m:row", NS_MAIN):
            values = []
            for cell in row.findall("m:c", NS_MAIN):
                idx = col_index(cell.attrib["r"])
                while len(values) <= idx:
                    values.append("")
                values[idx] = cell_value(cell, strings)
            raw_rows.append(values)
    if not raw_rows:
        return []
    headers = [str(x) for x in raw_rows[0]]
    rows = []
    for values in raw_rows[1:]:
        padded = values + [""] * (len(headers) - len(values))
        rows.append(dict(zip(headers, padded)))
    return rows


def weighted_mean(rows, cols):
    total = sum(float(r["cluster_size"]) for r in rows)
    return {c: sum(float(r["cluster_size"]) * float(r[c]) for r in rows) / total for c in cols}


def dominant_deviation(row, gm, labels):
    deltas = {c: float(row[c]) - gm[c] for c in labels}
    col = max(deltas, key=deltas.get)
    return col, deltas[col]


def family_values(row):
    return {fam: sum(float(row[c]) for c in cols) for fam, cols in S_FAMILIES.items()}


def family_weighted_mean(rows):
    gm = weighted_mean(rows, S_COLS)
    return {fam: sum(gm[c] for c in cols) for fam, cols in S_FAMILIES.items()}


def dominant_family(row, family_global):
    vals = family_values(row)
    deltas = {fam: vals[fam] - family_global[fam] for fam in vals}
    return max(deltas, key=deltas.get)


def cluster_id(row):
    for key in ("cluster", "cluster_dmm", "cluster_dpmm_nuts"):
        if key in row and row[key] != "":
            return int(row[key])
    raise KeyError("No cluster identifier found")


def dmm_profile_path(case_key, posts, k):
    if case_key == "2007" and posts == 9:
        return Path("outputs/tables/dmm_ennvm_9") / f"ennvm_2007_dmm_profiles_K{k}.xlsx"
    if case_key == "2014" and posts == 9:
        return Path("outputs/tables/dmm_encdm_9") / f"encdm_2014_dmm_profiles_K{k}.xlsx"
    if case_key == "2007" and posts == 23:
        return Path("outputs/tables/dmm_ennvm_23") / f"ennvm_2007_23_dmm_profiles_K{k}.xlsx"
    return Path("outputs/tables/dmm_encdm_23") / f"encdm_2014_23_dmm_profiles_K{k}.xlsx"


def dpmm_diag_path(case_key, posts):
    if case_key == "2007" and posts == 9:
        return Path("outputs/analysis_dpmm_ennvm_9/ENNVM_2007_DPMM_9postes_diagnostic.xlsx")
    if case_key == "2014" and posts == 9:
        return Path("outputs/analysis_dpmm_encdm_9/ENCDM_2014_DPMM_9postes_diagnostic.xlsx")
    if case_key == "2007" and posts == 23:
        return Path("outputs/analysis_dpmm_ennvm_23/ENNVM_2007_DPMM_23postes_diagnostic.xlsx")
    return Path("outputs/analysis_dpmm_encdm_23/ENCDM_2014_DPMM_23postes_diagnostic.xlsx")


def dpmm_profile_path(case_key, posts, prior):
    if case_key == "2007" and posts == 23:
        prefix = "ennvm_2007_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"
        return Path("outputs/tables/dpmm_ennvm_23") / f"{prefix}_{prior}_profiles_full.xlsx"
    if case_key == "2014" and posts == 23:
        prefix = "encdm_2014_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain"
        return Path("outputs/tables/dpmm_encdm_23") / f"{prefix}_{prior}_profiles_full.xlsx"
    raise ValueError("Only DPMM 23 profile paths are used here.")


def add_title(fig, title, subtitle=None):
    fig.suptitle(title, x=0.02, y=0.99, ha="left", va="top", fontsize=15, fontweight="bold")
    if subtitle:
        fig.text(0.02, 0.945, subtitle, ha="left", va="top", fontsize=9, color="#4a4a4a")


def save(fig, pdf, filename):
    fig.savefig(OUT_DIR / filename)
    pdf.savefig(fig)
    plt.close(fig)


def figure_1_k_propagation():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 6.4), sharey=True, constrained_layout=True)
    add_title(
        fig,
        "Propagation des profils DMM quand K augmente",
        "Chaque bulle est un cluster DMM 9 postes ; sa taille represente son poids dans l'echantillon et sa couleur le poste le plus sur-represente.",
    )
    legend_keys = set()
    for ax, (case_key, title) in zip(axes, [("2007", "ENNVM 2007"), ("2014", "ENCDM 2014")]):
        for k in range(2, 10):
            rows = read_xlsx(dmm_profile_path(case_key, 9, k))
            gm = weighted_mean(rows, G_COLS)
            total = sum(float(r["cluster_size"]) for r in rows)
            rows = sorted(rows, key=lambda r: float(r["w_G1"]))
            for idx, row in enumerate(rows):
                col, _ = dominant_deviation(row, gm, G_COLS)
                label = G_LABELS[col]
                legend_keys.add(label)
                x = k + (idx - (len(rows) - 1) / 2) * 0.045
                y = 100 * float(row["w_G1"])
                size = 55 + 950 * float(row["cluster_size"]) / total
                ax.scatter(x, y, s=size, color=PALETTE[label], alpha=0.75, edgecolor="white", linewidth=0.8)
                if k == 6:
                    ax.text(x, y + 0.6, f"C{cluster_id(row)}", ha="center", va="bottom", fontsize=7, color="#2b2b2b")
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_xlabel("Nombre de composantes K")
        ax.set_xticks(range(2, 10))
        ax.grid(axis="y", color="#e8e8e8", linewidth=0.8)
    axes[0].set_ylabel("Part alimentaire G1 du cluster (%)")
    handles = [
        Line2D([0], [0], marker="o", linestyle="", markersize=7, markerfacecolor=PALETTE[k], markeredgecolor="white", label=k)
        for k in sorted(legend_keys)
    ]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.02))
    return fig


def heatmap(ax, data, row_labels, col_labels, title, vlim=None):
    arr = np.array(data, dtype=float)
    if vlim is None:
        vlim = max(4, np.nanmax(np.abs(arr)))
    im = ax.imshow(arr, cmap="RdBu_r", vmin=-vlim, vmax=vlim, aspect="auto")
    ax.set_title(title, loc="left", fontweight="bold")
    ax.set_xticks(range(len(col_labels)))
    ax.set_xticklabels(col_labels, rotation=35, ha="right")
    ax.set_yticks(range(len(row_labels)))
    ax.set_yticklabels(row_labels)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if abs(arr[i, j]) >= 2.0:
                ax.text(j, i, f"{arr[i, j]:+.0f}", ha="center", va="center", fontsize=7, color="#1f1f1f")
    ax.tick_params(length=0)
    return im


def figure_2_dmm9_heatmap_k6():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 6.5), constrained_layout=True)
    add_title(
        fig,
        "Empreintes budgetaires des profils DMM retenus en K=6",
        "Ecarts en points de pourcentage par rapport a la moyenne de chaque annee ; les cellules annotees sont les ecarts les plus visibles.",
    )
    ims = []
    for ax, (case_key, title) in zip(axes, [("2007", "ENNVM 2007"), ("2014", "ENCDM 2014")]):
        rows = read_xlsx(dmm_profile_path(case_key, 9, 6))
        gm = weighted_mean(rows, G_COLS)
        total = sum(float(r["cluster_size"]) for r in rows)
        data = [[100 * (float(r[c]) - gm[c]) for c in G_COLS] for r in rows]
        row_labels = [f"C{cluster_id(r)}  {100*float(r['cluster_size'])/total:.0f}%" for r in rows]
        ims.append(heatmap(ax, data, row_labels, [G_LABELS[c] for c in G_COLS], title, vlim=18))
    fig.colorbar(ims[-1], ax=axes, shrink=0.75, location="right", label="Ecart a la moyenne (points)")
    return fig


def figure_3_dmm23_family_heatmap_k7():
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 6.7), constrained_layout=True)
    add_title(
        fig,
        "Lecture fine des profils DMM 23 postes en grandes familles",
        "K=7 est utilise ici comme coupe illustrative : il montre comment les 23 postes se condensent en comportements economiques lisibles.",
    )
    family_names = list(S_FAMILIES)
    ims = []
    for ax, (case_key, title) in zip(axes, [("2007", "ENNVM 2007"), ("2014", "ENCDM 2014")]):
        rows = read_xlsx(dmm_profile_path(case_key, 23, 7))
        fg = family_weighted_mean(rows)
        total = sum(float(r["cluster_size"]) for r in rows)
        data = []
        for row in rows:
            fv = family_values(row)
            data.append([100 * (fv[f] - fg[f]) for f in family_names])
        row_labels = [f"C{cluster_id(r)}  {100*float(r['cluster_size'])/total:.0f}%" for r in rows]
        ims.append(heatmap(ax, data, row_labels, family_names, title, vlim=18))
    fig.colorbar(ims[-1], ax=axes, shrink=0.75, location="right", label="Ecart a la moyenne (points)")
    return fig


def figure_4_dpmm_prior_sensitivity():
    priors = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]
    cases = [
        ("2007", 9, "ENNVM 2007 - 9 postes"),
        ("2014", 9, "ENCDM 2014 - 9 postes"),
        ("2007", 23, "ENNVM 2007 - 23 postes"),
        ("2014", 23, "ENCDM 2014 - 23 postes"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(13.2, 8.2), sharey=True, constrained_layout=True)
    add_title(
        fig,
        "Robustesse DPMM aux priors de alpha_DP",
        "Ambiguite, taille minimale et incertitude moyenne ; les etiquettes au-dessus donnent le nombre effectif de clusters au seuil 2%.",
    )
    for ax, (case_key, posts, title) in zip(axes.ravel(), cases):
        diag = dpmm_diag_path(case_key, posts)
        p_summary = read_xlsx(diag, "01_prior_summary")
        c_summary = read_xlsx(diag, "02_cluster_summary")
        amb, min_share, uncertainty, k_eff = [], [], [], []
        for prior in priors:
            pr = [r for r in p_summary if r["prior"] == prior][0]
            cc = [r for r in c_summary if r["prior"] == prior]
            amb.append(100 * float(pr["share_ambiguous_full_lt_0_60"]))
            min_share.append(100 * min(float(r["assigned_share_full"]) for r in cc))
            uncertainty.append(100 * (1 - float(pr["mean_max_prob_full"])))
            k_eff.append(sum(float(r["posterior_weight_mean"]) >= 0.02 for r in cc))
        x = np.arange(len(priors))
        width = 0.24
        ax.bar(x - width, min_share, width, color="#2a9d8f", alpha=0.85, label="Cluster min.")
        ax.bar(x, amb, width, color="#e76f51", alpha=0.85, label="Ambigus <60%")
        ax.bar(x + width, uncertainty, width, color="#f4a261", alpha=0.85, label="1 - prob. max")
        for xi, ke in zip(x, k_eff):
            ax.text(xi, max(amb[xi], uncertainty[xi], min_share[xi]) + 1.0, f"K={ke}", ha="center", fontsize=8, fontweight="bold")
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(["G(1,1)", "G(1,2)", "G(.5,2)", "G(.25,2)"], rotation=20, ha="right")
        ax.grid(axis="y", color="#e8e8e8")
        ax.set_ylim(0, 28)
    axes[0, 0].set_ylabel("%")
    axes[1, 0].set_ylabel("%")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.01))
    return fig


def figure_5_dpmm23_socio_gradient():
    cases = [
        ("2007", "ENNVM 2007", "gamma_0p25_2"),
        ("2014", "ENCDM 2014", "gamma_1_1"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 6.4), sharey=False, constrained_layout=True)
    add_title(
        fig,
        "Position socio-economique des profils DPMM 23 postes",
        "Axe horizontal : ecart de DAM moyenne du cluster ; axe vertical : part rurale. La taille represente le poids du cluster.",
    )
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
            ax.scatter(x, y, s=70 + 28 * share, color=PALETTE[fam], alpha=0.82, edgecolor="white", linewidth=0.9)
            ax.text(x, y, f"C{cluster}", ha="center", va="center", fontsize=8, fontweight="bold", color="#202020")
        ax.axvline(0, color="#888888", lw=1, ls="--")
        if rural_global is not None:
            ax.axhline(rural_global, color="#888888", lw=1, ls="--")
            ax.text(ax.get_xlim()[0], rural_global + 1, "moy. rurale", fontsize=7, color="#666666")
        ax.set_title(f"{title} ({prior})", loc="left", fontweight="bold")
        ax.set_xlabel("Ecart de DAM moyenne vs moyenne globale (%)")
        ax.set_ylabel("Part rurale du cluster (%)")
        ax.grid(color="#e8e8e8")
    handles = [
        Line2D([0], [0], marker="o", linestyle="", markersize=7, markerfacecolor=PALETTE[f], markeredgecolor="white", label=f)
        for f in sorted(used_families)
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.02))
    return fig


def main():
    setup_style()
    combined = OUT_DIR / "figures_interpretation_dirichlet_2007_2014.pdf"
    figures = [
        (figure_1_k_propagation, "fig_01_propagation_K_DMM9.pdf"),
        (figure_2_dmm9_heatmap_k6, "fig_02_profils_DMM9_K6.pdf"),
        (figure_3_dmm23_family_heatmap_k7, "fig_03_familles_DMM23_K7.pdf"),
        (figure_4_dpmm_prior_sensitivity, "fig_04_sensibilite_priors_DPMM.pdf"),
        (figure_5_dpmm23_socio_gradient, "fig_05_gradient_socioeco_DPMM23.pdf"),
    ]
    with PdfPages(combined) as pdf:
        for maker, filename in figures:
            fig = maker()
            save(fig, pdf, filename)
    print(combined)
    for _, filename in figures:
        print(OUT_DIR / filename)


if __name__ == "__main__":
    main()
