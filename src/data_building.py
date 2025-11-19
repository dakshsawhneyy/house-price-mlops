import pandas as pd
import numpy as np
import pickle
import yaml

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Load params
with open("params.yml", "r") as f:
    params = yaml.safe_load(f)

def train_model():
    df = pd.read_csv("data/processed/data.csv")

    # Target column
    target = params["target"]             # e.g. 'price'
    y = df[target]
    X = df.drop(columns=[target])

    # Identify categorical & numerical columns
    categorical_cols = X.select_dtypes(include=["object"]).columns
    numeric_cols = X.select_dtypes(exclude=["object"]).columns

    # Create preprocessing transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols)
        ]
    )

    # Pipeline (preprocessing + model)
    model_pipeline = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", LinearRegression())
    ])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params["split"], random_state=42
    )

    # Fit
    model_pipeline.fit(X_train, y_train)

    # Save model
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model_pipeline, f)

if __name__ == "__main__":
    train_model()
