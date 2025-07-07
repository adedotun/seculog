# tests/conftest.py
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.main import app
from app.database import Base, get_db
import os

# Use the same database URL used in Docker test environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://seculog:seculog@db/seculog_db")

# Set up test DB engine and session
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override FastAPI's dependency to use test DB session
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    Automatically creates all tables in the test database before any tests run.
    """
    Base.metadata.drop_all(bind=engine)  # Optional: reset the DB for clean testing
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
async def async_client():
    """
    Returns an async HTTP client for API testing without starting a real server.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
