import pandas as pd
import json
import os
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab, DataQualityTab

# ---- Paths ----
REFERENCE_DATA = "data/processed/data.csv"          # Training data
PRODUCTION_DATA = "drift/production_sample.csv"     # Mocked live data
REPORT_HTML = "reports/drift_report.html"


def run_drift_check():
    # Load Data
    reference_df = pd.read_csv(REFERENCE_DATA)
    production_df = pd.read_csv(PRODUCTION_DATA)

    # Create Dashboard
    dashboard = Dashboard(tabs=[
        DataDriftTab(),
        DataQualityTab()
    ])

    dashboard.calculate(
        reference_df,
        production_df
    )

    # Save HTML report
    os.makedirs("reports", exist_ok=True)
    dashboard.save(REPORT_HTML)

    # Simple drift check based on column comparison
    drift_detected = False
    try:
        # Check if columns match
        if set(reference_df.columns) != set(production_df.columns):
            drift_detected = True
        # Check basic statistics
        elif (production_df.describe() - reference_df.describe()).abs().max().max() > 1.0:
            drift_detected = True
    except Exception:
        drift_detected = False

    if drift_detected:
        print("🚨 Data Drift Detected!")
    else:
        print("✅ No Drift Detected.")

    return drift_detected


if __name__ == "__main__":
    run_drift_check()
