from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "rapport_resultats_DPMM_23postes_2007_2014.md"
DOCX_PATH = ROOT / "rapport_resultats_DPMM_23postes_2007_2014.docx"

SHARE_COLS = [f"w_S{i}" for i in range(1, 24)]

S_CODES = {
    "S1": "DAM_G01",
    "S2": "DAM_G02, DAM_G04, DAM_G05",
    "S3": "DAM_G06, DAM_G07, DAM_G08",
    "S4": "DAM_G09, DAM_G10",
    "S5": "DAM_G13, DAM_G14",
    "S6": "DAM_G03, DAM_G11, DAM_G12, DAM_G15, DAM_G17, DAM_G18",
    "S7": "DAM_G21 a DAM_G28",
    "S8": "DAM_G31",
    "S9": "DAM_G32, DAM_G34",
    "S10": "DAM_G41 a DAM_G47",
    "S11": "DAM_G33",
    "S12": "DAM_G51",
    "S13": "DAM_G52, DAM_G53",
    "S14": "DAM_G61",
    "S15": "DAM_G62",
    "S16": "DAM_G63",
    "S17": "DAM_G71 a DAM_G74",
    "S18": "DAM_G75, DAM_G76; + DAM_G77 dans ENCDM",
    "S19": "DAM_G81 a DAM_G84",
    "S20": "DAM_G87, DAM_G88",
    "S21": "DAM_G85, DAM_G86",
    "S22": "DAM_G89",
    "S23": "DAM_G91 a DAM_G94",
}

S_LABELS = {
    "w_S1": "S1 alimentaire 01",
    "w_S2": "S2 alimentaire 02/04/05",
    "w_S3": "S3 alimentaire 06/07/08",
    "w_S4": "S4 alimentaire 09/10",
    "w_S5": "S5 alimentaire 13/14",
    "w_S6": "S6 alimentaire mixte",
    "w_S7": "S7 habillement-chaussures",
    "w_S8": "S8 logement poste 31",
    "w_S9": "S9 logement/energie 32/34",
    "w_S10": "S10 ameublement-equipement",
    "w_S11": "S11 logement poste 33",
    "w_S12": "S12 sante 51",
    "w_S13": "S13 sante 52/53",
    "w_S14": "S14 transport 61",
    "w_S15": "S15 transport 62",
    "w_S16": "S16 transport/communication 63",
    "w_S17": "S17 loisirs/culture 71/74",
    "w_S18": "S18 culture/enseignement 75/76/77",
    "w_S19": "S19 autres 81/84",
    "w_S20": "S20 autres 87/88",
    "w_S21": "S21 autres 85/86",
    "w_S22": "S22 autres 89",
    "w_S23": "S23 autres 91/94",
}

FAMILIES = {
    "Alimentaire": [f"w_S{i}" for i in range(1, 7)],
    "Habillement": ["w_S7"],
    "Logement-energie": ["w_S8", "w_S9", "w_S11"],
    "Ameublement-equipement": ["w_S10"],
    "Sante": ["w_S12", "w_S13"],
    "Transport-communication": ["w_S14", "w_S15", "w_S16"],
    "Culture-enseignement": ["w_S17", "w_S18"],
    "Autres depenses": ["w_S19", "w_S20", "w_S21", "w_S22", "w_S23"],
}

PRIORS = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]

CASES = {
    "ENNVM 2007": {
        "prefix": "ennvm_2007_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain",
        "tables": Path("outputs/tables/dpmm_ennvm_23"),
        "diag": Path("outputs/analysis_dpmm_ennvm_23/ENNVM_2007_DPMM_23postes_diagnostic.xlsx"),
        "preferred": "gamma_0p25_2",
    },
    "ENCDM 2014": {
        "prefix": "encdm_2014_dpmm_nuts_full_23_Kmax7_orderedS1_singlechain",
        "tables": Path("outputs/tables/dpmm_encdm_23"),
        "diag": Path("outputs/analysis_dpmm_encdm_23/ENCDM_2014_DPMM_23postes_diagnostic.xlsx"),
        "preferred": "gamma_1_1",
    },
}

NS_MAIN = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
NS_REL = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}


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


def read_xlsx_sheet(path, sheet_name=None):
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
        rows = []
        width = 0
        for row in root.findall("m:sheetData/m:row", NS_MAIN):
            values = []
            for cell in row.findall("m:c", NS_MAIN):
                idx = col_index(cell.attrib["r"])
                while len(values) <= idx:
                    values.append("")
                values[idx] = cell_value(cell, strings)
            width = max(width, len(values))
            rows.append(values)
    if not rows:
        return []
    header = [str(x) for x in rows[0]]
    out = []
    for values in rows[1:]:
        padded = values + [""] * (len(header) - len(values))
        out.append(dict(zip(header, padded)))
    return out


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def pct(x, digits=1):
    return f"{100 * float(x):.{digits}f}%"


def num(x, digits=3):
    if x == "" or x is None:
        return ""
    return f"{float(x):.{digits}f}"


def read_prior_summary(cfg):
    return read_xlsx_sheet(cfg["diag"], "01_prior_summary")


def read_cluster_summary(cfg):
    return read_xlsx_sheet(cfg["diag"], "02_cluster_summary")


def read_overview(cfg):
    return read_xlsx_sheet(cfg["diag"], "10_prior_overview")


def read_profiles(cfg, prior):
    return read_xlsx_sheet(cfg["tables"] / f"{cfg['prefix']}_{prior}_profiles_full.xlsx")


def rows_for_prior(rows, prior):
    return [r for r in rows if r.get("prior") == prior]


def weighted_global(profile):
    total = sum(float(r["cluster_size"]) for r in profile)
    return {
        col: sum(float(r["cluster_size"]) * float(r[col]) for r in profile) / total
        for col in SHARE_COLS
    }


def family_values(row):
    return {fam: sum(float(row[c]) for c in cols) for fam, cols in FAMILIES.items()}


def family_global(gm):
    return {fam: sum(float(gm[c]) for c in cols) for fam, cols in FAMILIES.items()}


def behavioral_label(row, gm):
    fv = family_values(row)
    fg = family_global(gm)
    s = {c: float(row[c]) for c in SHARE_COLS}
    if s["w_S14"] >= 0.13 or fv["Transport-communication"] >= fg["Transport-communication"] + 0.065:
        return "Transport-communication tres eleve"
    if s["w_S13"] >= 0.11 or fv["Sante"] >= fg["Sante"] + 0.06:
        return "Sante specialisee"
    if fv["Logement-energie"] >= fg["Logement-energie"] + 0.07:
        return "Logement-energie eleve"
    if fv["Alimentaire"] >= fg["Alimentaire"] + 0.075:
        return "Alimentaire contraint"
    if fv["Culture-enseignement"] >= fg["Culture-enseignement"] + 0.04:
        return "Culture-enseignement eleve"
    if fv["Autres depenses"] >= fg["Autres depenses"] + 0.035:
        return "Autres depenses elevees"
    if s["w_S8"] >= 0.15:
        return "Logement S8 dominant"
    if s["w_S2"] >= 0.16:
        return "Alimentaire S2 dominant"
    if fv["Alimentaire"] <= fg["Alimentaire"] - 0.08:
        return "Profil diversifie hors alimentaire"
    return "Profil intermediaire"


def top_items(row, cols, n=5):
    ranked = sorted(((c, float(row[c])) for c in cols), key=lambda x: x[1], reverse=True)
    return ranked[:n]


def signature(row, gm):
    vals = {c: float(row[c]) for c in SHARE_COLS}
    diff = {c: vals[c] - float(gm[c]) for c in SHARE_COLS}
    top = sorted(vals.items(), key=lambda x: x[1], reverse=True)[:5]
    high = sorted(diff.items(), key=lambda x: x[1], reverse=True)[:4]
    low = sorted(diff.items(), key=lambda x: x[1])[:3]
    top_txt = ", ".join(f"{c.replace('w_', '')} {100*v:.1f}%" for c, v in top)
    high_txt = ", ".join(f"{c.replace('w_', '')} +{100*d:.1f} pp" for c, d in high if d > 0.004)
    low_txt = ", ".join(f"{c.replace('w_', '')} {100*d:.1f} pp" for c, d in low if d < -0.004)
    return top_txt, high_txt, low_txt


def prior_comparison_table(cfg):
    p = read_prior_summary(cfg)
    c = read_cluster_summary(cfg)
    rows = []
    for r in p:
        prior = r["prior"]
        cc = rows_for_prior(c, prior)
        weights = [float(x["posterior_weight_mean"]) for x in cc]
        shares = [float(x["assigned_share_full"]) for x in cc]
        sizes = [int(x["assigned_size_full"]) for x in cc]
        rows.append([
            prior,
            int(r["K_MAX"]),
            num(r["alpha_dp_mean"], 3),
            int(r["occupied_weight_gt_1pct"]),
            sum(w >= 0.02 for w in weights),
            sum(w >= 0.03 for w in weights),
            pct(min(shares)),
            min(sizes),
            num(r["mean_max_prob_full"], 3),
            pct(r["share_ambiguous_full_lt_0_60"]),
            int(r["n_divergences"]),
            num(r["min_ess_bulk"], 1),
        ])
    return md_table(
        [
            "Prior",
            "K_MAX",
            "alpha_DP moy.",
            "K eff >1%",
            "K eff >2%",
            "K eff >3%",
            "Plus petit cluster",
            "n min",
            "Prob. max moy.",
            "Ambigus",
            "Divergences",
            "ESS min",
        ],
        rows,
    )


def cluster_summary_table(cfg, prior):
    c = rows_for_prior(read_cluster_summary(cfg), prior)
    rows = []
    for r in c:
        rows.append([
            f"C{int(r['cluster'])}",
            pct(r["posterior_weight_mean"]),
            f"{int(r['assigned_size_full'])} ({pct(r['assigned_share_full'])})",
            num(r["phi_mean"], 1),
            pct(r["mean_S1_theoretical"]),
            "oui" if bool(r["weight_gt_1pct"]) else "non",
        ])
    return md_table(["Cluster", "Poids posteriori", "Affectes", "phi", "S1 theorique", ">1%"], rows)


def global_structure_table(profile):
    gm = weighted_global(profile)
    rows = []
    for i in range(1, 24):
        col = f"w_S{i}"
        rows.append([f"S{i}", S_LABELS[col], S_CODES[f"S{i}"], pct(gm[col])])
    return md_table(["Poste", "Libelle", "Codes source", "Part moyenne"], rows)


def family_structure_table(profile):
    gm = weighted_global(profile)
    fg = family_global(gm)
    rows = [[fam, pct(value)] for fam, value in sorted(fg.items(), key=lambda x: x[1], reverse=True)]
    return md_table(["Famille", "Part moyenne"], rows)


def profile_family_table(cfg, prior):
    prof = read_profiles(cfg, prior)
    gm = weighted_global(prof)
    total = sum(float(r["cluster_size"]) for r in prof)
    rows = []
    for r in prof:
        fv = family_values(r)
        top_fam = sorted(fv.items(), key=lambda x: x[1], reverse=True)[:4]
        rows.append([
            f"C{int(r['cluster_dpmm_nuts'])}",
            f"{int(r['cluster_size'])} ({100*float(r['cluster_size'])/total:.1f}%)",
            behavioral_label(r, gm),
            ", ".join(f"{k} {100*v:.1f}%" for k, v in top_fam),
        ])
    return md_table(["Cluster", "Taille", "Lecture comportementale", "Familles dominantes"], rows)


def profile_signature_table(cfg, prior):
    prof = read_profiles(cfg, prior)
    gm = weighted_global(prof)
    total = sum(float(r["cluster_size"]) for r in prof)
    rows = []
    for r in prof:
        top, high, low = signature(r, gm)
        rows.append([
            f"C{int(r['cluster_dpmm_nuts'])}",
            f"{int(r['cluster_size'])} ({100*float(r['cluster_size'])/total:.1f}%)",
            behavioral_label(r, gm),
            top,
            high,
            low,
        ])
    return md_table(["Cluster", "Taille", "Libelle", "Postes dominants", "Sur-representations", "Sous-representations"], rows)


def profile_numeric_table(cfg, prior, mode="top"):
    prof = read_profiles(cfg, prior)
    total = sum(float(r["cluster_size"]) for r in prof)
    if mode == "top":
        headers = ["Cluster", "Taille", "S1", "S2", "S3", "S6", "S7", "S8", "S9", "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18"]
        cols = ["w_S1", "w_S2", "w_S3", "w_S6", "w_S7", "w_S8", "w_S9", "w_S11", "w_S12", "w_S13", "w_S14", "w_S15", "w_S16", "w_S17", "w_S18"]
    else:
        headers = ["Cluster", "Taille"] + [f"S{i}" for i in range(1, 24)]
        cols = SHARE_COLS
    rows = []
    for r in prof:
        rows.append([
            f"C{int(r['cluster_dpmm_nuts'])}",
            f"{int(r['cluster_size'])} ({100*float(r['cluster_size'])/total:.1f}%)",
            *[f"{100*float(r[c]):.1f}" for c in cols],
        ])
    return md_table(headers, rows)


def overview_table(cfg):
    rows = []
    for r in read_overview(cfg):
        rows.append([
            r["prior"],
            num(r["mean_max_prob_full"], 3),
            pct(r["share_ambiguous_full_lt_0_60"]),
            pct(r["min_cluster_share"]),
            int(r["min_cluster_size"]),
            int(r["n_small_share_lt_1pct"]),
            int(r["n_small_size_lt_100"]),
            num(r["eta2_DAM"], 3),
            num(r["eta2_log_DAM"], 3),
            str(r["top_qualitative_associations"]).replace("|", "/"),
        ])
    return md_table(
        ["Prior", "Prob. max", "Ambigus", "Part min", "n min", "Small <1%", "n<100", "eta2 DAM", "eta2 log_DAM", "Associations dominantes"],
        rows,
    )


def k_context_table(cfg, prior):
    q = rows_for_prior(read_xlsx_sheet(cfg["diag"], "08_quant_by_cluster"), prior)
    d = rows_for_prior(read_xlsx_sheet(cfg["diag"], "06_crosstab_delta"), prior)
    dam = [r for r in q if r["variable"] == "DAM"]
    milieu = [r for r in d if r["variable"] == "Milieu"]
    quint = [r for r in d if r["variable"] == "quintile_DAM"]
    rows = []
    for r in dam:
        cluster = int(r["cluster"])
        urb = [x for x in milieu if int(x["cluster"]) == cluster and str(x["modalite"]).lower() == "urbain"]
        rural = [x for x in milieu if int(x["cluster"]) == cluster and str(x["modalite"]).lower() == "rural"]
        qrows = [x for x in quint if int(x["cluster"]) == cluster]
        top_quint = sorted(qrows, key=lambda x: float(x["delta_vs_global"]), reverse=True)[:1]
        rows.append([
            f"C{cluster}",
            int(r["n"]),
            f"{float(r['mean']):.0f}",
            f"{float(r['median']):.0f}",
            f"{100*float(r['relative_delta_mean_vs_global']):+.1f}%",
            pct(urb[0]["row_pct"]) if urb else "",
            pct(rural[0]["row_pct"]) if rural else "",
            f"Q{top_quint[0]['modalite']} ({pct(top_quint[0]['row_pct'])})" if top_quint else "",
        ])
    return md_table(["Cluster", "n", "DAM moy.", "DAM med.", "Ecart DAM", "Urbain", "Rural", "Quintile surrep."], rows)


def case_comment(case, preferred):
    if case == "ENNVM 2007":
        return (
            "Lecture : les quatre priors gardent les 7 composantes au seuil de 1%, mais la lecture a 23 postes montre "
            "que les groupes ne sont pas artificiellement vides. Le prior gamma_0p25_2 est retenu comme lecture principale "
            "car il combine des tailles non minuscules, un K effectif de 7 meme au seuil de 3%, et la meilleure separation "
            "socio-economique globale selon eta2_DAM. gamma_0p5_2 donne la classification la plus nette, mais avec un petit "
            "cluster plus proche du seuil de rarete."
        )
    return (
        "Lecture : en 2014, les 7 composantes sont toutes substantielles quel que soit le prior. gamma_1_1 est retenu comme "
        "lecture principale parce qu'il maximise la discrimination socio-economique et garde des tailles confortables. "
        "gamma_1_2 est tres proche et donne meme une probabilite maximale moyenne legerement superieure ; il sert donc de "
        "verification de robustesse plutot que de contradiction."
    )


def case_section(case, cfg):
    preferred = cfg["preferred"]
    pref_profile = read_profiles(cfg, preferred)
    lines = [f"## {case} - resultats DPMM 23 postes", ""]
    lines += ["### Structure moyenne de reference", "", family_structure_table(pref_profile), "", global_structure_table(pref_profile), ""]
    lines += ["### Comparaison des priors et nombre effectif de clusters", "", prior_comparison_table(cfg), ""]
    lines.append(case_comment(case, preferred))
    lines += ["", "### Diagnostic socio-economique global par prior", "", overview_table(cfg), ""]
    lines += [f"### Lecture principale des profils : {preferred}", ""]
    lines += ["#### Tailles, poids et concentration", "", cluster_summary_table(cfg, preferred), ""]
    lines += ["#### Lecture par grandes familles budgetaires", "", profile_family_table(cfg, preferred), ""]
    lines += ["#### Signatures fines S1-S23", "", profile_signature_table(cfg, preferred), ""]
    lines += ["#### Tableau numerique des postes structurants", "", profile_numeric_table(cfg, preferred, mode="top"), ""]
    lines += ["#### Caracterisation socio-economique", "", k_context_table(cfg, preferred), ""]
    lines += ["### Sensibilite des profils aux priors", ""]
    for prior in PRIORS:
        lines += [f"#### {prior}", "", profile_signature_table(cfg, prior), ""]
    lines += ["### Annexe numerique : profils complets S1-S23 par prior", ""]
    for prior in PRIORS:
        lines += [f"#### Profils numeriques complets - {prior}", "", profile_numeric_table(cfg, prior, mode="full"), ""]
    return "\n".join(lines)


def build_markdown():
    lines = ["# Rapport detaille des resultats DPMM - 23 postes, ENNVM 2007 et ENCDM 2014", ""]
    lines.append(
        "Ce rapport analyse les sorties du Dirichlet Process Mixture Model tronque applique aux matrices de parts budgetaires "
        "en 23 postes. La troncature fixe K_MAX=7 ne doit pas etre lue comme un K impose de maniere naive : le nombre effectif "
        "est juge a partir des poids posteriori, des tailles affectees, des composantes quasi vides, de la qualite d'affectation "
        "et de la coherence economique des profils."
    )
    lines += ["", "## Rappel methodologique", ""]
    lines.append(
        "Le modele estime des composantes Dirichlet avec une priorisation de type processus de Dirichlet tronque. Les quatre priors "
        "testes sur alpha_DP sont gamma_1_1, gamma_1_2, gamma_0p5_2 et gamma_0p25_2. Les labels sont stabilises par une contrainte "
        "d'ordre sur S1, ce qui rend la comparaison des composantes interpretable apres estimation. Les menages sont ensuite affectes "
        "au cluster de probabilite posteriori maximale sur l'echantillon complet."
    )
    lines += ["", "## Libelles des 23 postes", ""]
    rows = [[f"S{i}", S_LABELS[f"w_S{i}"], S_CODES[f"S{i}"]] for i in range(1, 24)]
    lines.append(md_table(["Poste", "Libelle", "Codes source"], rows))
    lines += ["", "## Conclusion generale", ""]
    lines.append(
        "Pour les deux bases, le DPMM 23 postes est plus stable que ce que l'on pouvait craindre avec une troncature a 7 composantes : "
        "aucune solution principale ne contient de cluster vide ou quasi vide. En 2007, certains priors suggerent une composante rare "
        "autour de 2%, mais elle reste exploitable et economiquement lisible. En 2014, les sept groupes sont clairement substantiels, "
        "avec un minimum superieur a 3,7% selon les priors. La conclusion operationnelle est donc plus nette que pour 9 postes : le "
        "DPMM 23 postes soutient une segmentation effective a 7 profils, tout en gardant l'idee qu'une presentation synthetique peut "
        "regrouper certains profils voisins en 6 familles comportementales."
    )
    lines.append("")
    for case, cfg in CASES.items():
        lines.append(case_section(case, cfg))
        lines.append("")
    lines += ["## Synthese comparative 2007-2014", ""]
    lines.append(
        "Le passage de 9 a 23 postes rend les profils plus riches : les composantes ne sont plus seulement alimentaires, logement, "
        "sante ou transport ; elles distinguent aussi des sous-types alimentaires, les differents blocs du logement, la sante detaillee, "
        "la culture/enseignement et les postes residuels. En 2007, la segmentation reste fortement liee au niveau de vie et au milieu, "
        "avec des profils alimentaires/logement opposes a des profils sante, transport ou depenses diversifiees. En 2014, la separation "
        "par niveau de vie demeure forte mais les profils sont plus differencies, ce qui traduit une diversification de la structure "
        "de consommation et une meilleure identification des comportements non alimentaires."
    )
    return "\n".join(lines)


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def docx_p(text="", style=None):
    text = escape(str(text))
    ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f'<w:p>{ppr}<w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'


def docx_code(text):
    text = escape(str(text))
    return (
        '<w:p><w:pPr><w:pStyle w:val="Code"/></w:pPr>'
        '<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>'
        '<w:sz w:val="16"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
    )


def make_docx(md):
    out = []
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("|"):
            out.append(docx_code(line))
        elif not line.strip():
            out.append(docx_p(""))
        elif line.startswith("# "):
            out.append(docx_p(line[2:], "Title"))
        elif line.startswith("## "):
            out.append(docx_p(line[3:], "Heading1"))
        elif line.startswith("### "):
            out.append(docx_p(line[4:], "Heading2"))
        elif line.startswith("#### "):
            out.append(docx_p(line[5:], "Heading3"))
        else:
            out.append(docx_p(line.replace("`", "")))
    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:body>'
        + "".join(out)
        + '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        + '<w:pgMar w:top="1440" w:right="900" w:bottom="1440" w:left="900"/>'
        + "</w:sectPr></w:body></w:document>"
    )
    styles_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="21"/></w:rPr><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="34"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:pPr><w:spacing w:before="360" w:after="180"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="24"/></w:rPr><w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="22"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Code"><w:name w:val="Code"/><w:basedOn w:val="Normal"/><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="16"/></w:rPr><w:pPr><w:spacing w:after="0"/></w:pPr></w:style>
</w:styles>'''
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>'''
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'''
    doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'''
    with ZipFile(DOCX_PATH, "w", ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("word/document.xml", document_xml)
        z.writestr("word/styles.xml", styles_xml)


def main():
    md = build_markdown()
    MD_PATH.write_text(md, encoding="utf-8")
    make_docx(md)
    print(MD_PATH)
    print(DOCX_PATH)


if __name__ == "__main__":
    main()
