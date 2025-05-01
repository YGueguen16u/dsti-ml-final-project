# back_end/api/routes/daily_log.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date
from back_end.database.connect import DatabaseConnector
from back_end.database.repository.user_daily_log_repository import UserDailyLogRepository

router = APIRouter(prefix="/api/log", tags=["Daily Log"])
db_connector = DatabaseConnector()

class DailyLogInput(BaseModel):
    log_date: date
    user_snapshot: dict
    log_data: dict

@router.post("/")
def insert_or_update_log(payload: DailyLogInput, user_id: str, db: Session = Depends(db_connector.get_db)):
    repo = UserDailyLogRepository(db)
    try:
        log = repo.insert_or_update_log(user_id, payload.log_date, payload.user_snapshot, payload.log_data)
        return {"message": "Log enregistré", "log_date": str(log.log_date)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'insertion : {e}")

@router.get("/")
def get_log_for_date(user_id: str, log_date: date, db: Session = Depends(db_connector.get_db)):
    repo = UserDailyLogRepository(db)
    log = repo.get_log_for_day(user_id, log_date)
    if not log:
        raise HTTPException(status_code=404, detail="Log introuvable pour cette date")
    return {
        "user_snapshot": log.user_snapshot,
        "log_data": log.log_data,
        "log_date": log.log_date
    }