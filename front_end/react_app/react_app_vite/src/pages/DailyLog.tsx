// front_end/react_app/react_app_vite/src/pages/DailyLog.tsx

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

import MealSection from "../components/MealSection";
import ActivitySection from "../components/ActivitySection";
import ChatSection from "../components/ChatSection";

const DailyLogPage = () => {
  const { userId } = useParams<{ userId: string }>();
  const [logDate, setLogDate] = useState<Date>(new Date());
  const [meals, setMeals] = useState<any[]>([]);
  const [activities, setActivities] = useState<any[]>([]);
  const [chatHistory, setChatHistory] = useState<any[]>([]);
  const [userSnapshot, setUserSnapshot] = useState<any>({});
  const [activitySchema, setActivitySchema] = useState<any>({});

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
          goals: user.goals
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
      params: { user_id: userId }
    });
    alert("Log sauvegardé !");
  };

  useEffect(() => {
    if (userId) fetchLog();
    fetchActivitySchema();
  }, [logDate, userId]);

  return (
    <div className="p-6 max-w-3xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold text-center">Journal Quotidien</h1>
      <DatePicker selected={logDate} onChange={(d) => d && setLogDate(d)} className="p-2 border rounded" />

      <MealSection
        meals={meals}
        setMeals={setMeals}
      />

      <ActivitySection
        activities={activities}
        setActivities={setActivities}
        activitySchema={activitySchema}
      />

      <ChatSection
        chatHistory={chatHistory}
        setChatHistory={setChatHistory}
      />

      <button onClick={handleSave} className="mt-4 bg-black text-white py-2 px-4 rounded">
        Sauvegarder le journal
      </button>
    </div>
  );
};

export default DailyLogPage;
