from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "rapport_resultats_DMM_23postes_2007_2014.md"
DOCX_PATH = ROOT / "rapport_resultats_DMM_23postes_2007_2014.docx"

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

CASES = {
    "ENNVM 2007": {
        "prefix": "ennvm_2007_23",
        "tables": Path("outputs/tables/dmm_ennvm_23"),
        "processed": Path("data/processed/ennvm_2007_parts_budgetaires_23.xlsx"),
        "diag": Path("outputs/analysis_dmm_ennvm_23_diagnostic/ENNVM_2007_23postes_diagnostic_K.xlsx"),
    },
    "ENCDM 2014": {
        "prefix": "encdm_2014_23",
        "tables": Path("outputs/tables/dmm_encdm_23"),
        "processed": Path("data/processed/encdm_2014_parts_budgetaires_23.xlsx"),
        "diag": Path("outputs/analysis_dmm_encdm_23_diagnostic/ENCDM_2014_23postes_diagnostic_K.xlsx"),
    },
}


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def load_profiles(cfg, k):
    return pd.read_excel(cfg["tables"] / f"{cfg['prefix']}_dmm_profiles_K{k}.xlsx")


def global_mean(cfg):
    df = pd.read_excel(cfg["processed"], usecols=SHARE_COLS)
    return df[SHARE_COLS].mean()


def family_values(row):
    return {fam: float(row[cols].sum()) for fam, cols in FAMILIES.items()}


def family_global(gm):
    return {fam: float(gm[cols].sum()) for fam, cols in FAMILIES.items()}


def behavioral_label(row, gm):
    fv = family_values(row)
    fg = family_global(gm)
    s = {c: float(row[c]) for c in SHARE_COLS}
    if s["w_S14"] >= 0.12:
        return "Transport tres eleve"
    if s["w_S13"] >= 0.10 or fv["Sante"] - fg["Sante"] >= 0.055:
        return "Sante detaillee elevee"
    if fv["Logement-energie"] - fg["Logement-energie"] >= 0.07:
        return "Logement-energie tres eleve"
    if fv["Alimentaire"] - fg["Alimentaire"] >= 0.07:
        return "Alimentaire contraint"
    if fv["Alimentaire"] <= fg["Alimentaire"] - 0.08 and fv["Transport-communication"] >= fg["Transport-communication"] + 0.04:
        return "Diversifie transport/autres"
    if fv["Autres depenses"] >= fg["Autres depenses"] + 0.035:
        return "Autres/culture diversifies"
    if s["w_S8"] >= 0.15:
        return "Logement poste S8 eleve"
    if s["w_S2"] >= 0.16:
        return "Alimentaire S2 dominant"
    return "Profil intermediaire"


def cluster_signature(row, gm):
    vals = row[SHARE_COLS].astype(float)
    diff = vals - gm
    top = vals.sort_values(ascending=False).head(5)
    over = diff.sort_values(ascending=False).head(4)
    low = diff.sort_values().head(3)
    top_txt = ", ".join(f"{c.replace('w_', '')} {100*v:.1f}%" for c, v in top.items())
    over_txt = ", ".join(f"{c.replace('w_', '')} +{100*d:.1f} pp" for c, d in over.items() if d > 0.004)
    low_txt = ", ".join(f"{c.replace('w_', '')} {100*d:.1f} pp" for c, d in low.items() if d < -0.004)
    return top_txt, over_txt, low_txt


def summary_table(summary):
    headers = ["K", "BIC", "AIC", "Entropie", "Prob. max moy.", "Ambigus <0.60", "Taille min", "Taille max"]
    rows = []
    for _, r in summary.iterrows():
        rows.append([
            int(r["K"]),
            f"{r['BIC']:.0f}",
            f"{r['AIC']:.0f}",
            f"{r['entropy_norm']:.3f}",
            f"{r['mean_max_prob']:.3f}",
            f"{100*r['share_ambiguous_prob_lt_0_60']:.1f}%",
            int(r["min_cluster_size"]),
            int(r["max_cluster_size"]),
        ])
    return md_table(headers, rows)


def global_tables(cfg):
    gm = global_mean(cfg)
    rows_s = [[f"S{i}", S_LABELS[f"w_S{i}"], f"{100*gm[f'w_S{i}']:.1f}%"] for i in range(1, 24)]
    fg = family_global(gm)
    rows_f = [[fam, f"{100*val:.1f}%"] for fam, val in sorted(fg.items(), key=lambda x: -x[1])]
    return md_table(["Poste", "Libelle court", "Part moyenne"], rows_s), md_table(["Famille", "Part moyenne"], rows_f)


def profile_family_table(cfg, k, gm):
    prof = load_profiles(cfg, k)
    total = prof["cluster_size"].sum()
    headers = ["Cluster", "Taille", "Libelle", *FAMILIES.keys()]
    rows = []
    for _, r in prof.iterrows():
        fv = family_values(r)
        rows.append([
            f"C{int(r['cluster'])}",
            f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
            behavioral_label(r, gm),
            *[f"{100*fv[fam]:.1f}" for fam in FAMILIES],
        ])
    return md_table(headers, rows)


def profile_signature_table(cfg, k, gm):
    prof = load_profiles(cfg, k)
    total = prof["cluster_size"].sum()
    headers = ["Cluster", "Taille", "Libelle", "Postes dominants", "Sur-representations", "Sous-representations"]
    rows = []
    for _, r in prof.iterrows():
        top, over, low = cluster_signature(r, gm)
        rows.append([
            f"C{int(r['cluster'])}",
            f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
            behavioral_label(r, gm),
            top,
            over,
            low,
        ])
    return md_table(headers, rows)


def profile_numeric_table(cfg, k, gm):
    prof = load_profiles(cfg, k)
    total = prof["cluster_size"].sum()
    headers = ["Cluster", "Taille", *[f"S{i}" for i in range(1, 24)]]
    rows = []
    for _, r in prof.iterrows():
        rows.append([
            f"C{int(r['cluster'])}",
            f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
            *[f"{100*r[f'w_S{i}']:.1f}" for i in range(1, 24)],
        ])
    return md_table(headers, rows)


def k6_context_table(cfg):
    diag = cfg["diag"]
    q = pd.read_excel(diag, sheet_name="06_quantitative_by_cluster")
    dam = q[(q["K"] == 6) & (q["variable"] == "DAM")][
        ["cluster", "n", "mean", "median", "relative_delta_mean_vs_global"]
    ].copy()
    d = pd.read_excel(diag, sheet_name="04_crosstab_global_delta")
    milieu = d[(d["K"] == 6) & (d["variable"] == "Milieu")]
    quint = d[(d["K"] == 6) & (d["variable"] == "quintile_DAM")]
    rows = []
    for _, r in dam.iterrows():
        cluster = int(r["cluster"])
        urb = milieu[(milieu["cluster"] == cluster) & (milieu["modalite"].astype(str).str.lower() == "urbain")]
        rural = milieu[(milieu["cluster"] == cluster) & (milieu["modalite"].astype(str).str.lower() == "rural")]
        top_quint = quint[quint["cluster"] == cluster].sort_values("delta_vs_global", ascending=False).head(1)
        rows.append([
            f"C{cluster}",
            int(r["n"]),
            f"{r['mean']:.0f}",
            f"{r['median']:.0f}",
            f"{100*r['relative_delta_mean_vs_global']:+.1f}%",
            f"{100*urb['row_pct'].iloc[0]:.1f}%" if not urb.empty else "",
            f"{100*rural['row_pct'].iloc[0]:.1f}%" if not rural.empty else "",
            f"Q{top_quint['modalite'].iloc[0]} ({100*top_quint['row_pct'].iloc[0]:.1f}%)" if not top_quint.empty else "",
        ])
    return md_table(["Cluster", "n", "DAM moy.", "DAM med.", "Ecart DAM", "Urbain", "Rural", "Quintile surrep."], rows)


def overview_diag_table(cfg):
    ov = pd.read_excel(cfg["diag"], sheet_name="08_K_overview")
    headers = ["K", "Cramer Milieu", "Cramer quintile_DAM", "eta2 DAM", "eta2 log_DAM", "Associations qualitatives dominantes"]
    rows = []
    for _, r in ov.iterrows():
        rows.append([
            int(r["K"]),
            f"{r['cramer_milieu']:.3f}" if not pd.isna(r["cramer_milieu"]) else "",
            f"{r['cramer_quintile_DAM']:.3f}" if not pd.isna(r["cramer_quintile_DAM"]) else "",
            f"{r['eta2_DAM']:.3f}" if not pd.isna(r["eta2_DAM"]) else "",
            f"{r['eta2_log_DAM']:.3f}" if not pd.isna(r["eta2_log_DAM"]) else "",
            str(r["top_qualitative_associations"]).replace("|", "/"),
        ])
    return md_table(headers, rows)


def alpha_k6_table(cfg):
    alpha = pd.read_excel(cfg["tables"] / f"{cfg['prefix']}_dmm_alpha_K6.xlsx")
    headers = ["Cluster", "pi", "alpha_sum", "Profil theorique dominant"]
    rows = []
    for _, r in alpha.iterrows():
        a = np.array([r[f"alpha_S{i}"] for i in range(1, 24)], dtype=float)
        m = a / a.sum()
        top = np.argsort(-m)[:5]
        top_txt = ", ".join(f"S{i+1}={100*m[i]:.1f}%" for i in top)
        rows.append([f"C{int(r['cluster'])}", f"{r['pi']:.3f}", f"{r['alpha_sum']:.1f}", top_txt])
    return md_table(headers, rows)


def case_section(case, cfg):
    summary = pd.read_excel(cfg["tables"] / f"{cfg['prefix']}_dmm_k2_to_k9_summary.xlsx")
    gm = global_mean(cfg)
    s_table, f_table = global_tables(cfg)
    lines = [f"## {case} - resultats DMM 23 postes", ""]
    lines += ["### Structure moyenne de reference", "", "#### Parts S1-S23", "", s_table, "", "#### Regroupement par familles", "", f_table, ""]
    lines += ["### Comparaison statistique de K=2 a K=9", "", summary_table(summary), ""]
    if case == "ENNVM 2007":
        lines.append(
            "Lecture : les criteres AIC/BIC continuent de favoriser K=9, mais la solution devient progressivement plus fragmentee. "
            "K=6 donne deja une decomposition fine avec des groupes interpretablement distincts : alimentaire contraint, sante detaillee, "
            "transport tres eleve, logement-energie et profils intermediaires. K=7 apporte une nuance supplementaire sans perte forte, "
            "mais K=8 introduit un groupe plus petit et K=9 fragmente davantage la lecture. Le choix central defendable est donc K=6, "
            "avec K=7 comme extension analytique possible."
        )
    else:
        lines.append(
            "Lecture : ENCDM 2014 conserve des tailles de clusters relativement solides meme pour K eleve, mais l'ambiguite augmente "
            "de 10,2% a K=6 a 16,1% a K=9. K=6 isole clairement les grands comportements : alimentaire populaire, logement-energie, "
            "sante, transport tres eleve et profils diversifies. K=7 ou K=8 sont utiles pour raffiner, mais K=6 reste la meilleure base "
            "de lecture comportementale."
        )
    lines += ["", "### Propagation comportementale des profils", ""]
    if case == "ENNVM 2007":
        lines.append(
            "A K=2, le modele oppose un grand bloc alimentaire-logement a un bloc plus aise/diversifie. K=3 separe deja une composante "
            "a forte sante et une composante alimentaire. K=4 clarifie le transport tres eleve. K=5 et K=6 distinguent mieux logement, "
            "sante detaillee et alimentation. Au-dela, les nouvelles classes deviennent surtout des sous-profils : variations de S8/S11 "
            "dans le logement, de S13 dans la sante ou de S14 dans le transport."
        )
    else:
        lines.append(
            "En 2014, K=2 resume encore une opposition alimentaire/logement contre profils diversifies. K=3 et K=4 font ressortir logement "
            "et sante. K=5 introduit nettement le transport tres eleve. K=6 est le premier niveau ou les six profils principaux deviennent "
            "lisibles ensemble. K=7-K9 ajoutent des sous-profils culture-autres, logement S8 et sante S13, mais au prix d'une classification "
            "moins nette."
        )
    lines += ["", "### Profils K=6 : lecture par familles", "", profile_family_table(cfg, 6, gm), ""]
    lines += ["### Profils K=6 : signatures fines S1-S23", "", profile_signature_table(cfg, 6, gm), ""]
    lines += ["### Caracterisation socio-economique K=6", "", k6_context_table(cfg), ""]
    lines += ["### Parametres de Dirichlet K=6", ""]
    lines.append(
        "`pi` donne le poids du cluster dans le melange. `alpha_sum` indique la concentration du profil : plus elle est elevee, "
        "plus la composante est homogene autour de son profil moyen theorique."
    )
    lines += ["", alpha_k6_table(cfg), ""]
    lines += ["### Diagnostics socio-economiques globaux", "", overview_diag_table(cfg), ""]
    lines += ["### Annexe : signatures des profils pour tous les K", ""]
    for k in range(2, 10):
        lines += [f"#### K={k}", "", profile_signature_table(cfg, k, gm), ""]
    lines += ["### Annexe : profils numeriques complets pour tous les K", ""]
    lines.append("Les valeurs sont exprimees en pourcentage de la depense totale du menage dans le cluster.")
    lines.append("")
    for k in range(2, 10):
        lines += [f"#### Profils numeriques K={k}", "", profile_numeric_table(cfg, k, gm), ""]
    return "\n".join(lines)


def build_markdown():
    lines = ["# Rapport detaille des resultats DMM - 23 postes, ENNVM 2007 et ENCDM 2014", ""]
    lines.append(
        "Ce rapport analyse les resultats du DMM applique aux matrices fines en 23 postes. Par rapport au rapport 9 postes, "
        "l'objectif est de decrire les sous-profils de consommation : sous-composantes alimentaires, logement-energie, sante detaillee, "
        "transport, culture et autres depenses. La lecture economique est faite a deux niveaux : les postes fins S1-S23 et des familles "
        "agregees reconstruites a partir du mapping des matrices."
    )
    lines += ["", "## Mapping S1-S23 utilise dans le rapport", ""]
    rows = [[s, S_CODES[s], S_LABELS[f"w_{s}"]] for s in [f"S{i}" for i in range(1, 24)]]
    lines.append(md_table(["Poste", "Codes sources", "Libelle court"], rows))
    lines += ["", "## Conclusion generale sur K", ""]
    lines.append(
        "Pour les deux enquetes, AIC/BIC favorisent les solutions les plus fines, mais la lecture comportementale ne doit pas suivre "
        "automatiquement K=9. Les solutions fines augmentent l'ambiguite et multiplient des sous-profils parfois proches. K=6 ressort "
        "comme solution centrale : il donne une segmentation riche, beaucoup plus informative que K=2-K4, tout en restant lisible. "
        "K=7 peut etre considere comme variante raffinee, surtout pour ENNVM 2007, mais K=6 reste le meilleur choix de presentation."
    )
    lines.append("")
    for case, cfg in CASES.items():
        lines.append(case_section(case, cfg))
        lines.append("")
    lines += ["## Synthese comparative 2007-2014", ""]
    lines.append(
        "Les deux annees montrent une stratification forte des comportements budgetaires. Les profils modestes restent marques par "
        "l'alimentaire et certaines composantes de logement. Les profils plus aises ou plus urbains se signalent par la montee de la sante, "
        "du transport, de la communication, de la culture et des autres depenses. La matrice en 23 postes permet surtout de voir que les "
        "clusters ne se differencient pas seulement par le volume alimentaire total : ils se distinguent aussi par la composition interne "
        "de l'alimentaire, par le type de logement/energie, et par l'apparition de postes tres specifiques comme S13 ou S14."
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
        + '<w:pgMar w:top="1440" w:right="720" w:bottom="1440" w:left="720"/>'
        + "</w:sectPr></w:body></w:document>"
    )
    styles_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="21"/></w:rPr><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="34"/></w:rPr><w:pPr><w:spacing w:after="300"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:pPr><w:spacing w:before="360" w:after="180"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="24"/></w:rPr><w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="22"/></w:rPr><w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr></w:style>
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
