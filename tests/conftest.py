# tests/conftest.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database import Base, engine


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)  # Optional: clean slate
    Base.metadata.create_all(bind=engine)


@pytest.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
