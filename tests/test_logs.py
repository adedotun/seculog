from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_log():
    response = client.post(
        "/logs/",
        json={"source": "unit-test", "level": "INFO", "message": "Test log entry"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["source"] == "unit-test"
    assert "id" in data
