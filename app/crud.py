from sqlalchemy.orm import Session
from app import models
from datetime import datetime
from typing import Optional


def get_logs(
    db: Session,
    level: Optional[str] = None,
    source: Optional[str] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    skip: int = 0,
    limit: int = 10,
):
    query = db.query(models.Log)

    if level:
        query = query.filter(models.Log.level == level)
    if source:
        query = query.filter(models.Log.source == source)
    if start_time:
        query = query.filter(models.Log.timestamp >= start_time)
    if end_time:
        query = query.filter(models.Log.timestamp <= end_time)

    return query.offset(skip).limit(limit).all()
