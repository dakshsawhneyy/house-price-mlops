import pandas as pd
import os

RAW_DATA_PATH = "data/raw/Housing.csv"
PROCESSED_DATA_PATH = "data/processed/data.csv"

def load_and_process():
    # read raw data
    df = pd.read_csv(RAW_DATA_PATH)

    # Basic cleaning (very light)
    df = df.dropna()   # remove missing rows

    # Save processed
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print(f"Processed data saved to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    load_and_process()
