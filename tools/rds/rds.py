from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Chemin vers .env.rds
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
env_path = os.path.join(project_root, "env_folder/.env.rds")
load_dotenv(dotenv_path=env_path)

# Variables d’environnement
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")

# Debug
print(" DEBUG des variables d'environnement :")
print("POSTGRES_HOST:", DB_HOST)
print("POSTGRES_PORT:", repr(DB_PORT))
print("POSTGRES_USER:", DB_USER)
print("POSTGRES_PASSWORD:", "***" if DB_PASSWORD else None)
print("POSTGRES_DB:", DB_NAME)

# Vérification
if not all([DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME]):
    print(" Une ou plusieurs variables RDS sont manquantes.")
    exit(1)

# Engine
url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(url)

def list_databases():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))
            print(" Bases de données disponibles sur RDS :")
            for row in result:
                print(" -", row[0])
    except Exception as e:
        print(f" Erreur de connexion à RDS : {e}")

def list_tables():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"))
            print(f" Tables dans la base '{DB_NAME}' :")
            for row in result:
                print(" -", row[0])
    except Exception as e:
        print(f" Erreur lors de la récupération des tables : {e}")

def show_users():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM users;"))
            rows = result.fetchall()
            print(f"Contenu de la table 'users' ({len(rows)} lignes) :")

            # Récupère les noms de colonnes
            columns = result.keys()

            for row in rows:
                user_dict = dict(zip(columns, row))
                print(" -", user_dict)

    except Exception as e:
        print(f"Erreur lors de l'affichage des utilisateurs : {e}")

def show_goals():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM goals;"))
            rows = result.fetchall()
            print(f" Contenu de la table 'goals' ({len(rows)} lignes) :")

            # Récupère les noms de colonnes
            columns = result.keys()

            for row in rows:
                user_dict = dict(zip(columns, row))
                print(" -", user_dict)

    except Exception as e:
        print(f"Erreur lors de l'affichage des objectifs : {e}")

def show_user_daily_logs():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM user_daily_logs;"))
            rows = result.fetchall()
            print(f" Contenu de la table 'user_daily_logs' ({len(rows)} lignes) :")

            # Récupère les noms de colonnes
            columns = result.keys()

            for row in rows:
                user_dict = dict(zip(columns, row))
                print(" -", user_dict)

    except Exception as e:
        print(f"Erreur lors de l'affichage des user daily goals : {e}")

def show_user_daily_logs_columns():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'user_daily_logs';
            """))
            print(f" Colonnes de la table 'user_daily_logs' :")
            for row in result:
                print(f" - {row[0]} ({row[1]})")
    except Exception as e:
        print(f"Erreur lors de l'affichage des colonnes : {e}")

def alter_user_daily_logs_table():
    try:
        with engine.connect() as conn:
            print("🛠️ Modification de la table user_daily_logs...")
            conn.execute(text("ALTER TABLE user_daily_logs ADD COLUMN IF NOT EXISTS weight FLOAT;"))
            conn.execute(text("ALTER TABLE user_daily_logs ADD COLUMN IF NOT EXISTS height FLOAT;"))
            print("Colonnes 'weight' et 'height' ajoutées (ou déjà existantes).")
    except Exception as e:
        print(f"Erreur lors de la modification de la table : {e}")

def force_add_missing_columns():
    try:
        with engine.begin() as conn:  # use begin() to ensure commit
            print("Vérification et ajout des colonnes 'weight' et 'height' dans user_daily_logs...")

            result = conn.execute(text("""
                SELECT column_name FROM information_schema.columns 
                WHERE table_name = 'user_daily_logs' AND column_name IN ('weight', 'height');
            """))
            existing_columns = [row[0] for row in result]

            if "weight" not in existing_columns:
                conn.execute(text("ALTER TABLE user_daily_logs ADD COLUMN weight FLOAT;"))
                print("Colonne 'weight' ajoutée.")
            else:
                print("✔️ Colonne 'weight' déjà présente.")

            if "height" not in existing_columns:
                conn.execute(text("ALTER TABLE user_daily_logs ADD COLUMN height FLOAT;"))
                print("Colonne 'height' ajoutée.")
            else:
                print("Colonne 'height' déjà présente.")
    except Exception as e:
        print(f"Erreur lors de la vérification/ajout de colonnes : {e}")


if __name__ == "__main__":
    force_add_missing_columns()
    alter_user_daily_logs_table()
    list_databases()
    list_tables()
    show_users()
    show_goals()
    show_user_daily_logs()
    show_user_daily_logs_columns()
