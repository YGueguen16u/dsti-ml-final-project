# back_end/main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from back_end.api.routes import user, daily_log
#from api.routes import user
#from services.product_searcher import ProductSearcher
from back_end.services.product_searcher import ProductSearcher
from back_end.database.connect import DatabaseConnector
#from database.connect import DatabaseConnector
from back_end.database.seed_postgres import run_seed

from back_end.config.settings import settings

print("📡 DATABASE_URL =", settings.DATABASE_URL)


# Créer FastAPI
app = FastAPI()

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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
    connector.initialize_schema()
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