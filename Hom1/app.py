from fastapi import FastAPI
from api.models.predict import PredictRequest, PredictResponse

app = FastAPI(title="To jest API")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction="positive")
