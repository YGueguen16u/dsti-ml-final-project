# back_end/main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from sqlalchemy import text

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from back_end.api.routes import user, daily_log
#from api.routes import user
#from services.product_searcher import ProductSearcher
from back_end.services.product_searcher import ProductSearcher
from back_end.database.connect import DatabaseConnector
#from database.connect import DatabaseConnector
from back_end.database.seed_postgres import run_seed

from fastapi import APIRouter, HTTPException

from back_end.config.settings import settings

print("DATABASE_URL =", settings.DATABASE_URL)


# Créer FastAPI
app = FastAPI()

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("🔎 Render ENV DEBUG :")
print("POSTGRES_HOST =", os.getenv("POSTGRES_HOST"))
print("POSTGRES_DB =", os.getenv("POSTGRES_DB"))
# Connecteur DB
connector = DatabaseConnector()

# Démarrer à l'initialisation
@app.on_event("startup")
def on_startup():
    connector = DatabaseConnector()

    with connector.engine.connect() as conn:
        print("Suppression manuelle de la table user_daily_logs (si elle existe)...")
        conn.execute(text("DROP TABLE IF EXISTS user_daily_logs CASCADE;"))

    # Recrée toutes les tables définies dans tes modèles SQLAlchemy
    connector.initialize_schema()

    # Resync les colonnes optionnelles après recréation
    with connector.engine.connect() as conn:
        print("🛠️ Vérification et ajout de colonnes manquantes dans user_daily_logs...")
        conn.execute(text("ALTER TABLE user_daily_logs ADD COLUMN IF NOT EXISTS weight FLOAT;"))
        conn.execute(text("ALTER TABLE user_daily_logs ADD COLUMN IF NOT EXISTS height FLOAT;"))

    run_seed()

# Product Searcher
product_searcher = ProductSearcher()


# Routes
app.include_router(user.router)
app.include_router(daily_log.router)
@app.get("/api/ping")
def ping():
    return {"message": "pong"}

@app.get("/api/search_products")
def search_products(q: str = Query(..., description="Rechercher un produit par nom ou marque"), max_results: int = 20):
    results = product_searcher.search_products(query=q, max_results=max_results)
    return {"results": results}

@app.get("/api/get_product_by_barcode")
def get_product_by_barcode(barcode: str):
    searcher = ProductSearcher()
    product = searcher.get_product_by_barcode(barcode)
    if not product:
        raise HTTPException(status_code=404, detail="Produit non trouvé")

    # Extraction utile
    nutr = product.get("nutrients_100g", {})
    return {
        "name": product.get("name"),
        "brands": product.get("brands"),
        "barcode": product.get("barcode"),
        "nutrients": {
            "calories": nutr.get("energy_kcal_100g", {}).get("quantity", 0),
            "protein": nutr.get("proteins", {}).get("quantity", 0),
            "carbs": nutr.get("carbohydrates", {}).get("quantity", 0),
            "fat": nutr.get("fat", {}).get("quantity", 0),
        }
    }