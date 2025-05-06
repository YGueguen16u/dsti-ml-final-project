// front_end/react_app/react_app_vite/src/components/MealSection.tsx

import { useState } from "react";
import { FoodItem, Meal } from "../types/log";

interface MealSectionProps {
  meals: Meal[];
  setMeals: (meals: Meal[]) => void;
}

const MealSection = ({ meals, setMeals }: MealSectionProps) => {
  const [mealInput, setMealInput] = useState("Lunch");
  const [foodInput, setFoodInput] = useState<FoodItem>({
    name: "",
    quantity: "",
    calories: 0,
    protein: 0,
    fat: 0,
    carbs: 0,
  });
  const [currentMealItems, setCurrentMealItems] = useState<FoodItem[]>([]);

  const handleAddFood = () => {
    setCurrentMealItems([...currentMealItems, foodInput]);
    setFoodInput({ name: "", quantity: "", calories: 0, protein: 0, fat: 0, carbs: 0 });
  };

  const handleAddMeal = () => {
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
    setCurrentMealItems([]);
  };

  return (
    <div>
      <h2 className="text-lg font-semibold mt-4">Repas</h2>
      <input value={mealInput} onChange={e => setMealInput(e.target.value)} placeholder="Nom du repas" className="border p-2 mr-2" />
      <button onClick={handleAddMeal} className="bg-blue-500 text-white px-3 py-1 rounded">Ajouter repas</button>
      <div className="mt-2">
        <input value={foodInput.name} onChange={e => setFoodInput({ ...foodInput, name: e.target.value })} placeholder="Aliment" className="border p-1 mr-1" />
        <input value={foodInput.quantity} onChange={e => setFoodInput({ ...foodInput, quantity: e.target.value })} placeholder="Quantité" className="border p-1 mr-1" />
        <input value={foodInput.calories} type="number" onChange={e => setFoodInput({ ...foodInput, calories: +e.target.value })} placeholder="kcal" className="border p-1 w-20" />
        <button onClick={handleAddFood} className="bg-green-500 text-white px-2 py-1 ml-2">+ aliment</button>
      </div>
      <ul className="text-sm list-disc ml-5">
        {meals.map((m, i) => <li key={i}>{m.name} ({m.total_nutrients.calories} kcal)</li>)}
      </ul>
    </div>
  );
};

export default MealSection;
