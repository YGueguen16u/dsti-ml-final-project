# back_end/show_tables.py

"""
from back_end.database.connect import DatabaseConnector
from back_end.database.models.user_config import User
"""
from database.connect import DatabaseConnector
from database.models.user_config import User
from sqlalchemy.orm import Session

def show_users():
    connector = DatabaseConnector()
    db: Session = connector.get_session()

    users = db.query(User).all()
    for user in users:
        print(f"User ID: {user.id}, Email: {user.email}")

if __name__ == "__main__":
    show_users()