from pathlib import Path

import joblib
import pytest
from fastapi.testclient import TestClient
from sentence_transformers import SentenceTransformer

from app import app

MODEL_DIR = Path("models")
VALID_LABELS = {"negative", "neutral", "positive"}


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_classifier_loads_without_errors():
    classifier = joblib.load(MODEL_DIR / "classifier.joblib")
    assert hasattr(classifier, "predict")


def test_sentence_transformer_loads_without_errors():
    transformer = SentenceTransformer(str(MODEL_DIR / "sentence_transformer.model"))
    embedding = transformer.encode(["test"])
    assert embedding.shape[0] == 1


@pytest.mark.parametrize(
    "text",
    [
        "What a great MLOps lecture, I am very satisfied",
        "This is terrible, I hated every minute",
        "The lecture was on Monday",
    ],
)
def test_predict_returns_valid_class(client, text):
    response = client.post("/predict", json={"text": text})
    assert response.status_code == 200
    assert response.json()["prediction"] in VALID_LABELS


def test_predict_sentiment_direction(client):
    positive = client.post("/predict", json={"text": "I love this, it is fantastic"})
    negative = client.post("/predict", json={"text": "I hate this, it is awful"})
    assert positive.json()["prediction"] != negative.json()["prediction"]


def test_response_is_valid_json_with_single_key(client):
    response = client.post("/predict", json={"text": "Nice weather today"})
    assert response.headers["content-type"] == "application/json"
    body = response.json()
    assert set(body.keys()) == {"prediction"}
    assert isinstance(body["prediction"], str)


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"wrong_key": "siema"},
        {"text": ""},
        {"text": "   "},
        {"text": None},
        {"text": 123},
        {"text": ["a", "b"]},
    ],
)
def test_invalid_input_returns_json_error(client, payload):
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
    assert response.headers["content-type"] == "application/json"
    detail = response.json()["detail"]
    assert isinstance(detail, list) and len(detail) > 0
    assert "msg" in detail[0] and "loc" in detail[0]


def test_malformed_json_returns_json_error(client):
    response = client.post(
        "/predict",
        content=b"{not valid json",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 422
    assert "detail" in response.json()


def test_wrong_http_method_not_allowed(client):
    response = client.get("/predict")
    assert response.status_code == 405
