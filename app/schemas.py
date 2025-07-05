from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class LogCreate(BaseModel):
    source: str
    level: str
    message: str
    timestamp: Optional[datetime] = None


class LogOut(LogCreate):
    id: int

    class Config:
        orm_mode = True
