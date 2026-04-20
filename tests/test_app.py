import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_app_startup():
    """Test que la app inicia correctamente"""
    assert app.title == "DCM to STL Batch Converter"

@pytest.mark.asyncio
async def test_convert_endpoint_exists():
    """Test que el endpoint /convert existe"""
    # Este test simplemente verifica que el endpoint está registrado
    response = client.post("/convert", files=[])
    # Esperamos error 422 porque no enviamos archivos
    assert response.status_code in [422, 400]