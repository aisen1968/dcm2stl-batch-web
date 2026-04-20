import pytest
from fastapi.testclient import TestClient
from app import app  # Ajusta según tu estructura

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_upload_endpoint():
    response = client.post("/upload")
    # Aquí validas la respuesta
    assert response.status_code in [200, 400]
