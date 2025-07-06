from pydantic import BaseModel
from datetime import datetime


class LogResponse(BaseModel):
    id: int
    source: str
    message: str
    level: str
    timestamp: datetime

    class Config:
        orm_mode = True
