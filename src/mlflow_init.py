from dagshub import dagshub_logger
import mlflow
from dotenv import load_dotenv
import os

def init_mlflow():
    load_dotenv()
    
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    username = os.getenv("MLFLOW_TRACKING_USERNAME")
    password = os.getenv("MLFLOW_TRACKING_PASSWORD")    
    
    mlflow.set_tracking_uri(tracking_uri)
    os.environ["MLFLOW_TRACKING_USERNAME"] = username
    os.environ["MLFLOW_TRACKING_PASSWORD"] = password
    
    mlflow.set_experiment("house-price-mlops-exp")

    print("MLflow initialized successfully!")