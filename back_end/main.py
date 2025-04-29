# back_end/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
# from back_end.api.routes import user
from api.routes import user
from services.product_searcher import ProductSearcher
#from back_end.services.product_searcher import ProductSearcher
#from back_end.database.connect import DatabaseConnector
from database.connect import DatabaseConnector

from back_end.database import models

# PAS BESOIN de load_dotenv ici
# settings.py s'en occupe déjà via DatabaseConnector()

# Créer FastAPI
app = FastAPI()

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

# Connecteur DB
connector = DatabaseConnector()  # <-- Pas besoin de dotenv_path ici

# Démarrer à l'initialisation
@app.on_event("startup")
def startup_event():
    connector.initialize_schema()

# Product Searcher
product_searcher = ProductSearcher(
    local_ean8_path="back_end/data/products_ean8_light.json",
    local_ean13_path="back_end/data/products_ean13_light.json"
)

# Routes
app.include_router(user.router)

@app.get("/api/ping")
def ping():
    return {"message": "pong"}

@app.get("/api/search_products")
def search_products(q: str = Query(..., description="Rechercher un produit par nom ou marque"), max_results: int = 20):
    results = product_searcher.search_products(query=q, max_results=max_results)
    return {"results": results}