# back_end/show_tables.py

from back_end.database.connect import DatabaseConnector
from back_end.database.models.user_config import User  # ou le modèle que tu veux voir
from sqlalchemy.orm import Session

def show_users():
    connector = DatabaseConnector()
    db: Session = connector.get_session()

    users = db.query(User).all()
    for user in users:
        print(f"User ID: {user.id}, Email: {user.email}")  # adapte selon ton modèle

if __name__ == "__main__":
    show_users()