# back_end/database/seed_postgres.py

"""
Seeds the PostgreSQL database with initial reference data using SQLAlchemy ORM models.
Includes values for gender, diet type, fitness level, and user goals.
"""

from database.connect import DatabaseConnector
from database.models import Gender, DietType, FitnessLevel, Goal
"""
from back_end.database.connect import DatabaseConnector
from back_end.database.models import Gender, DietType, FitnessLevel, Goal
"""
from sqlalchemy.orm import Session

# Reference values
GENDERS = ["male", "female", "other"]
DIET_TYPES = ["vegetarian", "vegan", "keto", "omnivore"]
FITNESS_LEVELS = ["beginner", "intermediate", "advanced"]
GOALS = ["Lose weight", "Gain muscle", "Improve endurance", "Tone muscles"]

# Initialise directement le connecteur (il utilisera settings.py tout seul)
db_connector = DatabaseConnector()

def insert_if_not_exists(session: Session, model, label_value: str):
    """
    Insert a row into the reference table if it doesn't already exist.

    Args:
        session (Session): SQLAlchemy session
        model: SQLAlchemy model class
        label_value (str): Label value to insert
    """
    exists = session.query(model).filter_by(label=label_value).first()
    if not exists:
        session.add(model(label=label_value))

def run_seed():
    """
    Seeds reference tables using ORM models.
    """
    print(" Seeding PostgreSQL reference tables with SQLAlchemy models...")
    db = db_connector.get_session()
    try:
        for gender in GENDERS:
            insert_if_not_exists(db, Gender, gender)
        for diet in DIET_TYPES:
            insert_if_not_exists(db, DietType, diet)
        for level in FITNESS_LEVELS:
            insert_if_not_exists(db, FitnessLevel, level)
        for goal in GOALS:
            insert_if_not_exists(db, Goal, goal)

        db.commit()
        print("✅ Seeding complete.")
    except Exception as e:
        db.rollback()
        print("❌ Error during seeding:", e)
        raise
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()