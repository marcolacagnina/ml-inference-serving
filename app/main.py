from fastapi import FastAPI
from pydantic import BaseModel
from app.model_logic import predict_sentiment

# Define app
app = FastAPI(title="Transformer Sentiment-Analysis API")

# Data Validation
class InputText(BaseModel):
    text: str

# Endpoint
@app.post("/predict")
def predict(input_data: InputText):
    result = predict_sentiment(input_data.text)
    return result

# Health check
@app.get("/")
def home():
    return {"message": "API is running. Go to /docs to test it."}

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": classifier is not None}
