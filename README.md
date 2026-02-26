Injury Predictor API
A FastAPI-based machine learning API that predicts an athlete’s injury risk using logistic regression. The model evaluates training hours, recovery days, and fatigue score to calculate injury probability and classify risk as Low, Mid, or High.
Features
Predicts injury probability
Returns clear risk classification
Built with FastAPI
Lightweight and easy to deploy
Installation
pip install -r requirements.txt
Run the API:
uvicorn main:app --reload
Server runs at:
http://127.0.0.1:8000
API Endpoints
GET /
Health check endpoint.
POST /predict
Request Body:
{
  "training_hours": 10.5,
  "recovery_days": 2,
  "fatigue_score": 6.0
}
Response Example:
{
  "probability": 0.28,
  "risk": "Mid"
}
Model
Uses a logistic regression formula to calculate injury probability based on training load, recovery, and fatigue.
📄 Project Structure
main.py        # FastAPI app
model.py       # Prediction logic
requirements.txt
Colligate_Injury_Predictor.ipynb
Built for educational and demonstration purposes.
