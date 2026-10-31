# Household Consumption Structure in Morocco: Integrated Econometric Approaches and Household Typology

Applied economics and statistics project analysing how Moroccan households allocate their budgets, using the two national household surveys **ENNVM 2007** and **ENCDM 2014** (HCP). Three complementary approaches are combined: a demand system (LES), a multilevel Working–Leser model, and Dirichlet mixture models for latent consumption profiles.

*Résumé (FR) : étude de la structure de consommation des ménages marocains (2007 et 2014) par trois approches complémentaires : système de dépenses linéaire (LES, GAMS), modèle de Working–Leser multiniveau (Stata) et modèles de mélange de Dirichlet (DMM / DPMM, Python). Les rapports techniques détaillés sont en français dans `dirichlet/outputs/rapports/`.*

---

## Research question

To what extent are household consumption behaviours determined by expenditure level, territorial context and socio-demographic characteristics, and how can the heterogeneity of these behaviours be modelled rigorously?

## Approach

| Block | Tool | What it does |
|---|---|---|
| **Budget shares** | Python | Household budget shares at two levels of detail: **9 aggregate categories** (G1–G9) and **23 sub-categories** (S1–S23). Zeros are replaced by ε = 10⁻⁶ and rows renormalised, because the Dirichlet distribution needs strictly positive shares. |
| **1. Linear Expenditure System (LES)** | Stata + GAMS | Regresses category spending on total spending by sub-population (sex of household head, urban / rural, region) to get α and β. A linear system solved in GAMS recovers the **minimum (subsistence) consumption** per category, then income and own-price elasticities. LES is used because the surveys record spending values, not prices and quantities. |
| **2. Working–Leser multilevel model** | Stata | Budget share regressed on centred log-expenditure and its square, plus household controls (size, share of children and of active members, age, sex, education and activity of the head). Households are grouped by **region × area**, with a random intercept and a random slope on expenditure (model **M6**, chosen out of 11 specifications with AIC / BIC). ICCs and random effects measure how territorial each category is. Diagnostics: VIF, Breusch–Pagan, White, RESET, Cook's distance. |
| **3. Dirichlet mixture models** | Python (NumPy, SciPy, scikit-learn, PyMC, ArviZ) | **DMM**: finite mixture fitted by EM with k-means initialisation, K = 2…9. **DPMM**: truncated Dirichlet-process mixture (K_max = 7, stick-breaking, NUTS sampler, prior-sensitivity analysis on the concentration parameter). Profiles are interpreted afterwards against socio-economic variables. |
| **Descriptive analysis** | Python | Sample structure, household size, education, expenditure distribution, Lorenz curve, budget structure by year. |

## Main findings

- **Engel's law holds.** The food share falls from 40.9 % (2007) to 37.3 % (2014) but food remains the first budget item. Per-person expenditure is unequal (Gini 0.428 in 2007, 0.416 in 2014).
- **Hierarchy of goods (LES).** Food and housing–energy are necessities (income elasticity < 1; food 0.73 rural vs 0.51 urban in 2007). Transport, communication, leisure, education, financial services and private transport are strongly income-sensitive (elasticities well above 1; transport–communication about 2.5 in 2007). Price elasticities are larger in absolute value in rural areas.
- **Territory matters, unevenly (multilevel).** Housing is the most territorialised sub-category (ICC 0.26 in 2007), followed by hygiene, fruit and vegetables, and water–energy. Many other categories depend more on household characteristics than on location.
- **Latent consumption profiles (DMM / DPMM).** Fitting criteria keep improving up to K = 9, but finer solutions create tiny, ambiguous groups. **K = 6 is the best compromise** in both surveys: a constrained essentials profile, a housing profile, a health-constrained profile, an affluent mobile profile, an intermediate profile and a diversified profile. DMM and DPMM recover the same budget logics, and the profiles line up with expenditure level, urban / rural location, household size and education.
- **Limits stated in the report:** no price data, so price elasticities are structural rather than observed; the LES cannot represent inferior goods; no formal Hausman / Mundlak test for the multilevel model; an AIDS extension was tried but gave unstable price elasticities and is not included here.

## Repository layout

```
dirichlet/
  matrix_creation/     budget-share matrices (9 and 23 categories, per survey)
  DMM/                 finite Dirichlet mixture (EM)
  DPMM/                Bayesian Dirichlet process mixture (NUTS)
  Diagnostics/         alpha / convergence / K diagnostics
  Visualisations/      figures (radar profiles, fragmentation, stability, ...)
  scripts/             weighted profiles, diagnostic reports
  outputs/
    rapports/          method and results reports (.md / .docx, in French)
    reports/           alpha diagnostic summaries (.csv / .pdf)
    tables/            cluster profiles, alphas, summaries, prior comparisons
    figures/           PNG and PDF figures
GAMS/                  LES models (*.gms) and elasticity tables (*.xlsx)
Multiniveau/           Stata multilevel model selection and diagnostics (tables)
Résultats_Stata/       Stata regression tables by area, region and sex of head
graphiques_echantillon/   descriptive charts of the survey samples
DATAGAMS.xlsx          aggregated inputs for the GAMS models
```

Method details (equations, algorithms, libraries) are in [rapport_procedure_DMM_DPMM.md](dirichlet/outputs/rapports/rapport_procedure_DMM_DPMM.md). Survey-weighted K = 6 profiles are in [dirichlet/outputs/tables/profils_ponderees_K6/](dirichlet/outputs/tables/profils_ponderees_K6/).

## Reproducing the analysis

The microdata are **not included** (see below), so the pipeline can only be re-run with your own copy of the HCP files.

```bash
python -m venv .venv
.venv\Scripts\activate                 # Windows
pip install -r requirements.txt

# place the cleaned household files in dirichlet/data/raw/, then:
python dirichlet/matrix_creation/matrice_encdm_9.py     # budget-share matrix
python dirichlet/DMM/dmm_encdm_9.py                     # finite mixture, K = 2..9
python dirichlet/DPMM/dpmm_encdm_9.py                   # Bayesian mixture (long run)
python dirichlet/scripts/compute_weighted_k6_profiles.py
```

Scripts exist for each survey (`encdm` = 2014, `ennvm` = 2007) and each level of detail (`_9`, `_23`). Paths are set at the top of each script. The LES (GAMS) and multilevel (Stata) steps need GAMS and Stata licences; run the `.gms` files from inside the `GAMS/` folder (they read the `GAMS_*.xlsx` files next to them).

## Data

Anonymised microdata and nomenclatures come from the HCP and are **not redistributed** here (`BDD/`, `dirichlet/data/`, household-level membership tables are excluded):

- ENNVM 2006–2007: <https://www.hcp.ma/Enquete-Nationale-sur-les-niveaux-de-vie-des-Menages-ENNVM-2007_a2948.html>
- ENCDM 2013–2014: <https://www.hcp.ma/Enquete-Nationale-sur-la-Consommation-et-les-Depenses-des-Menages-ENCDM-2014_a2946.html>

Everything published here is code or aggregated output (profiles, summaries, figures, regression and elasticity tables).

## References

Third-party references that underpin the work are cited, not republished:

1. Ait Faraji, S. (2023). *Estimation of LES Consumption Elasticity for Morocco*. GEAS3D.
2. Annabi, N., Cockburn, J., & Decaluwé, B. (2003). *Formes fonctionnelles et paramétrisation dans les MCEG*. Université Laval.
3. Deaton, A., & Muellbauer, J. (1980); Banks, J., Blundell, R., & Lewbel, A. (1997); Leser, C. E. V. (1963): demand systems and Engel curves.
4. Pal, S., & Heumann, C. (2022). Clustering compositional data using Dirichlet mixture model. *PLOS ONE*, 17(5).
5. Müller, P., & Mitra, R. (2013). Bayesian nonparametric inference: why and how. *Bayesian Analysis*, 8(2).

## Status

**Work in progress.** The analysis is complete for both surveys. The project is meant to be finalised with an **interactive dashboard summarising all the work**: budget structure by year, income and price elasticities, territorial (region × area) effects, and household consumption profiles. It is not built yet.
