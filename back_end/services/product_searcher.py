# back_end/services/product_searcher.py

import json
from infrastructure.aws.s3.s3_manager import S3Manager

class ProductSearcher:
    def __init__(self):
        """
        Loads product data (EAN8 + EAN13) directly from S3 into memory.
        """
        self.products = []
        self.s3_manager = S3Manager()
        self.load_products()

    def load_products(self):
        """
        Load product JSONs directly from S3 into memory.
        """
        print(" Loading product data from S3...")
        products_ean8 = self.s3_manager.load_json("productindex/products_ean8_light.json")
        products_ean13 = self.s3_manager.load_json("productindex/products_ean13_light.json")
        self.products = products_ean8 + products_ean13
        print(f" Loaded {len(self.products)} products.")

    def search_products(self, query: str, max_results: int = 20):
        """
        Search products by name or brand.

        Args:
            query (str): The search string.
            max_results (int): Maximum number of results.

        Returns:
            List of matching products.
        """
        query = query.lower()
        matches = []

        for product in self.products:
            name = product.get("name", "").lower()
            brands = (product.get("brands") or "").lower()

            if query in name or query in brands:
                matches.append(product)

            if len(matches) >= max_results:
                break

        return matches

    def get_product_by_barcode(self, barcode: str):
        """
        Given a barcode, fetch full product JSON from appropriate S3 folder.
        """
        folder = "openfoodfactstransformed/EAN8" if len(barcode) == 8 else "openfoodfactstransformed/EAN13"
        path = f"{folder}/{barcode}.json"
        try:
            product_data = self.s3_manager.load_json(path)
            return product_data
        except Exception as e:
            print(f"Erreur chargement produit {barcode} : {e}")
            return None
