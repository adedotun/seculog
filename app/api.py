from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.schemas import LogCreate
from app.models import Log
from app.database import get_db
from datetime import datetime

router = APIRouter()


@router.post("/logs", response_model=LogCreate, status_code=status.HTTP_201_CREATED)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    if not log.timestamp:
        log.timestamp = datetime.utcnow()
    db_log = Log(level=log.level, message=log.message, timestamp=log.timestamp)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


@router.get("/logs", response_model=List[LogCreate])
def get_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Log).offset(skip).limit(limit).all()
