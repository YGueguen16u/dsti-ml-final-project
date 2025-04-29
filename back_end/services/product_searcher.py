import json
import os
from ..infrastructure.aws.s3.s3_manager import S3Manager

class ProductSearcher:
    def __init__(self, local_ean8_path: str, local_ean13_path: str):
        """
        Args:
            local_ean8_path (str): Local path for EAN8 product file.
            local_ean13_path (str): Local path for EAN13 product file.
        """
        self.products = []
        self.local_ean8_path = local_ean8_path
        self.local_ean13_path = local_ean13_path
        self.s3_manager = S3Manager()

        self.ensure_files()
        self.load_products()

    def ensure_files(self):
        """
        Download the two product index files from S3 if they are missing locally.
        """
        if not os.path.exists(self.local_ean8_path):
            print(f"⬇️ Downloading EAN8 index from S3...")
            self.s3_manager.download(
                "productindex/products_ean8_light.json",
                self.local_ean8_path
            )
        else:
            print(f"✅ EAN8 index already exists locally.")

        if not os.path.exists(self.local_ean13_path):
            print(f"⬇️ Downloading EAN13 index from S3...")
            self.s3_manager.download(
                "productindex/products_ean13_light.json",
                self.local_ean13_path
            )
        else:
            print(f"✅ EAN13 index already exists locally.")

    def load_products(self):
        """
        Load products from the two local JSON files.
        """
        try:
            with open(self.local_ean8_path, "r", encoding="utf-8") as f:
                products_ean8 = json.load(f)
            with open(self.local_ean13_path, "r", encoding="utf-8") as f:
                products_ean13 = json.load(f)

            self.products = products_ean8 + products_ean13
            print(f"🔍 Loaded {len(self.products)} products for search.")
        except Exception as e:
            print(f"❌ Error loading products: {e}")

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