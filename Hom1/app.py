from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import joblib
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

from api.models.predict import PredictRequest, PredictResponse

MODEL_DIR = Path("models")
TRANSFORMER_PATH = MODEL_DIR / "sentence_transformer.model"
CLASSIFIER_PATH = MODEL_DIR / "classifier.joblib"
LABELS = {0: "negative", 1: "neutral", 2: "positive"}

ml_models: dict[str, Any] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_models["transformer"] = SentenceTransformer(str(TRANSFORMER_PATH))
    ml_models["classifier"] = joblib.load(CLASSIFIER_PATH)
    yield
    ml_models.clear()


app = FastAPI(title="To jest API", lifespan=lifespan)


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    embedding = ml_models["transformer"].encode([request.text])
    label = ml_models["classifier"].predict(embedding)[0]
    return PredictResponse(prediction=LABELS[int(label)])


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
