from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from app.schemas import LogCreate
from app.models import Log
from app.database import get_db
from fastapi import APIRouter

app = FastAPI()  # Define your FastAPI app here

router = APIRouter()


@router.post("/logs", response_model=LogCreate, status_code=status.HTTP_201_CREATED)
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    if not log.timestamp:
        from datetime import datetime

        log.timestamp = datetime.now()

    db_log = Log(level=log.level, message=log.message, timestamp=log.timestamp)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


app.include_router(router)  # Register the router with your app
