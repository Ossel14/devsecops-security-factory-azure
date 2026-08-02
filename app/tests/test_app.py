import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_secure_data_requires_key():
    client = app.test_client()
    response = client.get("/secure-data")
    assert response.status_code == 401


def test_secure_data_with_valid_key():
    client = app.test_client()
    response = client.get("/secure-data", headers={"X-API-Key": "dev-only-placeholder-key"})
    assert response.status_code == 200