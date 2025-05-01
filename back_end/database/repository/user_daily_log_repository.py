# back_end/database/repository/user_daily_log_repository.py

from sqlalchemy.orm import Session
from back_end.database.models.user_daily_log import UserDailyLog
from datetime import date

class UserDailyLogRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_log_for_day(self, user_id: str, log_date: date):
        return self.db.query(UserDailyLog).filter_by(user_id=user_id, log_date=log_date).first()

    def insert_or_update_log(self, user_id: str, log_date: date, user_snapshot: dict, log_data: dict):
        log = self.get_log_for_day(user_id, log_date)
        if log:
            log.user_snapshot = user_snapshot
            log.log_data = log_data
        else:
            log = UserDailyLog(
                user_id=user_id,
                log_date=log_date,
                user_snapshot=user_snapshot,
                log_data=log_data
            )
            self.db.add(log)
        self.db.commit()
        return log