# BI and analytics implementation evidence

This index separates readable implementation evidence from report artifacts.
**Neither PBIX has been independently inspected internally in this review.** A
screenshot or build guide does not verify embedded DAX, relationships, Power Query
steps, source bindings or successful refresh inside Power BI Desktop.

## Power BI modelling and DAX

| Project | Actual evidence | Scope of the evidence |
| --- | --- | --- |
| NorthPeak | [Build guide: load and model](../northpeak-fpna-main/outputs/DASHBOARD_GUIDE.md#load--model) | Documented long-format model, Calendar relationship and existing DAX examples: `Calendar = CALENDAR(DATE(2024,1,1), DATE(2026,12,31))` and `Value = SUM(dashboard_data[value])`. These are quoted from the guide, not extracted from the PBIX. |
| NorthPeak | [KPI and page specifications](../northpeak-fpna-main/outputs/DASHBOARD_GUIDE.md#page-1---executive-summary), [PBIX artifact](../northpeak-fpna-main/outputs/northpeak_dashboard.pbix), [gallery](../northpeak-fpna-main/screenshots/README.md) | Page designs, filters and screenshots; the annual NRR expression is described in the guide but no complete additional measure is invented here. |
| Clinical | [Technical notes](../Clinical-KPI-Dashboard-main/docs/README_technical.md#power-bi-dashboard), [PBIX artifact](../Clinical-KPI-Dashboard-main/powerbi/dashboard.pbix), [gallery](../Clinical-KPI-Dashboard-main/screenshots/README.md) | Dashboard descriptions and screenshots. No standalone DAX definitions or exported model metadata were found. Python/SQL KPI formulas are not claimed to be the report's embedded DAX. |
| Reinsight | [React page](../Actuariat_dashboard/src/pages/Subscription.tsx), [API calculations](../Actuariat_dashboard/subscription_backend.py), [formula documentation](../Actuariat_dashboard/docs/NOTIONS_ET_FORMULES_REASSURANCE.md) | Web BI implementation, not Power BI or DAX evidence. |
| Household consumption | [Methodology](../Consommation_Maroc/dirichlet/outputs/rapports/rapport_procedure_DMM_DPMM.md), [GAMS model](../Consommation_Maroc/GAMS/2014_9.gms) | Research models and outputs; an interactive summary dashboard remains a stated future step. |

## Preparation, validation and handoff

| Need | Evidence |
| --- | --- |
| Financial data definitions | NorthPeak [dictionary](../northpeak-fpna-main/data/DATA_DICTIONARY.md), [synthetic generator](../northpeak-fpna-main/data/generate_data.py), [loaders](../northpeak-fpna-main/src/utils.py) |
| Financial analysis | [Forecast and backtest](../northpeak-fpna-main/src/forecast.py), [variance](../northpeak-fpna-main/src/variance.py), [scenarios](../northpeak-fpna-main/src/scenarios.py), [dashboard export](../northpeak-fpna-main/src/dashboard.py) |
| Financial controls | [Reconciliation and sanity checks](../northpeak-fpna-main/src/validate.py); compares accounting identities, scenario consistency and backtest behaviour. Not a PBIX audit. |
| Clinical ETL | [Existing Python definitions](../Clinical-KPI-Dashboard-main/src/etl_pipeline.py) and [notebooks](../Clinical-KPI-Dashboard-main/notebooks/) |
| Executable SQL | [SQLite views](../Clinical-KPI-Dashboard-main/sql/clinical_kpis.sql), [Python-vs-SQL verification](../Clinical-KPI-Dashboard-main/sql/verify_companion.py), [run instructions](../Clinical-KPI-Dashboard-main/sql/README.md). This new companion does not claim to power the PBIX. |
| Reinsurance transformations | [Backend](../Actuariat_dashboard/subscription_backend.py): file loading, region/line mappings, treaty/facultative segmentation, premium-weighted ratios and cedant-ranking rules; [API client](../Actuariat_dashboard/src/services/subscriptionService.ts) |
| Research preparation | [Budget-share matrix scripts](../Consommation_Maroc/dirichlet/matrix_creation/), [weighted K=6 summaries](../Consommation_Maroc/dirichlet/scripts/compute_weighted_k6_profiles.py), [diagnostic report script](../Consommation_Maroc/dirichlet/scripts/generate_alpha_diagnostic_report.py) |

## Refresh and reproduce

These are manual instructions, not evidence of an operating scheduled service.

- **NorthPeak:** from its project root, run the forecast, variance, scenarios and
  dashboard scripts, then `python src/validate.py` as listed in the
  [run instructions](../northpeak-fpna-main/README.md#how-to-run).
  Follow the [documented Power BI refresh step](../northpeak-fpna-main/outputs/DASHBOARD_GUIDE.md#refresh).
  Check local CSV paths in Power BI Desktop; the PBIX source bindings and refresh
  have not been tested here. Regeneration can replace generated files.
- **Clinical:** from the project root, the source script's relative paths require
  `cd src`, then `python etl_pipeline.py`, then `cd ..`. This writes the cleaned
  CSV. The [SQLite verifier](../Clinical-KPI-Dashboard-main/sql/README.md) is a
  separate, non-destructive way to check the original definitions. For Power BI,
  inspect the actual source settings in Desktop before selecting Refresh; no
  verified binding to the cleaned CSV is asserted.
- **Reinsight:** follow the [local API/frontend instructions](../Actuariat_dashboard/README.md#run-locally).
  Use `data/demo_dataset.csv.gz` for demonstration. The backend reads its file and
  builds caches at startup; restart it after changing the source, then reload the
  browser. There is no scheduled refresh or database.
- **Household consumption:** follow [reproduction requirements](../Consommation_Maroc/README.md#reproducing-the-analysis).
  Microdata and licensed GAMS/Stata software are prerequisites for the applicable
  steps. This documentation update renders existing figures; it does not rerun
  survey estimation or verify historical findings independently.

## Verification limits and follow-up

The SQL companion was executed against the bundled CSV and boundary fixtures.
Reinsight screenshots are captured from the local frontend backed by its bundled
demo data, after successful API responses and chart rendering. Existing research
and Power BI images are labelled as retained artifacts. See
[existing application and evidence issues](EXISTING_ISSUES.md) for discrepancies.

[Portfolio](../README.md)
