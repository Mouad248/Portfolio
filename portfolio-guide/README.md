# Repository guide

[Portfolio and project navigator](../README.md#start-here)

## Folder layout

```text
Portfolio/
├── README.md                       Start here: services and featured work
├── Consommation_Maroc/              Household consumption research
├── Actuariat_dashboard/             Reinsight: React/FastAPI dashboard
├── northpeak-fpna-main/             SaaS financial BI and forecasting
├── Clinical-KPI-Dashboard-main/      Healthcare reporting and SQL companion
├── portfolio-guide/                           Shared evidence and review notes
└── maintenance/                       Maintenance helpers and optional demo sources
```

The original project names and internal source/output paths are retained. Each
project has the same three reader entry points:

| File | Purpose |
| --- | --- |
| `README.md` | Overview, technology and local run instructions |
| `CASE_STUDY.md` | Problem, contribution, deliverables, decision and limitations |
| `screenshots/README.md` | Indexed images and their provenance |

Start with these files before exploring the detailed code, data or generated
outputs. Galleries link original figures in place, avoiding extra image copies.

## Shared reference

- [BI implementation evidence](BI_IMPLEMENTATION.md): model documentation, existing
  DAX examples, ETL, refresh and validation links, including verification limits.
- [Existing issues](EXISTING_ISSUES.md): reporting discrepancies and application
  observations kept separate from the client-facing case studies.
- [Support folder guide](../maintenance/README.md): optional scripts and browser-demo sources.

## Maintenance

Run these from the portfolio root when changing the corresponding material:

```powershell
python maintenance/scripts/check_portfolio_docs.py
python Clinical-KPI-Dashboard-main/sql/verify_companion.py
```

The first checks local documentation links and anchors. The second compares the
Clinical SQL companion against the original Python definitions; it requires pandas
and numpy. Neither command publishes anything.
