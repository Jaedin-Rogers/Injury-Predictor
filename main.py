from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_injury

app = FastAPI()

class PlayerData(BaseModel):
    training_hours: float
    recovery_days: float
    fatigue_score: float

    
@app.get("/")
def home():
    return {"message": "API is working"}


@app.post("/predict")
def predict(data: PlayerData):
    result = predict_injury(
        data.training_hours,
        data.recovery_days,
        data.fatigue_score
    )
    return result