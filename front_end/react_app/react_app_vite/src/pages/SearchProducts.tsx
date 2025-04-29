// front_end/react_app/react_app_vite/src/pages/SearchProducts.tsx

import { useState } from "react";

function SearchProducts() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);

  const handleSearch = async () => {
    if (!query.trim()) return;

    try {
      const response = await fetch(`http://localhost:8000/api/search_products?q=${encodeURIComponent(query)}`);
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error("Erreur de recherche :", error);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Recherche de produits</h1>
      <div className="flex gap-2 mb-6">
        <input
          type="text"
          className="border p-2 flex-1 rounded"
          placeholder="Nom ou marque..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleSearch} className="bg-blue-500 text-white p-2 rounded">
          Rechercher
        </button>
      </div>
      <div className="grid gap-4">
        {results.map((product, idx) => (
          <div key={idx} className="border p-4 rounded shadow">
            <p className="font-semibold">{product.name || "Produit sans nom"}</p>
            <p className="text-gray-500 text-sm">{product.brands || "Marque inconnue"}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SearchProducts;