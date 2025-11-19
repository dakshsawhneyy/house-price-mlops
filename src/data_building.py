import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yaml
import os

DATA_PATH = "data/processed/data.csv"
PARAMS_PATH = "params.yml"
MODEL_PATH = "models/model.pkl"


def train_model():
    # Load parameters (optional but production-style)
    with open(PARAMS_PATH, "r") as f:
        params = yaml.safe_load(f)

    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["price"])    # features
    y = df["price"]                   # target

    # Split the data
    test_size = params["train"]["test_size"]
    random_state = params["train"]["random_state"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state
    )

    # Train a simple model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save model
    os.makedirs("models", exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
