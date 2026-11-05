# Existing application and evidence issues

These observations are separate from the documentation work. Application logic,
dependencies, lockfiles, PBIX files and original generated figures were not changed.
This is a focused portfolio review, not a complete application or data audit.

## Clinical reporting

- **Narrative vs. bundled data:** older technical text quoted 72% success, 3.2 pain
  improvement and 28 mobility gain. The current ten-row CSV and original Python
  ETL produce 100%, 4.00 and 25.60 respectively, matching the overview screenshot.
  Those verified values are now prominent, and the old claims are explicitly
  identified as unsupported. No PBIX measure or data binding was inferred from
  the numerical agreement.
- **Limited success variation:** every supplied record passes the project rule.
  The sample cannot support claims of lower success rates for particular injury
  types, population recovery predictions or clinical effectiveness.
- **Relative paths:** [the existing ETL entry point](../Clinical-KPI-Dashboard-main/src/etl_pipeline.py)
  uses `../data/` paths. Running it from the project root fails to find its input;
  documentation now runs it from `src/`. The source code is unchanged.
- **Data-quality scope:** the ETL removes exact duplicate rows and converts dates;
  it does not enforce score ranges, non-negative durations or uniqueness by patient
  ID. The companion intentionally reproduces these definitions instead of silently
  changing them. “Recovery days” measures a recorded interval.
- **Presentation:** the retained overview has a truncated pain-improvement label,
  and some injury-type visuals show counts/sums instead of rates/averages. Their
  titles must be read carefully; the images were not cosmetically altered.

## Reinsight

- **Margin definitions differ between views:** [global KPI calculations](../Actuariat_dashboard/subscription_backend.py)
  set profitability to `100 - combined technical ratio`, including charges.
  `calculate_profitability` used by regional/annual views subtracts claims and
  reserves only. Thus differing “profitability” values are not directly comparable.
- **Some explanatory copy is fixed text:** the
  [profitability page](../Actuariat_dashboard/src/pages/Subscription.tsx) contains
  narrative impact factors alongside calculated values. They do not demonstrate
  measured causal drivers or realised client improvements.
- **Home and roadmap views:** home-page charts contain sample values; investment
  and solvency/IFRS 17 functionality is not claimed as completed. Captures focus on
  the populated profitability and cedant pages.
- **Local origin configuration:** default CORS permits `localhost:8080`, not
  `127.0.0.1:8080`. An initial capture at the latter origin failed with CORS errors;
  using the documented localhost URL worked without source changes.
- **Operational scope:** startup file loading and caches, no database, no
  authentication, no scheduled refresh. Existing frontend test files have no test
  runner script configured in `package.json`.
- **Tooling warning:** Vite emitted an outdated Browserslist/caniuse data warning
  during capture. It did not prevent rendering; dependencies and lockfiles were
  left unchanged.

## NorthPeak and research evidence

- NorthPeak's PBIX measures, formatting and relationships have not been
  independently audited. The [build guide](../northpeak-fpna-main/outputs/DASHBOARD_GUIDE.md)
  is design documentation. Existing screenshots retain some editor chrome and
  inconsistent variance colouring; favorable/unfavorable labels and source sign
  conventions should guide interpretation.
- NorthPeak's accuracy and financial results apply only to its synthetic business
  simulation. The existing reconciliation script is indexed, but the forecasting
  pipeline was not rerun for this documentation task.
- The household study's historical microdata are not supplied for reproduction.
  Models and findings were not re-estimated. The new previews render existing
  PDFs only; no new model validity or current population claims are made.

[Evidence index](BI_IMPLEMENTATION.md) · [Portfolio](../README.md)
