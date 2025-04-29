# back_end/database/connect.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from back_end.database.models import Base
import back_end.database.models.user_config
import back_end.database.models.shared_config
import back_end.database.models.activity_log
import back_end.database.models.meal_log
from back_end.config.settings import settings
"""
from database.models import Base
import database.models.user_config
import database.models.shared_config
import database.models.activity_log
import database.models.meal_log
from config.settings import settings
"""
from pprint import pprint

class DatabaseConnector:
    def __init__(self, database_url: str = None):
        """
        Initialise la connexion à la base de données.

        Args:
            database_url (str, optional): URL de connexion.
            Si None, utilise settings.DATABASE_URL.
        """
        self.database_url = database_url or settings.DATABASE_URL

        self.engine = create_engine(
            self.database_url,
            pool_pre_ping=True
        )
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def get_session(self) -> Session:
        """Retourne une session brute SQLAlchemy."""
        return self.SessionLocal()

    def get_db(self):
        """Yield une session pour FastAPI (avec fermeture automatique)."""
        db = self.get_session()
        try:
            yield db
        finally:
            db.close()

    def initialize_schema(self):
        """Crée toutes les tables définies dans les modèles si elles n'existent pas."""
        print("✅ Tables détectées par SQLAlchemy avant création :")
        pprint(Base.metadata.tables.keys())
        Base.metadata.create_all(bind=self.engine)
        print("✅ ORM schema created (if not exists).")