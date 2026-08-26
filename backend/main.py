from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Pydantic for automatic data validation

import joblib

import pandas as pd

# Input schema
class Request(BaseModel):
    cement: float
    slag: float
    ash: float
    water: float
    superplastic: float
    coarseagg: float
    fineagg: float
    age: int

# Output Schema
class Response(BaseModel):
    prediction: float


# Global dictionary to store the loaded model in memory
ml_models = {}


# Load the model efficiently during application startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    model = joblib.load('concrete_model.joblib')
    scaler = joblib.load('scaler.joblib')
    ml_models['model'] = model
    ml_models['scaler'] = scaler
    print("Model loaded successfully.")

    yield

    # Clean up memory when the server shuts down
    ml_models.clear()
    print("Model unloaded.")


app = FastAPI(lifespan=lifespan)
# Prediction Endpoint
@app.post("/predict", response_model=Response)
def predict(data: Request):
    # data is of type 'Request' Class

    # Verify the model is loaded before processing
    if "model" not in ml_models:
        raise HTTPException(status_code=500, detail="ML Model not initialized.")


    input_features = pd.DataFrame([data.model_dump()])
    
    scaled_input = ml_models['scaler'].transform(input_features)

    prediction = ml_models['model'].predict(scaled_input)
    
    return Response(prediction=prediction[0])

# run
# fastapi dev main.py