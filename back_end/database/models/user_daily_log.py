# back_end/database/models/user_daily_log.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, JSON, Float
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

    weight = Column(Float)
    height = Column(Float)

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
-- Contenu de la ligne
id: 1
user_id: '123e4567-e89b-12d3-a456-426614174000'
log_date: '2025-05-01'
weight: 74.5
height: 179.0
user_snapshot: {
  "age": 29,
  "gender": "Homme",
  "fitness_level": "Intermediate",
  "diet_type": "Omnivore"
}
log_data: {
  "meals": [
    {
      "name": "Petit-déjeuner",
      "items": [
        {
          "name": "Omelette",
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
        "calories": 150,
        "protein": 12,
        "fat": 10,
        "carbs": 2
      }
    }
  ],
  "activities": [
    {
      "type": "course",
      "duration_minutes": 30,
      "intensity": "modérée"
    }
  ],
  "chat_history": [
    {
      "time": "08:30",
      "user_input": "J’ai mangé une omelette",
      "input_type": "log_alimentaire",
      "assistant_output": "OK, j’ai enregistré 150 kcal pour ce repas."
    }
  ]
}
created_at: '2025-05-01T08:35:00Z'
updated_at: '2025-05-01T08:35:00Z'
"""