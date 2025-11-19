import pandas as pd
import pickle
import json
from sklearn.metrics import mean_squared_error
import os

DATA_PATH = "data/processed/data.csv"
MODEL_PATH = "models/model.pkl"
METRICS_PATH = "metrics/score.json"


def evaluate_model():
    df = pd.read_csv(DATA_PATH)
    
    X = df.drop(columns=["price"])
    y = df["price"]

    # Load model
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    # Predictions
    preds = model.predict(X)

    # RMSE
    rmse = mean_squared_error(y, preds, squared=False)

    # Save metrics
    os.makedirs("metrics", exist_ok=True)
    with open(METRICS_PATH, "w") as f:
        json.dump({"rmse": rmse}, f, indent=4)

    print(f"RMSE saved to {METRICS_PATH}")


if __name__ == "__main__":
    evaluate_model()
