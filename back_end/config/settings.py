# back_end/config/settings.py

import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        mode = os.getenv("MODE", "local").lower()  # 👈 robustesse peu importe majuscules/minuscules

        if mode == "docker":
            load_dotenv("env_folder/.env.postgre.docker")
        elif mode == "local":
            load_dotenv("env_folder/.env.postgre.local")
        # mode == "aws" → ne charge rien, les variables sont déjà injectées dans Render

        self.POSTGRES_DB = self._get_env_var("POSTGRES_DB")
        self.POSTGRES_USER = self._get_env_var("POSTGRES_USER")
        self.POSTGRES_PASSWORD = self._get_env_var("POSTGRES_PASSWORD")
        self.POSTGRES_HOST = self._get_env_var("POSTGRES_HOST")
        self.POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

        self.DATABASE_URL = (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    def _get_env_var(self, var_name: str) -> str:
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f" Variable d'environnement obligatoire manquante : {var_name}")
        return value

settings = Settings()