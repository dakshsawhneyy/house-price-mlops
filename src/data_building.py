import pandas as pd
import numpy as np
import pickle
import yaml
import mlflow
from mlflow import sklearn
from mlflow.models.signature import infer_signature

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from dotenv import load_dotenv
import os

# Load params
with open("params.yml", "r") as f:
    params = yaml.safe_load(f)

def train_model():
    df = pd.read_csv("data/processed/data.csv")

    target = params["target"]
    y = df[target]
    X = df.drop(columns=[target])

    categorical_cols = X.select_dtypes(include=["object"]).columns
    numeric_cols = X.select_dtypes(exclude=["object"]).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols)
        ]
    )

    model_pipeline = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", LinearRegression())
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params["train"]["test_size"], random_state=params["train"]["random_state"]
    )

    load_dotenv()
    
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    username = os.getenv("MLFLOW_TRACKING_USERNAME")
    password = os.getenv("MLFLOW_TRACKING_PASSWORD")    
    
    mlflow.set_tracking_uri(tracking_uri)
    os.environ["MLFLOW_TRACKING_USERNAME"] = username
    os.environ["MLFLOW_TRACKING_PASSWORD"] = password
    
    mlflow.set_experiment("house-price-mlops-exp")

    print("MLflow initialized successfully!")

    with mlflow.start_run():

        # Fit model
        model_pipeline.fit(X_train, y_train)

        # Infer model signature
        signature = infer_signature(X_train, model_pipeline.predict(X_train))

        # Log params
        mlflow.log_params(params["train"])

        # Log the model
        model_path = "models/model.pkl"
        with open(model_path, "wb") as f:
            pickle.dump(model_pipeline, f)

        # Log into MLflow as an artifact
        mlflow.log_artifact(model_path, artifact_path="model")

        # Save model locally
        with open("models/model.pkl", "wb") as f:
            pickle.dump(model_pipeline, f)


if __name__ == "__main__":
    train_model()
