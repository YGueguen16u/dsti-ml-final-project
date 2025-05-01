# back_end/database/models/user_daily_log.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class UserDailyLog(Base):
    """
    Daily log for a user (all-in-one structure).

    This table stores:
    - user_id
    - log_date
    - user_snapshot (age, weight, etc. at this date)
    - log_data (all meals, activities, mood, chat, etc.)
    """
    __tablename__ = "user_daily_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    log_date = Column(Date, nullable=False)

    user_snapshot = Column(JSON)  # âge, poids, etc. au moment du log
    log_data = Column(JSON)       # repas, sport, humeur, messages...

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", backref="daily_logs")

    __table_args__ = (
        # Un seul log par jour par utilisateur
        {'sqlite_autoincrement': True},
    )


"""
{
  "user_info": {
    "user_id": "123e4567-e89b-12d3-a456-426614174000",
    "age": 29,
    "height_cm": 180,
    "weight_kg": 75,
    "gender": "Homme"
  },
  "date": "2025-04-30",

  "meals": [
    {
      "name": "Petit-déjeuner",
      "items": [
        {
          "name": "omelette",
          "quantity": "2 oeufs",
          "barcode": "12345678",
          "nutrients": {
            "calories": 150,
            "protein": 12,
            "fat": 10,
            "carbs": 2,
            "micro": {
              "vitamin_a": 0.3,
              "iron": 1.2
            }
          }
        }
      ],
      "total_nutrients": {
        "calories": 400,
        "protein": 20,
        "fat": 15,
        "carbs": 30
      }
    }
  ],

  "activities": [
    {
      "type": "musculation",
      "mode": "détaillée",
      "exercise": "Développé couché",
      "sets": [
        {"reps": 8, "weight_kg": 120},
        {"reps": 9, "weight_kg": 110}
      ]
    },
    {
      "type": "course",
      "duration_minutes": 30,
      "intensity": "haute"
    }
  ],

  "chat_history": [
    {
      "time": "08:30",
      "user_input": "J’ai mangé 2 œufs et une banane",
      "input_type": "log_alimentaire",
      "assistant_output": "C’est noté ! Cela ajoute ~220 calories à ton petit-déjeuner"
    },
    {
      "time": "08:31",
      "user_input": "Et une tartine avec du beurre",
      "input_type": "log_alimentaire",
      "assistant_output": "Parfait, on ajoute 150 calories de plus."
    },
    {
      "time": "13:00",
      "user_input": "Je veux un conseil pour le dîner",
      "input_type": "conseil",
      "assistant_output": "Tu pourrais viser un dîner léger avec des protéines, par exemple du poisson avec des légumes."
    }
  ]
}
"""