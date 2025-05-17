# back_end/database/models/user_daily_log.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, JSON, Float, UniqueConstraint, Index
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
        UniqueConstraint("user_id", "log_date", name="unique_user_log_per_day"),
        Index('ix_user_log_user_date', 'user_id', 'log_date'),
    )

