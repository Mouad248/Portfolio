# Clinical KPI Dashboard

A personal reporting project focused on rehabilitation indicators, using Python,
pandas and a supplied Power BI report. The bundled data contains 10 synthetic
records, not real patients. The separately added [SQLite companion](../sql/README.md)
is verified against Python and is not claimed to power the existing PBIX.

[Case study](../CASE_STUDY.md) · [Gallery](../screenshots/README.md) ·
[Implementation evidence and verification limits](../../portfolio-guide/BI_IMPLEMENTATION.md)

Model relationships, embedded DAX, Power Query steps and source bindings have not
been independently inspected inside the PBIX. Descriptions below are documentation,
not evidence of a verified semantic model or successful refresh.

## Project Overview

This project simulates a real-world healthcare analytics workflow, including:

- Clinical data ingestion
- Data cleaning and validation
- KPI creation (pain reduction, mobility gain, recovery time, success rate)
- Exploratory data analysis
- Dashboard development in Power BI
- Data storytelling for clinical decision support

The goal is to demonstrate how a Healthcare Data Analyst can convert patient data into meaningful insights for clinicians, administrators, and rehabilitation teams.

## Dashboard Features

### 1. Clinical Overview
- Average recovery time
- Rehabilitation success rate
- Average number of sessions
- Mean pain reduction
- Mean mobility gain

### 2. Injury Type Analysis
- Recovery time by injury type
- Success rate by injury type
- Pain improvement distribution
- Mobility gain comparison

### 3. Patient Evolution
- Pain score progression
- Mobility progression
- Individual patient outcome trends

### 4. Sessions Efficiency
- Relationship between number of sessions and recovery time
- Efficiency indicators
- Outlier detection

## Dataset Description

The dataset is a synthetic clinical dataset created for educational and portfolio purposes. It contains anonymized, simulated patient rehabilitation data with the following fields:

| Column | Description |
|--------|-------------|
| patient_id | Unique patient identifier |
| age | Patient age |
| gender | M/F |
| injury_type | Type of injury (muscle, joint, ligament, etc.) |
| start_date | Rehabilitation start date |
| end_date | Rehabilitation end date |
| sessions | Number of therapy sessions |
| pain_score_initial | Initial pain score (0–10) |
| pain_score_final | Final pain score (0–10) |
| mobility_initial | Initial mobility score (0–100) |
| mobility_final | Final mobility score (0–100) |

## Data Processing (Python)

The project includes a Python ETL pipeline that performs:

- Duplicate removal
- Date conversion
- KPI calculations
- Success flag creation
- Export of cleaned dataset

Example code snippet:

```python
import pandas as pd

df = pd.read_csv("clinical_data.csv")

df = df.drop_duplicates()

df["start_date"] = pd.to_datetime(df["start_date"])
df["end_date"] = pd.to_datetime(df["end_date"])

df["recovery_days"] = (df["end_date"] - df["start_date"]).dt.days
df["pain_improvement"] = df["pain_score_initial"] - df["pain_score_final"]
df["mobility_gain"] = df["mobility_final"] - df["mobility_initial"]

df["success"] = (df["mobility_gain"] > 20) & (df["pain_improvement"] > 2)
```

## SQL Transformations

The snippet below is the original illustrative SQL Server-style example, not an
executable SQLite script or proof of the PBIX data source. The new
[runnable SQLite views](../sql/clinical_kpis.sql) also implement full-row duplicate
removal and injury-type aggregates; [run the comparison](../sql/README.md) to check
them against the original Python functions.

- This illustrative snippet describes:
- KPI calculations
- An injury-type field for subsequent grouping
- Success classification

```SQL
SELECT
    patient_id,
    injury_type,
    DATEDIFF(day, start_date, end_date) AS recovery_days,
    (pain_score_initial - pain_score_final) AS pain_improvement,
    (mobility_final - mobility_initial) AS mobility_gain,
    sessions,
    CASE 
        WHEN (mobility_final - mobility_initial) > 20 
         AND (pain_score_initial - pain_score_final) > 2
        THEN 1 ELSE 0
    END AS success
FROM clinical_data;
```

## Power BI Dashboard
The Power BI file (dashboard.pbix) includes:

- KPI cards
- Bar charts
- Line charts
- Scatter plots
- Filters by injury type, gender, and age

It provides a clear visual summary of patient outcomes and rehabilitation performance.

## Data Storytelling
The current bundled CSV, evaluated through the existing Python ETL and the SQLite
companion, gives 33.30 average recovery days, 4.00 average pain improvement, 25.60
average mobility gain, 13.70 average sessions and 100% rule-based success.

An earlier narrative in this document quoted 18% faster recovery, 3.2 pain
improvement, 28 mobility gain and 72% success, and made predictive statements.
Those claims are not supported by the current verification and should not be used
as portfolio findings. See [existing issues](../../portfolio-guide/EXISTING_ISSUES.md).

The synthetic sample supports a demonstration of calculations and presentation,
not causal conclusions or evidence of clinical effectiveness.

## Repository Structure

```
clinical-kpi-dashboard/
│
├── data/
│   ├── clinical_data.csv
│   └── README.md
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── analysis.ipynb
│   └── visualizations.ipynb
│
├── powerbi/
│   └── dashboard.pbix
│
├── src/
│   └── etl_pipeline.py
│
├── README.md
└── LICENSE
```
 
## License
This project is released under the MIT License, allowing free use and adaptation for educational and professional purposes.
