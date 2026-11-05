-- SQLite companion to src/etl_pipeline.py, independent of the existing PBIX.
-- Input table: clinical_raw, loaded from data/clinical_data.csv by verify_companion.py.
-- Dates are ISO YYYY-MM-DD as in the bundled CSV. DISTINCT compares ALL raw fields,
-- matching pandas drop_duplicates(), rather than deduplicating by patient_id alone.

CREATE VIEW clinical_clean AS
SELECT DISTINCT
    patient_id, age, gender, injury_type, start_date, end_date, sessions,
    pain_score_initial, pain_score_final, mobility_initial, mobility_final
FROM clinical_raw;

CREATE VIEW clinical_kpis AS
SELECT *,
    CAST(julianday(end_date) - julianday(start_date) AS INTEGER) AS recovery_days,
    pain_score_initial - pain_score_final AS pain_improvement,
    mobility_final - mobility_initial AS mobility_gain,
    CASE WHEN mobility_final - mobility_initial > 20
              AND pain_score_initial - pain_score_final > 2
         THEN 1 ELSE 0 END AS success
FROM clinical_clean;

CREATE VIEW injury_type_summary AS
SELECT injury_type,
    COUNT(*) AS record_count,
    AVG(recovery_days) AS avg_recovery_days,
    AVG(sessions) AS avg_sessions,
    AVG(pain_improvement) AS avg_pain_improvement,
    AVG(mobility_gain) AS avg_mobility_gain,
    SUM(success) AS successful_records,
    100.0 * AVG(success) AS success_rate_pct
FROM clinical_kpis
GROUP BY injury_type;
