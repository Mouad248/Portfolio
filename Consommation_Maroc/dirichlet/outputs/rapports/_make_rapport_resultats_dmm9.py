from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "rapport_resultats_DMM_9postes_2007_2014.md"
DOCX_PATH = ROOT / "rapport_resultats_DMM_9postes_2007_2014.docx"

SHARE_COLS = [f"w_G{i}" for i in range(1, 10)]
POST_LABELS = {
    "w_G1": "Alimentation & boissons",
    "w_G2": "Habillement & chaussures",
    "w_G3": "Logement, eau, energie",
    "w_G4": "Boissons alcool. & tabac",
    "w_G5": "Ameublement & equipement",
    "w_G6": "Sante",
    "w_G7": "Transport",
    "w_G8": "Communication",
    "w_G9": "Loisirs, culture & enseignement",
}

CASES = {
    "ENNVM 2007": {
        "short": "2007",
        "prefix": "ennvm_2007",
        "tables": Path("outputs/tables/dmm_ennvm_9"),
        "processed": Path("data/processed/ennvm_2007_parts_budgetaires.xlsx"),
        "diag": Path("outputs/analysis_dmm_ennvm_9_diagnostic/ENNVM_2007_9postes_diagnostic_K.xlsx"),
    },
    "ENCDM 2014": {
        "short": "2014",
        "prefix": "encdm_2014",
        "tables": Path("outputs/tables/dmm_encdm_9"),
        "processed": Path("data/processed/encdm_2014_parts_budgetaires.xlsx"),
        "diag": Path("outputs/analysis_dmm_encdm_9_diagnostic/ENCDM_2014_9postes_diagnostic_K.xlsx"),
    },
}


def fmt_pct(x, digits=1):
    if pd.isna(x):
        return ""
    return f"{100 * x:.{digits}f}%"


def fmt_num(x, digits=2):
    if pd.isna(x):
        return ""
    if isinstance(x, (int, np.integer)):
        return str(int(x))
    return f"{x:.{digits}f}"


def md_table(headers, rows):
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def load_profiles(cfg, k):
    path = cfg["tables"] / f"{cfg['prefix']}_dmm_profiles_K{k}.xlsx"
    return pd.read_excel(path)


def global_mean(cfg):
    df = pd.read_excel(cfg["processed"], usecols=SHARE_COLS)
    return df[SHARE_COLS].mean()


def cluster_signature(row, gm):
    vals = row[SHARE_COLS].astype(float)
    diff = vals - gm
    dominant = vals.sort_values(ascending=False).head(3)
    high = diff.sort_values(ascending=False).head(3)
    low = diff.sort_values().head(2)

    dom_txt = ", ".join(f"{POST_LABELS[c]} {100*v:.1f}%" for c, v in dominant.items())
    high_txt = ", ".join(f"{POST_LABELS[c]} +{100*d:.1f} pp" for c, d in high.items() if d > 0.005)
    low_txt = ", ".join(f"{POST_LABELS[c]} {100*d:.1f} pp" for c, d in low.items() if d < -0.005)
    return dom_txt, high_txt, low_txt


def behavioral_label(row, gm):
    vals = row[SHARE_COLS].astype(float)
    diff = vals - gm
    if vals["w_G6"] >= 0.20:
        return "Sante tres elevee"
    if vals["w_G6"] >= 0.14 and vals["w_G7"] >= 0.08:
        return "Sante-transport aise"
    if diff["w_G5"] >= 0.05:
        return "Equipement/logement"
    if diff["w_G3"] >= 0.075:
        return "Logement tres eleve"
    if diff["w_G1"] >= 0.055 and diff["w_G3"] >= 0.025:
        return "Alimentation-logement"
    if diff["w_G1"] >= 0.055:
        return "Alimentation dominante"
    if diff["w_G8"] >= 0.04:
        return "Communication elevee"
    if diff["w_G1"] <= -0.08 and (diff["w_G6"] > 0.04 or diff["w_G7"] > 0.03):
        return "Diversifie hors alimentaire"
    if diff["w_G3"] >= 0.03:
        return "Logement renforce"
    return "Profil intermediaire"


def profile_table(cfg, k, gm, compact=False):
    prof = load_profiles(cfg, k)
    total = prof["cluster_size"].sum()
    headers = ["Cluster", "Taille", "Libelle comportemental", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
    rows = []
    for _, r in prof.iterrows():
        rows.append([
            f"C{int(r['cluster'])}",
            f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
            behavioral_label(r, gm),
            *[f"{100*r[c]:.1f}" for c in SHARE_COLS],
        ])
    if compact:
        headers = ["Cluster", "Taille", "Libelle comportemental", "Postes dominants", "Sur-representations"]
        rows = []
        for _, r in prof.iterrows():
            dom, high, _ = cluster_signature(r, gm)
            rows.append([
                f"C{int(r['cluster'])}",
                f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
                behavioral_label(r, gm),
                dom,
                high,
            ])
    return md_table(headers, rows)


def summary_table(summary):
    headers = ["K", "BIC", "AIC", "Entropie", "Prob. max moy.", "Ambigus < 0.60", "Taille min", "Taille max"]
    rows = []
    for _, r in summary.iterrows():
        rows.append([
            int(r["K"]),
            f"{r['BIC']:.0f}",
            f"{r['AIC']:.0f}",
            f"{r['entropy_norm']:.3f}",
            f"{r['mean_max_prob']:.3f}",
            fmt_pct(r["share_ambiguous_prob_lt_0_60"]),
            int(r["min_cluster_size"]),
            int(r["max_cluster_size"]),
        ])
    return md_table(headers, rows)


def k6_context_tables(case, cfg):
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
    return md_table(
        ["Cluster", "n", "DAM moy.", "DAM med.", "Ecart DAM", "Urbain", "Rural", "Quintile surrep."],
        rows,
    )


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
        a = np.array([r[f"alpha_G{i}"] for i in range(1, 10)], dtype=float)
        m = a / a.sum()
        top = np.argsort(-m)[:3]
        top_txt = ", ".join(f"G{i+1}={100*m[i]:.1f}%" for i in top)
        rows.append([f"C{int(r['cluster'])}", f"{r['pi']:.3f}", f"{r['alpha_sum']:.1f}", top_txt])
    return md_table(headers, rows)


def build_case_section(case, cfg):
    summary = pd.read_excel(cfg["tables"] / f"{cfg['prefix']}_dmm_k2_to_k9_summary.xlsx")
    gm = global_mean(cfg)
    lines = []
    lines.append(f"## {case} - resultats DMM 9 postes")
    lines.append("")
    lines.append("### Profil moyen global de l'echantillon")
    lines.append("")
    rows = [[f"G{i}", POST_LABELS[f"w_G{i}"], f"{100*gm[f'w_G{i}']:.1f}%"] for i in range(1, 10)]
    lines.append(md_table(["Poste", "Libelle", "Part moyenne"], rows))
    lines.append("")
    lines.append("### Comparaison statistique des valeurs de K")
    lines.append("")
    lines.append(summary_table(summary))
    lines.append("")
    if case == "ENNVM 2007":
        lines.append(
            "Lecture synthetique : les criteres de vraisemblance, AIC et BIC continuent de s'ameliorer jusqu'a K=9, "
            "ce qui est attendu dans un melange fini flexible. Cependant, la qualite classificatoire se degrade apres K=6 : "
            "la probabilite maximale moyenne descend de 0,824 a K=6 a 0,771 a K=9, et la part des menages ambigus passe de "
            "14,0% a 23,9%. Les solutions K=7 a K=9 introduisent aussi des groupes tres petits, autour de 160 menages. "
            "Pour une lecture comportementale, K=6 est donc le compromis le plus defendable ; K=5 reste une solution plus conservatrice."
        )
    else:
        lines.append(
            "Lecture synthetique : comme pour 2007, AIC et BIC favorisent mecaniquement les solutions les plus fines. "
            "Mais K=9 introduit un cluster minuscule de 162 menages et une ambiguite proche de 27,5%. K=6 conserve des tailles "
            "de clusters raisonnables, avec un minimum de 1095 menages, tout en isolant les grands comportements budgetaires. "
            "K=7 ou K=8 peuvent servir a une analyse plus fine, mais K=6 reste la solution centrale pour l'interpretation."
        )
    lines.append("")

    lines.append("### Propagation des profils de K=2 a K=9")
    lines.append("")
    if case == "ENNVM 2007":
        lines.append(
            "La partition commence a K=2 par une opposition entre un profil plus diversifie, moins alimentaire et plus urbain, "
            "et un profil plus alimentaire-logement. A K=3, le bloc essentiel se separe entre un profil fortement alimentaire "
            "et un profil alimentaire-logement. A K=4, apparait plus clairement un groupe a sante et communication elevees. "
            "A K=5, le modele isole un petit groupe a tres forte part de sante. A K=6, les principaux comportements sont lisibles "
            "sans tomber encore dans une fragmentation excessive. A partir de K=7, ce groupe sante se divise en un noyau extreme "
            "et un groupe plus modere ; K=8 et K=9 ajoutent surtout des sous-profils de logement, equipement et communication."
        )
    else:
        lines.append(
            "La partition de 2014 commence egalement par une opposition entre depenses essentielles et depenses plus diversifiees. "
            "A K=3, les profils alimentaire, logement et diversifie se separent. A K=4, le logement tres eleve devient un comportement distinct. "
            "A K=5, le modele isole un groupe aise marque par la sante, le transport et la communication. A K=6, la structure devient "
            "economiquement tres claire : alimentaire populaire, logement contraint, centre urbain, communication/equipement et profil aise. "
            "Les valeurs K=7 et K=8 raffinent surtout les profils logement et communication. K=9 ajoute un petit groupe loisirs-culture, "
            "mais sa taille de 1% le rend fragile comme classe generale."
        )
    lines.append("")

    lines.append("### Profils detailles pour K=6")
    lines.append("")
    lines.append(profile_table(cfg, 6, gm, compact=False))
    lines.append("")
    lines.append("### Caracterisation socio-economique des profils K=6")
    lines.append("")
    lines.append(k6_context_tables(case, cfg))
    lines.append("")
    lines.append("### Parametres de Dirichlet pour K=6")
    lines.append("")
    lines.append(
        "Le parametre `pi` represente le poids estime de la composante dans le melange. `alpha_sum` mesure la concentration : "
        "plus elle est elevee, plus le profil theorique du cluster est homogene autour de sa moyenne."
    )
    lines.append("")
    lines.append(alpha_k6_table(cfg))
    lines.append("")
    lines.append("### Diagnostics socio-economiques globaux par K")
    lines.append("")
    lines.append(overview_diag_table(cfg))
    lines.append("")
    lines.append("### Annexe : signatures de profils pour tous les K")
    lines.append("")
    for k in range(2, 10):
        lines.append(f"#### K={k}")
        lines.append("")
        lines.append(profile_table(cfg, k, gm, compact=True))
        lines.append("")
    lines.append("### Annexe : profils numeriques complets pour tous les K")
    lines.append("")
    lines.append(
        "Les valeurs ci-dessous sont exprimees en pourcentage de la depense totale du menage dans chaque cluster. "
        "Elles permettent de retrouver precisement la contribution de chaque poste G1-G9."
    )
    lines.append("")
    for k in range(2, 10):
        lines.append(f"#### Profils numeriques K={k}")
        lines.append("")
        lines.append(profile_table(cfg, k, gm, compact=False))
        lines.append("")
    return "\n".join(lines)


def build_markdown():
    lines = []
    lines.append("# Rapport detaille des resultats DMM - 9 postes, ENNVM 2007 et ENCDM 2014")
    lines.append("")
    lines.append("## Objet et angle de lecture")
    lines.append("")
    lines.append(
        "Ce rapport presente les resultats du Dirichlet Mixture Model fini applique aux matrices de parts budgetaires en 9 postes. "
        "Il couvre uniquement les cas ENNVM 2007 et ENCDM 2014. L'accent est mis sur les profils comportementaux issus des clusters : "
        "ce que chaque groupe consomme relativement plus ou moins, comment les profils se divisent lorsque K augmente, et quelles solutions "
        "sont les plus defendables pour une interpretation economique."
    )
    lines.append("")
    lines.append(
        "Les profils sont lus a partir des parts budgetaires moyennes des menages affectes a chaque cluster. Les diagnostics socio-economiques "
        "utilisent les fichiers de diagnostic deja generes et servent a qualifier les groupes par niveau de depense, milieu et quintiles de DAM. "
        "Les resultats de modelisation DMM eux-memes sont construits sur les matrices de parts normalisees."
    )
    lines.append("")
    lines.append("## Libelles des 9 postes")
    lines.append("")
    rows = [[f"G{i}", POST_LABELS[f"w_G{i}"]] for i in range(1, 10)]
    lines.append(md_table(["Poste", "Libelle"], rows))
    lines.append("")
    lines.append("## Conclusion generale sur le choix de K")
    lines.append("")
    lines.append(
        "Dans les deux enquetes, les criteres AIC/BIC continuent d'avantager les solutions plus fines, surtout K=9. "
        "Cette amelioration statistique ne doit pas etre confondue avec une meilleure interpretabilite. Les solutions elevees "
        "reduisent la nettete des affectations, augmentent la part de menages ambigus et finissent par creer des groupes tres petits. "
        "Pour l'analyse comportementale, K=6 ressort comme le meilleur compromis commun : il conserve des tailles suffisantes, "
        "fait apparaitre les grands profils economiques et reste lisible. Pour ENNVM 2007, K=5 peut etre defendu comme version plus sobre ; "
        "pour ENCDM 2014, K=7 ou K=8 peuvent etre exploites comme raffinement, mais K=6 reste la base de lecture la plus robuste."
    )
    lines.append("")
    for case, cfg in CASES.items():
        lines.append(build_case_section(case, cfg))
        lines.append("")
    lines.append("## Synthese comparative 2007-2014")
    lines.append("")
    lines.append(
        "Le passage de 2007 a 2014 fait ressortir une structure plus diversifiee en 2014. La part alimentaire moyenne baisse, "
        "tandis que le logement, l'equipement, la communication et les depenses liees a des comportements plus urbains prennent davantage de place. "
        "Les deux enquetes revelent un axe central oppose : d'un cote les profils alimentaires-logement, souvent plus modestes et plus ruraux ; "
        "de l'autre les profils plus aises, plus urbains et plus diversifies, avec davantage de sante, transport, communication et loisirs. "
        "Le DMM capte donc non seulement des differences de structure budgetaire, mais aussi une stratification economique sous-jacente."
    )
    lines.append("")
    lines.append(
        "La solution K=6 est particulierement utile parce qu'elle evite deux ecueils : elle n'ecrase pas les comportements dans une opposition trop generale "
        "comme K=2 ou K=3, et elle evite la multiplication de micro-profils des solutions K=8 ou K=9. Elle donne une segmentation suffisamment expressive "
        "pour decrire les comportements des menages, tout en restant defendable statistiquement et economiquement."
    )
    return "\n".join(lines)


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def docx_paragraph(text="", style=None):
    text = escape(str(text))
    ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f'<w:p>{ppr}<w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'


def docx_code(text):
    text = escape(str(text))
    return (
        '<w:p><w:pPr><w:pStyle w:val="Code"/></w:pPr>'
        '<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>'
        '<w:sz w:val="17"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
    )


def make_docx(md_text):
    out = []
    in_code = False
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.startswith("|"):
            out.append(docx_code(line))
        elif not line.strip():
            out.append(docx_paragraph(""))
        elif line.startswith("# "):
            out.append(docx_paragraph(line[2:], "Title"))
        elif line.startswith("## "):
            out.append(docx_paragraph(line[3:], "Heading1"))
        elif line.startswith("### "):
            out.append(docx_paragraph(line[4:], "Heading2"))
        elif line.startswith("#### "):
            out.append(docx_paragraph(line[5:], "Heading3"))
        elif line.startswith("- "):
            out.append(docx_paragraph("• " + line[2:]))
        else:
            out.append(docx_paragraph(line.replace("`", "")))

    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:body>'
        + "".join(out)
        + '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        + '<w:pgMar w:top="1440" w:right="1080" w:bottom="1440" w:left="1080"/>'
        + "</w:sectPr></w:body></w:document>"
    )
    styles_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="21"/></w:rPr><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="34"/></w:rPr><w:pPr><w:spacing w:after="300"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:pPr><w:spacing w:before="360" w:after="180"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="24"/></w:rPr><w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="22"/></w:rPr><w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Code"><w:name w:val="Code"/><w:basedOn w:val="Normal"/><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="17"/></w:rPr><w:pPr><w:spacing w:after="0"/></w:pPr></w:style>
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
