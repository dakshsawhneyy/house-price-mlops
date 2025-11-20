from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# ---- Add Prometheus BEFORE app starts ----
instrumentator = Instrumentator().instrument(app)
instrumentator.expose(app)

# ---- INPUT SCHEMA ----
class HouseInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus: int

# ---- PREDICT ENDPOINT ----
@app.post("/predict")
def predict_price(data: HouseInput):

    features = np.array([[ 
        data.area,
        data.bedrooms,
        data.bathrooms,
        data.stories,
        data.mainroad,
        data.guestroom,
        data.basement,
        data.hotwaterheating,
        data.airconditioning,
        data.parking,
        data.prefarea,
        data.furnishingstatus
    ]])

    pred = model.predict(features)[0]

    return {"predicted_price": float(pred)}

# ---- HEALTHCHECK ----
@app.get("/health")
def health():
    return {"status": "ok"}
