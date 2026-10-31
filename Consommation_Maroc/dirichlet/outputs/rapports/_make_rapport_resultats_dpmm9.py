from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "rapport_resultats_DPMM_9postes_2007_2014.md"
DOCX_PATH = ROOT / "rapport_resultats_DPMM_9postes_2007_2014.docx"

POSTS = [f"w_G{i}" for i in range(1, 10)]
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

PRIORS = ["gamma_1_1", "gamma_1_2", "gamma_0p5_2", "gamma_0p25_2"]

CASES = {
    "ENNVM 2007": {
        "prefix": "ennvm_2007_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain",
        "tables": Path("outputs/tables/dpmm_ennvm_9"),
        "processed": Path("data/processed/ennvm_2007_parts_budgetaires.xlsx"),
        "diag": Path("outputs/analysis_dpmm_ennvm_9/ENNVM_2007_DPMM_9postes_diagnostic.xlsx"),
        "preferred": "gamma_1_1",
    },
    "ENCDM 2014": {
        "prefix": "encdm_2014_dpmm_nuts_full_9_Kmax7_orderedG1_singlechain",
        "tables": Path("outputs/tables/dpmm_encdm_9"),
        "processed": Path("data/processed/encdm_2014_parts_budgetaires.xlsx"),
        "diag": Path("outputs/analysis_dpmm_encdm_9/ENCDM_2014_DPMM_9postes_diagnostic.xlsx"),
        "preferred": "gamma_0p25_2",
    },
}


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def global_mean(cfg):
    df = pd.read_excel(cfg["processed"], usecols=POSTS)
    return df[POSTS].mean()


def read_prior_summary(cfg):
    return pd.read_excel(cfg["diag"], sheet_name="01_prior_summary")


def read_cluster_summary(cfg):
    return pd.read_excel(cfg["diag"], sheet_name="02_cluster_summary")


def read_overview(cfg):
    return pd.read_excel(cfg["diag"], sheet_name="10_prior_overview")


def read_profiles(cfg, prior):
    return pd.read_excel(cfg["tables"] / f"{cfg['prefix']}_{prior}_profiles_full.xlsx")


def behavioral_label(row, gm):
    vals = row[POSTS].astype(float)
    diff = vals - gm
    if vals["w_G6"] >= 0.23:
        return "Sante tres elevee"
    if vals["w_G9"] >= 0.18:
        return "Loisirs/culture extreme"
    if vals["w_G8"] >= 0.18:
        return "Communication extreme"
    if vals["w_G7"] >= 0.16:
        return "Transport tres eleve"
    if vals["w_G6"] >= 0.13 and vals["w_G7"] >= 0.07:
        return "Sante-transport aise"
    if diff["w_G3"] >= 0.06 and diff["w_G1"] >= 0.02:
        return "Alimentation-logement"
    if diff["w_G1"] >= 0.05 and vals["w_G8"] <= 0.015:
        return "Alimentation dominante, communication faible"
    if diff["w_G8"] >= 0.04:
        return "Communication elevee"
    if diff["w_G5"] >= 0.025:
        return "Equipement/logement"
    if diff["w_G1"] <= -0.10 and (diff["w_G6"] > 0.04 or diff["w_G7"] > 0.03):
        return "Diversifie hors alimentaire"
    return "Profil intermediaire"


def signature(row, gm):
    vals = row[POSTS].astype(float)
    diff = vals - gm
    dom = vals.sort_values(ascending=False).head(3)
    high = diff.sort_values(ascending=False).head(3)
    low = diff.sort_values().head(2)
    dom_txt = ", ".join(f"G{c[-1]} {100*v:.1f}%" for c, v in dom.items())
    high_txt = ", ".join(f"G{c[-1]} +{100*d:.1f} pp" for c, d in high.items() if d > 0.005)
    low_txt = ", ".join(f"G{c[-1]} {100*d:.1f} pp" for c, d in low.items() if d < -0.005)
    return dom_txt, high_txt, low_txt


def prior_comparison_table(cfg):
    p = read_prior_summary(cfg)
    c = read_cluster_summary(cfg)
    rows = []
    for _, r in p.iterrows():
        prior = r["prior"]
        cc = c[c["prior"] == prior]
        weights = cc["posterior_weight_mean"]
        shares = cc["assigned_share_full"]
        rows.append([
            prior,
            int(r["K_MAX"]),
            f"{r['alpha_dp_mean']:.3f}",
            int(r["occupied_weight_gt_1pct"]),
            int((weights >= 0.02).sum()),
            int((weights >= 0.03).sum()),
            f"{100*shares.min():.1f}%",
            int(cc["assigned_size_full"].min()),
            f"{r['mean_max_prob_full']:.3f}",
            f"{100*r['share_ambiguous_full_lt_0_60']:.1f}%",
            int(r["n_divergences"]),
        ])
    return md_table(
        ["Prior", "K_MAX", "alpha_DP moy.", "K eff >1%", "K eff >2%", "K eff >3%", "Plus petit cluster", "n min", "Prob. max moy.", "Ambigus", "Divergences"],
        rows,
    )


def cluster_summary_table(cfg, prior):
    c = read_cluster_summary(cfg)
    cc = c[c["prior"] == prior].copy()
    rows = []
    for _, r in cc.iterrows():
        rows.append([
            f"C{int(r['cluster'])}",
            f"{100*r['posterior_weight_mean']:.1f}%",
            f"{int(r['assigned_size_full'])} ({100*r['assigned_share_full']:.1f}%)",
            f"{r['phi_mean']:.1f}",
            f"{100*r['mean_G1_theoretical']:.1f}%",
            "oui" if r["weight_gt_1pct"] else "non",
        ])
    return md_table(["Cluster", "Poids posteriori", "Affectes", "phi", "G1 theorique", ">1%"], rows)


def profile_table(cfg, prior, gm, compact=False):
    prof = read_profiles(cfg, prior)
    total = prof["cluster_size"].sum()
    rows = []
    if compact:
        headers = ["Cluster", "Taille", "Libelle", "Postes dominants", "Sur-representations", "Sous-representations"]
        for _, r in prof.iterrows():
            dom, high, low = signature(r, gm)
            rows.append([
                f"C{int(r['cluster_dpmm_nuts'])}",
                f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
                behavioral_label(r, gm),
                dom,
                high,
                low,
            ])
    else:
        headers = ["Cluster", "Taille", "Libelle", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
        for _, r in prof.iterrows():
            rows.append([
                f"C{int(r['cluster_dpmm_nuts'])}",
                f"{int(r['cluster_size'])} ({100*r['cluster_size']/total:.1f}%)",
                behavioral_label(r, gm),
                *[f"{100*r[c]:.1f}" for c in POSTS],
            ])
    return md_table(headers, rows)


def overview_table(cfg):
    ov = read_overview(cfg)
    rows = []
    for _, r in ov.iterrows():
        rows.append([
            r["prior"],
            f"{r['mean_max_prob_full']:.3f}",
            f"{100*r['share_ambiguous_full_lt_0_60']:.1f}%",
            f"{100*r['min_cluster_share']:.1f}%",
            int(r["min_cluster_size"]),
            int(r["n_small_share_lt_1pct"]),
            int(r["n_small_size_lt_100"]),
            f"{r['eta2_DAM']:.3f}",
            f"{r['eta2_log_DAM']:.3f}",
            str(r["top_qualitative_associations"]).replace("|", "/"),
        ])
    return md_table(
        ["Prior", "Prob. max", "Ambigus", "Part min", "n min", "Small <1%", "n<100", "eta2 DAM", "eta2 log_DAM", "Associations dominantes"],
        rows,
    )


def k_context_table(cfg, prior):
    q = pd.read_excel(cfg["diag"], sheet_name="08_quant_by_cluster")
    dam = q[(q["prior"] == prior) & (q["variable"] == "DAM")][
        ["cluster", "n", "mean", "median", "relative_delta_mean_vs_global"]
    ]
    d = pd.read_excel(cfg["diag"], sheet_name="06_crosstab_delta")
    milieu = d[(d["prior"] == prior) & (d["variable"] == "Milieu")]
    quint = d[(d["prior"] == prior) & (d["variable"] == "quintile_DAM")]
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


def global_structure(cfg):
    gm = global_mean(cfg)
    rows = [[f"G{i}", POST_LABELS[f"w_G{i}"], f"{100*gm[f'w_G{i}']:.1f}%"] for i in range(1, 10)]
    return md_table(["Poste", "Libelle", "Part moyenne"], rows)


def case_section(case, cfg):
    gm = global_mean(cfg)
    preferred = cfg["preferred"]
    lines = [f"## {case} - resultats DPMM 9 postes", ""]
    lines += ["### Structure moyenne de reference", "", global_structure(cfg), ""]
    lines += ["### Comparaison des priors et nombre effectif de clusters", "", prior_comparison_table(cfg), ""]
    if case == "ENNVM 2007":
        lines.append(
            "Lecture : tous les priors utilisent formellement les 7 composantes de la troncature au seuil de 1%, "
            "mais certains produisent un petit cluster autour de 1% a 2%. La solution est donc mieux interpretee comme "
            "un K effectif de 6 a 7. Le prior gamma_1_1 donne la classification la plus nette, mais avec un petit groupe "
            "de 73 menages ; gamma_0p5_2 donne des groupes plus equilibres mais une ambiguite plus elevee. Pour la presentation, "
            "gamma_1_1 est retenu comme lecture principale, avec la reserve que son cluster C7 est un profil rare."
        )
    else:
        lines.append(
            "Lecture : le cas 2014 montre plus clairement le debat entre K=6 et K=7 effectifs. gamma_0p5_2 indique seulement "
            "6 clusters au seuil de poids posteriori de 1%, tandis que gamma_1_1 et gamma_1_2 gardent un petit groupe proche de 1%. "
            "gamma_0p25_2 offre le meilleur compromis de qualite d'affectation et de tailles non minuscules. Il est donc retenu "
            "comme lecture principale, avec K effectif proche de 7 mais une lecture conservatrice possible a 6."
        )
    lines += ["", "### Diagnostic socio-economique global par prior", "", overview_table(cfg), ""]
    lines += [f"### Lecture principale des profils : {preferred}", "", "#### Tailles, poids et concentration", "", cluster_summary_table(cfg, preferred), ""]
    lines += ["#### Profils budgetaires detailles", "", profile_table(cfg, preferred, gm, compact=False), ""]
    lines += ["#### Caracterisation socio-economique", "", k_context_table(cfg, preferred), ""]
    lines += ["### Sensibilite des profils aux priors", ""]
    for prior in PRIORS:
        lines += [f"#### {prior}", "", profile_table(cfg, prior, gm, compact=True), ""]
    lines += ["### Annexe numerique : profils complets par prior", ""]
    for prior in PRIORS:
        lines += [f"#### Profils numeriques - {prior}", "", profile_table(cfg, prior, gm, compact=False), ""]
    return "\n".join(lines)


def build_markdown():
    lines = ["# Rapport detaille des resultats DPMM - 9 postes, ENNVM 2007 et ENCDM 2014", ""]
    lines.append(
        "Ce rapport analyse les resultats du Dirichlet Process Mixture Model tronque applique aux matrices de parts budgetaires en 9 postes. "
        "Contrairement au DMM fini, le DPMM ne choisit pas directement un K fixe : il utilise une troncature K_MAX=7, puis le nombre effectif "
        "de groupes est lu a partir des poids posteriori, des tailles affectees et de la stabilite comportementale des profils."
    )
    lines += ["", "## Libelles des 9 postes", ""]
    rows = [[f"G{i}", POST_LABELS[f"w_G{i}"]] for i in range(1, 10)]
    lines.append(md_table(["Poste", "Libelle"], rows))
    lines += ["", "## Conclusion generale", ""]
    lines.append(
        "Les resultats DPMM sont coherents avec les resultats DMM : les grands comportements recurrents sont les profils alimentaires, "
        "logement, sante, communication, transport et loisirs/culture. La difference principale est que le DPMM exprime cette segmentation "
        "comme une solution tronquee a K_MAX=7, avec parfois des composantes rares. Pour les deux bases, le K effectif comportemental "
        "est plutot compris entre 6 et 7. Une presentation conservatrice peut retenir 6 groupes substantiels ; une presentation plus fine "
        "peut garder 7 groupes en precisant que certains clusters sont rares."
    )
    lines.append("")
    for case, cfg in CASES.items():
        lines.append(case_section(case, cfg))
        lines.append("")
    lines += ["## Synthese comparative 2007-2014", ""]
    lines.append(
        "En 2007, les profils DPMM font ressortir une forte opposition entre profils alimentaires/logement et profils a forte sante ou "
        "communication. Les petits clusters correspondent a des comportements rares mais economiquement lisibles, notamment loisirs/culture "
        "ou sante tres elevee. En 2014, la structure est plus diversifiee : le modele isole plus nettement les comportements de transport, "
        "communication et loisirs/culture, en plus des profils alimentaires et logement. Cela confirme une diversification de la structure "
        "budgetaire entre 2007 et 2014."
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
