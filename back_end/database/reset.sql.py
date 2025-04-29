# back_end/database/reset_db.py

from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from back_end.database.connect import DatabaseConnector

#from database.connect import DatabaseConnector

# Utilise directement ton DatabaseConnector (qui utilise settings.py automatiquement)
db = DatabaseConnector()

def reset_schema():
    """
    Drops all tables using SQLAlchemy ORM metadata.

    This is useful during development for resetting the entire database.
    """
    print("🧹 Dropping all tables via SQLAlchemy metadata...")
    metadata = MetaData()
    metadata.reflect(bind=db.engine)
    metadata.drop_all(bind=db.engine)
    print("✅ All tables dropped.")

if __name__ == "__main__":
    reset_schema()