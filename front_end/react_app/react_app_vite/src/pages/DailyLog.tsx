// front_end/react_app/react_app_vite/src/pages/DailyLog.tsx

import { useEffect, useState } from "react";
import axios from "axios";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const DailyLogPage = () => {
  const [log, setLog] = useState<any | null>(null);
  const [userId, setUserId] = useState<string>("");
  const [logDate, setLogDate] = useState<Date>(new Date());
  const [isLoading, setIsLoading] = useState(false);

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
    } catch (err: any) {
      console.error("Erreur de récupération du log :", err.response?.data || err.message);
      setLog(null);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (userId) {
      fetchLog();
    }
  }, [logDate]);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold text-center mb-6">Journal Quotidien</h1>

      <input
        type="text"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        className="w-full p-2 mb-4 border rounded"
      />

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
        <div className="border rounded p-4 bg-white shadow">
          <h2 className="text-xl font-semibold mb-2">{log.log_date}</h2>
          <pre className="whitespace-pre-wrap text-sm bg-gray-100 p-3 rounded overflow-x-auto">
            {JSON.stringify(log, null, 2)}
          </pre>
        </div>
      ) : (
        <p className="text-gray-600">Aucune donnée disponible.</p>
      )}
    </div>
  );
};

export default DailyLogPage;
