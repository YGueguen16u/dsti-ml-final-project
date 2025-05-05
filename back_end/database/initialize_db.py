# back_end/database/initialize_db.py

from sqlalchemy import MetaData

from back_end.database.connect import DatabaseConnector
from back_end.database.repository.user_repository import UserRepository

"""
from connect import DatabaseConnector
from database.repository.user_repository import UserRepository
"""
def reset_schema(connector: DatabaseConnector):
    """Supprime toutes les tables existantes."""
    print("🧹 Dropping all tables via SQLAlchemy metadata...")
    metadata = MetaData()
    metadata.reflect(bind=connector.engine)
    metadata.drop_all(bind=connector.engine)
    print("✅ All tables dropped.")

def seed_test_data(connector: DatabaseConnector):
    """Ajoute des données de test pour le développement."""
    print("🌱 Inserting test data...")

    db = next(connector.get_db())
    repo = UserRepository(db)

    import uuid

    user_id = str(uuid.uuid4())

    repo.insert_user(
        user_id=user_id,
        name="Test User",
        age=28,
        gender="Male",
        height=180.0,
        weight=75.0,
        target_weight=72.0,
        diet_type="Omnivore",
        fitness_level="Intermediate",
        goals=["Lose fat", "Build muscle"]
    )

    print(f"✅ Test user inserted: {user_id}")

def initialize_database():
    """Reset complet + recréation + ajout de données de test."""
    connector = DatabaseConnector()

    print("🚨 Resetting the database...")
    reset_schema(connector)

    print("🛠️ Recreating tables...")
    connector.initialize_schema()

    print("🌱 Seeding test data...")
    seed_test_data(connector)

    print("✅ Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()