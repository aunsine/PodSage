from fastapi.testclient import TestClient
from podsage.ml_service.main import app  # Test ML Service health

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
