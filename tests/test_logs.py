import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_log_success(async_client: AsyncClient):
    data = {
        "level": "INFO",
        "message": "Test log message",
    }
    response = await async_client.post("/logs", json=data)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["level"] == data["level"]
    assert json_data["message"] == data["message"]
    assert "timestamp" in json_data


@pytest.mark.asyncio
async def test_create_log_failure_missing_message(async_client: AsyncClient):
    data = {"level": "ERROR"}
    response = await async_client.post("/logs", json=data)
    assert response.status_code == 422  # Validation error
