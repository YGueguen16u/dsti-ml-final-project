// front_end/react_app/react_app_vite/src/pages/DailyLog.tsx

// front_end/react_app/react_app_vite/src/pages/DailyLog.tsx

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const DailyLogPage = () => {
  const { userId } = useParams<{ userId: string }>();
  const [log, setLog] = useState<any | null>(null);
  const [logDate, setLogDate] = useState<Date>(new Date());
  const [isLoading, setIsLoading] = useState(false);
  const [chatInput, setChatInput] = useState("");
  const [chatHistory, setChatHistory] = useState<any[]>([]);

  const BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

  const fetchLog = async () => {
    if (!userId) return;
    setIsLoading(true);
    try {
      const formattedDate = logDate.toISOString().split("T")[0];
      const res = await axios.get(`${BASE_URL}/api/log`, {
        params: { user_id: userId, log_date: formattedDate },
      });
      setLog(res.data);
      setChatHistory(res.data.chat_history || []);
    } catch (err: any) {
      console.error("Erreur de récupération du log :", err.response?.data || err.message);
      setLog(null);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSendMessage = () => {
    if (!chatInput.trim()) return;
    const newMessage = {
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      user_input: chatInput,
      input_type: "message",
      assistant_output: "(réponse simulée)"
    };
    setChatHistory([...chatHistory, newMessage]);
    setChatInput("");
  };

  useEffect(() => {
    if (userId) {
      fetchLog();
    }
  }, [logDate, userId]);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold text-center mb-6">Journal Quotidien</h1>

      <div className="mb-4">
        <label className="block mb-1">Choisir une date :</label>
        <DatePicker
          selected={logDate}
          onChange={(date: Date | null) => {
            if (date) setLogDate(date);
          }}
          className="p-2 border rounded"
        />
      </div>

      <button
        onClick={fetchLog}
        className="mb-6 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded"
      >
        Charger le journal
      </button>

      {isLoading ? (
        <p>Chargement...</p>
      ) : log ? (
        <div className="border rounded p-4 bg-white shadow space-y-6">
          <h2 className="text-xl font-semibold mb-2">{log.log_date}</h2>

          {/* Meals */}
          <div>
            <h3 className="text-lg font-bold">Repas</h3>
            {log.meals?.map((meal: any, idx: number) => (
              <div key={idx} className="mb-4 p-3 border rounded bg-gray-50">
                <h4 className="font-semibold">{meal.name}</h4>
                <ul className="list-disc pl-4">
                  {meal.items.map((item: any, i: number) => (
                    <li key={i}>{item.name} - {item.quantity} - {item.nutrients.calories} kcal</li>
                  ))}
                </ul>
                <div className="text-sm text-gray-600 mt-2">
                  Total : {meal.total_nutrients.calories} kcal, Prot: {meal.total_nutrients.protein}g, Glu: {meal.total_nutrients.carbs}g, Lip: {meal.total_nutrients.fat}g
                </div>
              </div>
            ))}
          </div>

          {/* Activities */}
          <div>
            <h3 className="text-lg font-bold">Activités</h3>
            {log.activities?.map((act: any, i: number) => (
              <div key={i} className="mb-2 p-3 border rounded bg-gray-50">
                <p>{act.type === 'musculation' ? `${act.exercise} - ${act.sets.length} séries` : `${act.type} - ${act.duration_minutes} min`}</p>
              </div>
            ))}
          </div>

          {/* Chatbot */}
          <div>
            <h3 className="text-lg font-bold">Assistant</h3>
            <div className="max-h-64 overflow-y-auto border rounded p-2 bg-gray-100 mb-2">
              {chatHistory.map((msg, i) => (
                <div key={i} className="mb-2">
                  <div className="text-right text-sm text-blue-700">{msg.time} - Vous : {msg.user_input}</div>
                  <div className="text-left text-sm text-green-700">{msg.assistant_output}</div>
                </div>
              ))}
            </div>
            <div className="flex gap-2">
              <input
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                className="flex-1 p-2 border rounded"
                placeholder="Envoyer un message au coach..."
              />
              <button onClick={handleSendMessage} className="px-4 bg-green-600 text-white rounded">Envoyer</button>
            </div>
          </div>
        </div>
      ) : (
        <p className="text-gray-600">Aucune donnée disponible.</p>
      )}
    </div>
  );
};

export default DailyLogPage;
