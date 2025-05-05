// front_end/react_app/react_app_vite/src/pages/DailyLog.tsx
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const DailyLogPage = () => {
  const { userId } = useParams<{ userId: string }>();
  const [logDate, setLogDate] = useState<Date>(new Date());
  const [meals, setMeals] = useState<any[]>([]);
  const [activities, setActivities] = useState<any[]>([]);
  const [chatHistory, setChatHistory] = useState<any[]>([]);
  const [chatInput, setChatInput] = useState("");
  const [mealInput, setMealInput] = useState("Lunch");
  const [currentMealItems, setCurrentMealItems] = useState<any[]>([]);
  const [foodInput, setFoodInput] = useState({ name: "", quantity: "", calories: 0, protein: 0, fat: 0, carbs: 0 });
  const [activityInput, setActivityInput] = useState<any>({ type: "" });
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

  const handleAddActivity = () => {
    setActivities([...activities, activityInput]);
    setActivityInput({ type: "" });
  };

  const handleSendMessage = () => {
    const msg = {
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      user_input: chatInput,
      input_type: "message",
      assistant_output: "(réponse simulée)"
    };
    setChatHistory([...chatHistory, msg]);
    setChatInput("");
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

  const renderActivityFields = () => {
    if (!activityInput.type || !activitySchema[activityInput.type]) return null;
    const config = activitySchema[activityInput.type];
    return (
      <div className="space-y-2 mt-2">
        {config.fields?.map((field: string) => (
          <input
            key={field}
            placeholder={field}
            className="border p-1 mr-1"
            value={activityInput[field] || ""}
            onChange={(e) => setActivityInput({ ...activityInput, [field]: e.target.value })}
          />
        ))}
        {activityInput.type === "muscle_training" && (
          <>
            <label className="block mt-2">Exercice :</label>
            <select
              value={activityInput.exercise_name || ""}
              onChange={(e) => setActivityInput({ ...activityInput, exercise_name: e.target.value })}
              className="border p-1"
            >
              <option value="">-- Choisir --</option>
              {config.exercises.map((ex: string) => (
                <option key={ex} value={ex}>{ex}</option>
              ))}
            </select>
            <label className="block mt-2">Séries :</label>
            <textarea
              placeholder={'Séries en JSON ex: [{"reps": 10, "weight": "60kg", "rest": "90s"}]'}
              className="border w-full p-1"
              rows={3}
              value={activityInput.sets || ""}
              onChange={(e) => setActivityInput({ ...activityInput, sets: e.target.value })}
            />
          </>
        )}
      </div>
    );
  };

  return (
    <div className="p-6 max-w-3xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold text-center">Journal Quotidien</h1>
      <DatePicker selected={logDate} onChange={(d) => d && setLogDate(d)} className="p-2 border rounded" />

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

      <div>
        <h2 className="text-lg font-semibold">Activités</h2>
        <select
          value={activityInput.type || ""}
          onChange={(e) => setActivityInput({ type: e.target.value })}
          className="border p-1 mr-2"
        >
          <option value="">-- Type d'activité --</option>
          {Object.keys(activitySchema).map((key) => (
            <option key={key} value={key}>{key}</option>
          ))}
        </select>
        {renderActivityFields()}
        <button onClick={handleAddActivity} className="bg-blue-500 text-white px-2 py-1 mt-2">+ Activité</button>
        <ul className="text-sm list-disc ml-5 mt-2">
          {activities.map((a, i) => <li key={i}>{a.type}</li>)}
        </ul>
      </div>

      <div>
        <h2 className="text-lg font-semibold">Assistant</h2>
        <div className="max-h-60 overflow-y-auto bg-gray-100 p-2 border mb-2">
          {chatHistory.map((m, i) => (
            <div key={i} className="mb-2">
              <div className="text-right text-blue-700">Vous: {m.user_input}</div>
              <div className="text-left text-green-700">Coach: {m.assistant_output}</div>
            </div>
          ))}
        </div>
        <div className="flex gap-2">
          <input value={chatInput} onChange={(e) => setChatInput(e.target.value)} className="flex-1 p-2 border rounded" />
          <button onClick={handleSendMessage} className="bg-green-600 text-white px-3 py-1 rounded">Envoyer</button>
        </div>
      </div>

      <button onClick={handleSave} className="mt-4 bg-black text-white py-2 px-4 rounded">Sauvegarder le journal</button>
    </div>
  );
};

export default DailyLogPage;
