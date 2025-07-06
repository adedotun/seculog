from pydantic import BaseModel, Field
from datetime import datetime


class LogCreate(BaseModel):
    level: str = Field(..., description="Log level e.g. INFO, ERROR")
    message: str = Field(..., min_length=1, max_length=1024)
    timestamp: datetime | None = None

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility in Pydantic v2
