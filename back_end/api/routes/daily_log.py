# back_end/api/routes/daily_log.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date
from back_end.database.connect import DatabaseConnector
from back_end.database.repository.user_daily_log_repository import UserDailyLogRepository
import json
import os

router = APIRouter(prefix="/api/log", tags=["Daily Log"])
db_connector = DatabaseConnector()

# Charger les schémas d'activités depuis un fichier local JSON
SCHEMA_ACTIVITY_PATH = os.path.join(os.path.dirname(__file__), "activity_schema.json")
try:
    with open(SCHEMA_ACTIVITY_PATH, "r", encoding="utf-8") as f:
        ACTIVITY_SCHEMAS = json.load(f)
except Exception as e:
    print(f"Erreur de chargement des schémas d'activité : {e}")
    ACTIVITY_SCHEMAS = {}

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

@router.get("")
def get_log_for_date(user_id: str, log_date: date, db: Session = Depends(db_connector.get_db)):
    repo = UserDailyLogRepository(db)
    log = repo.get_log_for_day(user_id, log_date)
    if not log:
        # Return default structured empty log
        user = db.query(User).filter_by(user_id=user_id).first()
        if not user:
            raise HTTPException(404, "Utilisateur introuvable")
        return {
            "log_date": log_date,
            "user_snapshot": {
                "name": user.name,
                "age": user.age,
                "gender": user.gender.label,
                "weight": user.weight,
                "height": user.height,
                "target_weight": user.target_weight,
                "fitness_level": user.fitness_level.label,
                "diet_type": user.diet_type.label,
                "goals": [g.label for g in user.goals]
            },
            "log_data": {
                "meals": [],
                "activities": [],
                "chat_history": []
            }
        }
    return {
        "user_snapshot": log.user_snapshot,
        "log_data": log.log_data,
        "log_date": log.log_date
    }

@router.get("/activity_schema")
def get_activity_schemas():
    return ACTIVITY_SCHEMAS