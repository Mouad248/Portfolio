from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import figures_interpretation_dirichlet as base


OUT_DIR = base.PROJECT_ROOT / "outputs" / "figures" / "interpretation_dirichlet_sans_textes"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def no_title(*args, **kwargs):
    return None


def clean_figure(fig):
    # Remove only global titles/descriptive text added above the plot area.
    # The graph grammar itself is preserved: axes, panel labels, legends and symbols.
    fig._suptitle = None
    for text in list(fig.texts):
        text.remove()
    return fig


def save(fig, pdf, filename):
    fig = clean_figure(fig)
    fig.savefig(OUT_DIR / filename)
    pdf.savefig(fig)
    plt.close(fig)


def main():
    base.setup_style()
    base.add_title = no_title

    figures = [
        (base.figure_1_k_propagation, "fig_01_propagation_K_DMM9_sans_textes.pdf"),
        (base.figure_2_dmm9_heatmap_k6, "fig_02_profils_DMM9_K6_sans_textes.pdf"),
        (base.figure_3_dmm23_family_heatmap_k7, "fig_03_familles_DMM23_K7_sans_textes.pdf"),
        (base.figure_4_dpmm_prior_sensitivity, "fig_04_sensibilite_priors_DPMM_sans_textes.pdf"),
        (base.figure_5_dpmm23_socio_gradient, "fig_05_gradient_socioeco_DPMM23_sans_textes.pdf"),
    ]

    combined = OUT_DIR / "figures_interpretation_dirichlet_sans_textes.pdf"
    with PdfPages(combined) as pdf:
        for maker, filename in figures:
            fig = maker()
            save(fig, pdf, filename)

    print(combined)
    for _, filename in figures:
        print(OUT_DIR / filename)


if __name__ == "__main__":
    main()
