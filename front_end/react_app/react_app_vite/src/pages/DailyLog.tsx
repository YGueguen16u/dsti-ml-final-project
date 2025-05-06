// front_end/react_app/react_app_vite/src/pages/DailyLog.tsx

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

import MealSection from "../components/MealSection";
import ActivitySection from "../components/ActivitySection";
import ChatSection from "../components/ChatSection";

import { Activity, ChatMessage, Meal } from "../types/log";

const DailyLogPage = () => {
  const { userId } = useParams<{ userId: string }>();
  const [logDate, setLogDate] = useState<Date>(new Date());

  const [meals, setMeals] = useState<Meal[]>([]);
  const [activities, setActivities] = useState<Activity[]>([]);
  const [chatHistory, setChatHistory] = useState<ChatMessage[]>([]);
  const [userSnapshot, setUserSnapshot] = useState<any>({});
  const [activitySchema, setActivitySchema] = useState<any>({});
  const [successMessage, setSuccessMessage] = useState("");

  const BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

  const fetchLog = async () => {
    if (!userId) return;
    try {
      const formattedDate = logDate.toISOString().split("T")[0];
      const res = await axios.get(`${BASE_URL}/api/log`, {
        params: { user_id: userId, log_date: formattedDate },
      });
      const d = res.data.log_data;
      setMeals(d.meals || []);
      setActivities(d.activities || []);
      setChatHistory(d.chat_history || []);
      setUserSnapshot(res.data.user_snapshot || {});
    } catch (err) {
      console.warn("Pas de log ce jour, créez-en un nouveau.");
      setMeals([]);
      setActivities([]);
      setChatHistory([]);
      fetchUserSnapshot();
    }
  };

  const fetchUserSnapshot = async () => {
    try {
      const res = await axios.get(`${BASE_URL}/api/user/all`);
      const user = res.data.find((u: any) => u.user_id === userId);
      if (user) {
        setUserSnapshot({
          name: user.name,
          age: user.age,
          gender: user.gender,
          weight: user.weight,
          height: user.height,
          target_weight: user.target_weight,
          fitness_level: user.fitness_level,
          diet_type: user.diet_type,
          goals: user.goals,
        });
      }
    } catch (err) {
      console.error("Erreur lors du snapshot utilisateur :", err);
    }
  };

  const fetchActivitySchema = async () => {
    try {
      const res = await axios.get(`${BASE_URL}/api/log/activity_schema`);
      setActivitySchema(res.data);
    } catch (err) {
      console.error("Erreur de chargement des schémas d'activité", err);
    }
  };

  const handleSave = async () => {
    const payload = {
      log_date: logDate.toISOString().split("T")[0],
      user_snapshot: userSnapshot,
      log_data: { meals, activities, chat_history: chatHistory },
    };
    await axios.post(`${BASE_URL}/api/log/`, payload, {
      params: { user_id: userId },
    });
    setSuccessMessage("✔️ Journal bien sauvegardé !");
    setTimeout(() => setSuccessMessage(""), 3000);
  };

  useEffect(() => {
    if (userId) fetchLog();
    fetchActivitySchema();
  }, [logDate, userId]);

  // Résumé nutritionnel
  const dailySummary = meals.reduce(
    (acc, meal) => {
      acc.calories += meal.total_nutrients.calories || 0;
      acc.protein += meal.total_nutrients.protein || 0;
      acc.carbs += meal.total_nutrients.carbs || 0;
      acc.fat += meal.total_nutrients.fat || 0;
      return acc;
    },
    { calories: 0, protein: 0, carbs: 0, fat: 0 }
  );

  const totalActivityTime = activities.reduce((sum, act) => {
    const t = parseInt(act.duration_minutes || act.time || "0", 10);
    return sum + (isNaN(t) ? 0 : t);
  }, 0);

  return (
    <div className="p-6 max-w-3xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold text-center">Journal Quotidien</h1>

      <div className="flex justify-center">
        <DatePicker
          selected={logDate}
          onChange={(d) => d && setLogDate(d)}
          className="p-2 border rounded text-sm"
        />
      </div>

      <MealSection meals={meals} setMeals={setMeals} />
      <ActivitySection
        activities={activities}
        setActivities={setActivities}
        activitySchema={activitySchema}
      />
      <ChatSection
        chatHistory={chatHistory}
        setChatHistory={setChatHistory}
      />

      <div className="p-4 bg-gray-100 rounded-lg shadow text-sm space-y-1">
        <h3 className="font-semibold">Résumé de la journée :</h3>
        <div>🔥 Calories totales : {dailySummary.calories} kcal</div>
        <div>🥩 Protéines : {dailySummary.protein} g</div>
        <div>🍞 Glucides : {dailySummary.carbs} g</div>
        <div>🥑 Lipides : {dailySummary.fat} g</div>
        <div>⏱️ Temps d’activité : {totalActivityTime} min</div>
      </div>

      {successMessage && (
        <div className="text-green-700 text-sm font-medium bg-green-100 p-2 rounded text-center">
          {successMessage}
        </div>
      )}

      <button
        onClick={handleSave}
        className="mt-4 w-full bg-black text-white py-2 px-4 rounded text-lg"
      >
        Sauvegarder le journal
      </button>
    </div>
  );
};

export default DailyLogPage;