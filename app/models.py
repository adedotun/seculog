from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    message = Column(String)
    level = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
