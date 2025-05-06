// front_end/react_app/react_app_vite/src/components/MealSection.tsx

// front_end/react_app/react_app_vite/src/components/MealSection.tsx

import { useRef, useState, useEffect } from "react";
import { FoodItem, Meal } from "../types/log";
import { PlusCircle } from "lucide-react";

interface MealSectionProps {
  meals: Meal[];
  setMeals: (meals: Meal[]) => void;
}

const BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

const MealSection = ({ meals, setMeals }: MealSectionProps) => {
  const [mealInput, setMealInput] = useState("Lunch");
  const [foodInputs, setFoodInputs] = useState<Record<number, FoodItem>>({});
  const [suggestions, setSuggestions] = useState<Record<number, any[]>>({});

  const addMeal = () => {
    if (!mealInput.trim()) return;
    setMeals([
      ...meals,
      {
        name: mealInput,
        items: [],
        total_nutrients: { calories: 0, protein: 0, fat: 0, carbs: 0 },
      },
    ]);
    setMealInput("");
  };

  const handleAddFoodToMeal = (mealIdx: number) => {
    const input = foodInputs[mealIdx];
    if (!input || !input.name) return;

    const updatedMeals = [...meals];
    const meal = updatedMeals[mealIdx];
    const updatedItems = [...meal.items, input];

    const total = updatedItems.reduce(
      (acc, f) => ({
        calories: acc.calories + +f.calories,
        protein: acc.protein + +f.protein,
        fat: acc.fat + +f.fat,
        carbs: acc.carbs + +f.carbs,
      }),
      { calories: 0, protein: 0, fat: 0, carbs: 0 }
    );

    updatedMeals[mealIdx] = {
      ...meal,
      items: updatedItems,
      total_nutrients: total,
    };

    setMeals(updatedMeals);
    setFoodInputs((prev) => ({
      ...prev,
      [mealIdx]: { name: "", quantity: "", calories: 0, protein: 0, fat: 0, carbs: 0 },
    }));
    setSuggestions((prev) => ({ ...prev, [mealIdx]: [] }));
  };

  const handleSelectSuggestion = (mealIdx: number, product: any) => {
    const nutriments = product.nutriments || {};
    setFoodInputs((prev) => ({
      ...prev,
      [mealIdx]: {
        name: product.name,
        quantity: "100g",
        calories: nutriments.energy_kcal || 0,
        protein: nutriments.proteins || 0,
        fat: nutriments.fat || 0,
        carbs: nutriments.carbohydrates || 0,
      },
    }));
    setSuggestions((prev) => ({ ...prev, [mealIdx]: [] }));
  };

  useEffect(() => {
    const timeouts: Record<number, ReturnType<typeof setTimeout>> = {};
    Object.entries(foodInputs).forEach(([idxStr, input]) => {
      const idx = parseInt(idxStr);
      if (!input?.name || input.name.length < 2) {
        setSuggestions((prev) => ({ ...prev, [idx]: [] }));
        return;
      }
      if (timeouts[idx]) clearTimeout(timeouts[idx]);
      timeouts[idx] = setTimeout(async () => {
        try {
          const res = await fetch(`${BASE_URL}/api/search_products?q=${encodeURIComponent(input.name)}`);
          const data = await res.json();
          setSuggestions((prev) => ({ ...prev, [idx]: data.results || [] }));
        } catch (err) {
          console.error("Erreur de suggestion:", err);
        }
      }, 300);
    });
    return () => Object.values(timeouts).forEach(clearTimeout);
  }, [foodInputs]);

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2">
        <input
          value={mealInput}
          onChange={(e) => setMealInput(e.target.value)}
          placeholder="Nom du repas (ex: Déjeuner)"
          className="border p-2 rounded flex-1"
        />
        <button
          onClick={addMeal}
          className="flex items-center gap-1 bg-blue-600 text-white px-3 py-1 rounded"
        >
          <PlusCircle size={18} /> Ajouter repas
        </button>
      </div>

      {meals.map((meal, idx) => (
        <div key={idx} className="border rounded p-4 shadow-sm bg-white relative">
          <div className="flex justify-between items-center font-semibold text-lg mb-2">
            <span>{meal.name}</span>
            <span>{meal.total_nutrients.calories} kcal</span>
          </div>

          <table className="w-full text-sm border">
            <thead>
              <tr className="bg-gray-100">
                <th className="border px-2 py-1">Aliment</th>
                <th className="border px-2 py-1">Quantité</th>
                <th className="border px-2 py-1">Kcal</th>
                <th className="border px-2 py-1">Prot</th>
                <th className="border px-2 py-1">Gluc</th>
                <th className="border px-2 py-1">Lip</th>
              </tr>
            </thead>
            <tbody>
              {meal.items.map((item, i) => (
                <tr key={i}>
                  <td className="border px-2 py-1">{item.name}</td>
                  <td className="border px-2 py-1">{item.quantity}</td>
                  <td className="border px-2 py-1">{item.calories}</td>
                  <td className="border px-2 py-1">{item.protein}</td>
                  <td className="border px-2 py-1">{item.carbs}</td>
                  <td className="border px-2 py-1">{item.fat}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <div className="grid grid-cols-6 gap-2 mt-3 relative">
            <div className="col-span-2 relative">
              <input
                value={foodInputs[idx]?.name || ""}
                onChange={(e) =>
                  setFoodInputs({ ...foodInputs, [idx]: { ...foodInputs[idx], name: e.target.value } })
                }
                placeholder="Aliment"
                className="border p-2 w-full rounded"
              />
              {suggestions[idx]?.length > 0 && (
                <ul className="absolute z-10 bg-white border w-full max-h-40 overflow-y-auto rounded shadow">
                  {suggestions[idx].map((product, i) => (
                    <li
                      key={i}
                      className="p-2 text-sm hover:bg-gray-100 cursor-pointer"
                      onClick={() => handleSelectSuggestion(idx, product)}
                    >
                      {product.name} <span className="text-gray-400">({product.brands})</span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
            <input
              value={foodInputs[idx]?.quantity || ""}
              onChange={(e) => setFoodInputs({ ...foodInputs, [idx]: { ...foodInputs[idx], quantity: e.target.value } })}
              placeholder="Quantité"
              className="border p-2 col-span-1 rounded"
            />
            <input
              value={foodInputs[idx]?.calories || 0}
              type="number"
              onChange={(e) =>
                setFoodInputs({ ...foodInputs, [idx]: { ...foodInputs[idx], calories: +e.target.value } })
              }
              placeholder="kcal"
              className="border p-2 col-span-1 rounded"
            />
            <button
              onClick={() => handleAddFoodToMeal(idx)}
              className="col-span-2 bg-green-600 text-white rounded flex items-center justify-center"
            >
              <PlusCircle className="mr-1" size={18} /> Ajouter aliment
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default MealSection;
