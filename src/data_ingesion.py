import pandas as pd
import os

RAW_DATA = "data/raw/Housing.csv"
PROCESSED_DATA = "data/processed/data.csv"

def process_data():
    df = pd.read_csv(RAW_DATA)

    # Encode yes/no
    yes_no_cols = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]
    for col in yes_no_cols:
        df[col] = df[col].map({"yes": 1, "no": 0})

    # Encode furnishingstatus
    df["furnishingstatus"] = df["furnishingstatus"].map({
        "furnished": 2,
        "semi-furnished": 1,
        "unfurnished": 0
    })

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA, index=False)

if __name__ == "__main__":
    process_data()
