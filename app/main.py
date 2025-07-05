from fastapi import FastAPI
from .routers import logs
from .database import Base, engine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(logs.router)
