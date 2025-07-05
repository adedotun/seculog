from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


def create_log(db: Session, log: schemas.LogCreate):
    db_log = models.LogEntry(
        source=log.source,
        level=log.level,
        message=log.message,
        timestamp=log.timestamp or datetime.utcnow(),
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
