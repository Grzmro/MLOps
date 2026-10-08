from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_welcome_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_nonexistent_route_returns_404():
    response = client.get("/does-not-exist")
    assert response.status_code == 404
