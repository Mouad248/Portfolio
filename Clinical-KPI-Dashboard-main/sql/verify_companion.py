"""Run SQLite views and compare them to the existing, unmodified Python ETL."""
from pathlib import Path
import argparse
import importlib.util
import sqlite3
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SQL = Path(__file__).with_name("clinical_kpis.sql").read_text(encoding="utf-8")
SPEC = importlib.util.spec_from_file_location("clinical_etl", ROOT / "src/etl_pipeline.py")
ETL = importlib.util.module_from_spec(SPEC)
_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    SPEC.loader.exec_module(ETL)
finally:
    sys.dont_write_bytecode = _bytecode_setting


def compare(raw, connection):
    # Scope matches the source CSV: date-only ISO strings. Do not silently claim
    # equivalence for timestamps, mixed date formats, or malformed dates.
    for col in ["start_date", "end_date"]:
        if not raw[col].astype("string").str.fullmatch(r"\d{4}-\d{2}-\d{2}").fillna(False).all():
            raise ValueError("This companion requires non-null ISO YYYY-MM-DD dates")
        pd.to_datetime(raw[col], format="%Y-%m-%d", errors="raise")
    raw.to_sql("clinical_raw", connection, index=False, if_exists="fail")
    connection.executescript(SQL)
    actual = pd.read_sql_query("SELECT * FROM clinical_kpis", connection)
    expected = ETL.calculate_kpis(ETL.clean_data(raw.copy())).reset_index(drop=True)
    for col in ["start_date", "end_date"]:
        actual[col] = pd.to_datetime(actual[col])
    actual["success"] = actual["success"].astype(bool)
    # SQL row order is not a contract; compare the complete rows in canonical order.
    order = list(raw.columns)
    actual = actual.sort_values(order).reset_index(drop=True)
    expected = expected.sort_values(order).reset_index(drop=True)
    pd.testing.assert_frame_equal(actual, expected, check_dtype=False, atol=1e-10, rtol=1e-10)

    summary = pd.read_sql_query("SELECT * FROM injury_type_summary ORDER BY injury_type", connection)
    reference = expected.groupby("injury_type", dropna=False).agg(
        record_count=("patient_id", "size"),
        avg_recovery_days=("recovery_days", "mean"), avg_sessions=("sessions", "mean"),
        avg_pain_improvement=("pain_improvement", "mean"), avg_mobility_gain=("mobility_gain", "mean"),
        successful_records=("success", "sum"), success_rate_pct=("success", lambda s: 100 * s.mean()),
    ).reset_index().sort_values("injury_type").reset_index(drop=True)
    pd.testing.assert_frame_equal(summary, reference, check_dtype=False, atol=1e-10, rtol=1e-10)
    return expected, summary


def boundary_fixture():
    # Include strict threshold boundaries, a passing case, reverse dates, a null
    # score, a leap day and a same-ID/different-row case. No fixture is exported.
    cols = ["patient_id", "age", "gender", "injury_type", "start_date", "end_date", "sessions",
            "pain_score_initial", "pain_score_final", "mobility_initial", "mobility_final"]
    rows = [
        [1, 30, "F", "Test", "2024-02-28", "2024-03-01", 3, 6, 3, 40, 60],
        [2, 30, "F", "Test", "2024-02-28", "2024-03-01", 3, 6, 4, 40, 61],
        [3, 30, "F", "Test", "2024-02-28", "2024-03-01", 3, 6, 3, 40, 61],
        [4, 30, "F", "Other", "2024-03-02", "2024-03-01", 3, 6, 3, 40, 61],
        [5, 30, "F", "Other", "2024-03-01", "2024-03-01", 3, None, 3, 40, 61],
    ]
    rows += [rows[2].copy(), rows[2].copy()]
    rows[-1][6] = 4
    return pd.DataFrame(rows, columns=cols)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, help="Optional new SQLite file; existing files are refused")
    args = parser.parse_args()
    if args.database and args.database.exists():
        parser.error("Choose a new database path; existing files are preserved")
    raw = pd.read_csv(ROOT / "data/clinical_data.csv")
    with sqlite3.connect(str(args.database) if args.database else ":memory:") as connection:
        result, summary = compare(raw, connection)
    print(f"PASS bundled CSV: {len(raw)} input rows -> {len(result)} distinct rows; all columns and injury aggregates match Python")
    print(summary.to_string(index=False))
    print(f"Overall: recovery={result.recovery_days.mean():.2f} days; pain={result.pain_improvement.mean():.2f}; "
          f"mobility={result.mobility_gain.mean():.2f}; success={100 * result.success.mean():.2f}%")
    with sqlite3.connect(":memory:") as connection:
        fixture, _ = compare(boundary_fixture(), connection)
    assert len(fixture) == 6, "One exact duplicate must be removed, but the differing same-ID row retained"
    assert not fixture[fixture.patient_id.isin([1, 2])].success.any(), "Strict thresholds must exclude equality"
    assert fixture[fixture.patient_id == 3].success.all(), "Values above both thresholds must pass"
    assert fixture.loc[fixture.patient_id == 4, "recovery_days"].iloc[0] == -1
    print("PASS boundary fixture: full-row duplicates, strict thresholds, null score, leap day and negative date interval")


if __name__ == "__main__":
    main()
