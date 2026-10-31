"""
ETL Pipeline for Clinical KPI Dashboard

This script performs:
- Data ingestion
- Data cleaning
- KPI calculations
- Clinical metric generation
- Export of cleaned dataset

The dataset is synthetic and safe for public use.
"""

import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    """Load raw clinical dataset."""
    print(f"Loading dataset from: {path}")
    df = pd.read_csv(path)
    print(f"Dataset loaded. Shape: {df.shape}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and validate clinical dataset."""
    print("Cleaning dataset...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert dates
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"])

    print("Cleaning completed.")
    return df


def calculate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Generate clinical KPIs."""
    print("Calculating KPIs...")

    df["recovery_days"] = (df["end_date"] - df["start_date"]).dt.days
    df["pain_improvement"] = df["pain_score_initial"] - df["pain_score_final"]
    df["mobility_gain"] = df["mobility_final"] - df["mobility_initial"]

    df["success"] = (df["mobility_gain"] > 20) & (df["pain_improvement"] > 2)

    print("KPIs calculated.")
    return df


def export_data(df: pd.DataFrame, path: str):
    """Export cleaned dataset."""
    df.to_csv(path, index=False)
    print(f"Cleaned dataset exported to: {path}")


def run_pipeline():
    """Run full ETL pipeline."""
    print("Starting ETL pipeline...")

    raw_path = "../data/clinical_data.csv"
    export_path = "../data/clinical_data_cleaned.csv"

    df = load_data(raw_path)
    df = clean_data(df)
    df = calculate_kpis(df)
    export_data(df, export_path)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
