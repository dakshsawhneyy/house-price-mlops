import pandas as pd
import json
import os
from evidently.report import Report
from evidently.metrics import DataDriftPreset
from evidently.metrics import DataQualityPreset
from evidently.metrics import TargetDriftPreset

# ---- Paths ----
REFERENCE_DATA = "data/processed/data.csv"          # Training data
PRODUCTION_DATA = "drift/production_sample.csv"     # Mocked live data
REPORT_HTML = "reports/drift_report.html"
REPORT_JSON = "reports/drift_metrics.json"


def run_drift_check():
    # Load Data
    reference_df = pd.read_csv(REFERENCE_DATA)
    production_df = pd.read_csv(PRODUCTION_DATA)

    # Create Report
    report = Report(metrics=[
        DataDriftPreset(),
        DataQualityPreset(),
        TargetDriftPreset()
    ])

    report.run(
        reference_data=reference_df,
        current_data=production_df
    )

    # Save HTML report
    os.makedirs("reports", exist_ok=True)
    report.save_html(REPORT_HTML)

    # Save metrics JSON
    metrics = report.as_dict()
    with open(REPORT_JSON, "w") as f:
        json.dump(metrics, f, indent=4)

    # Print simple decision
    drift = metrics["metrics"][0]["result"]["dataset_drift"]

    if drift:
        print("🚨 Data Drift Detected!")
    else:
        print("✅ No Drift Detected.")

    return drift


if __name__ == "__main__":
    run_drift_check()
