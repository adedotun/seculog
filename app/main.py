from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/logs", response_model=List[schemas.LogResponse])
def read_logs(
    level: Optional[str] = Query(None),
    source: Optional[str] = Query(None),
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_logs(db, level, source, start_time, end_time, skip, limit)
