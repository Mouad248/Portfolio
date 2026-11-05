# SQLite companion: clinical KPI definitions

This separate portfolio addition reproduces the definitions in the existing
[Python ETL](../src/etl_pipeline.py). **It is not claimed to power the existing
Power BI report.** No standalone SQL file was found before this companion was added;
the older technical README contained only an illustrative SQL snippet.

## Run and verify

From this project's root, use Python with pandas and numpy installed (the existing
ETL imports both). SQLite is included with Python; no database server is needed.

```powershell
python sql/verify_companion.py
```

The default run uses an in-memory database and leaves the CSV and existing outputs
untouched. To retain an inspectable database, choose a **new** destination:

```powershell
python sql/verify_companion.py --database clinical_companion.sqlite
```

Existing database files are refused. The saved database contains `clinical_raw`
and three views defined in [clinical_kpis.sql](clinical_kpis.sql):

| View | Definition |
| --- | --- |
| `clinical_clean` | Full-row `SELECT DISTINCT`, matching `drop_duplicates()`; not deduplication by patient ID |
| `clinical_kpis` | End date minus start date in days; initial minus final pain; final minus initial mobility; success when mobility gain **> 20 AND** pain improvement **> 2** |
| `injury_type_summary` | Row count, average recovery days/sessions/pain improvement/mobility gain, successful row count and success percentage by injury type |

For example, query a retained database with Python's standard library:

```powershell
python -c "import sqlite3; c=sqlite3.connect('clinical_companion.sqlite'); print(c.execute('SELECT * FROM injury_type_summary ORDER BY injury_type').fetchall())"
```

## Verification and scope

[verify_companion.py](verify_companion.py) imports and calls the original
`clean_data` and `calculate_kpis` functions. It compares every resulting column and
all injury-type aggregates with SQLite, ignoring row order and storage dtype.
It also checks an in-memory fixture with exact duplicates, differing rows sharing
an ID, equality at each success threshold, a passing case, missing pain, leap-day
dates and a negative recovery interval.

The companion accepts the bundled CSV's non-null ISO `YYYY-MM-DD` dates. Its date
arithmetic is not presented as equivalent for arbitrary timestamps or mixed date
formats. It retains negative intervals to match the existing ETL; it does not add
clinical validity rules. A null score fails the success condition, as in Python.

The bundled dataset has **10 synthetic rows**. These are demonstration KPIs, not
clinical evidence; “success” is a project rule, not a validated treatment outcome.
See the [case study](../CASE_STUDY.md), [gallery](../screenshots/README.md) and
[evidence index](../../portfolio-guide/BI_IMPLEMENTATION.md).
