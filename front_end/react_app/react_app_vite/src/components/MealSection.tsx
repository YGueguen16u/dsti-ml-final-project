// front_end/react_app/react_app_vite/src/components/MealSection.tsx

import { useRef, useState } from "react";
import { FoodItem, Meal } from "../types/log";
import { PlusCircle } from "lucide-react";

interface MealSectionProps {
  meals: Meal[];
  setMeals: (meals: Meal[]) => void;
}

const MealSection = ({ meals, setMeals }: MealSectionProps) => {
  const [mealInput, setMealInput] = useState("Lunch");
  const [currentMealItems, setCurrentMealItems] = useState<FoodItem[]>([]);
  const [foodInput, setFoodInput] = useState<FoodItem>({
    name: "",
    quantity: "",
    calories: 0,
    protein: 0,
    fat: 0,
    carbs: 0,
  });

  const nameInputRef = useRef<HTMLInputElement>(null);

  const handleAddFood = () => {
    if (!foodInput.name) return;
    setCurrentMealItems((prev) => [...prev, foodInput]);
    setFoodInput({ name: "", quantity: "", calories: 0, protein: 0, fat: 0, carbs: 0 });
    nameInputRef.current?.focus();
  };

  const handleAddMeal = () => {
    if (currentMealItems.length === 0) return;
    const total = currentMealItems.reduce(
      (acc, f) => ({
        calories: acc.calories + +f.calories,
        protein: acc.protein + +f.protein,
        fat: acc.fat + +f.fat,
        carbs: acc.carbs + +f.carbs,
      }),
      { calories: 0, protein: 0, fat: 0, carbs: 0 }
    );
    setMeals([...meals, { name: mealInput, items: currentMealItems, total_nutrients: total }]);
    setMealInput("");
    setCurrentMealItems([]);
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2">
        <input
          value={mealInput}
          onChange={(e) => setMealInput(e.target.value)}
          placeholder="Nom du repas (ex: Déjeuner)"
          className="border p-2 rounded flex-1"
        />
        <button onClick={handleAddMeal} className="flex items-center gap-1 bg-blue-600 text-white px-3 py-1 rounded">
          <PlusCircle size={18} /> Ajouter repas
        </button>
      </div>

      <div className="grid grid-cols-6 gap-2">
        <input
          ref={nameInputRef}
          value={foodInput.name}
          onChange={(e) => setFoodInput({ ...foodInput, name: e.target.value })}
          placeholder="Aliment"
          className="border p-2 col-span-2 rounded"
        />
        <input
          value={foodInput.quantity}
          onChange={(e) => setFoodInput({ ...foodInput, quantity: e.target.value })}
          placeholder="Quantité"
          className="border p-2 col-span-1 rounded"
        />
        <input
          value={foodInput.calories}
          type="number"
          onChange={(e) => setFoodInput({ ...foodInput, calories: +e.target.value })}
          placeholder="kcal"
          className="border p-2 col-span-1 rounded"
        />
        <button onClick={handleAddFood} className="col-span-2 bg-green-600 text-white rounded flex items-center justify-center">
          <PlusCircle className="mr-1" size={18} /> Ajouter aliment
        </button>
      </div>

      {meals.map((meal, idx) => (
        <div key={idx} className="border rounded p-4 shadow-sm bg-white">
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
        </div>
      ))}
    </div>
  );
};

export default MealSection;