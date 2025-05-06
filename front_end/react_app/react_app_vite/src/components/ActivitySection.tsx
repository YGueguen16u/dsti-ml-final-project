// front_end/react_app/react_app_vite/src/components/ActivitySection.tsx

import { useState, useRef } from "react";
import { Activity } from "../types/log";
import { PlusCircle } from "lucide-react";

interface ActivitySectionProps {
  activities: Activity[];
  setActivities: (activities: Activity[]) => void;
  activitySchema: any;
}

const ActivitySection = ({ activities, setActivities, activitySchema }: ActivitySectionProps) => {
  const [activityInput, setActivityInput] = useState<Activity>({ type: "" });
  const selectRef = useRef<HTMLSelectElement>(null);

  const handleAddActivity = () => {
    if (!activityInput.type) return;
    setActivities([...activities, activityInput]);
    setActivityInput({ type: "" });
    selectRef.current?.focus();
  };

  const renderActivityFields = () => {
    if (!activityInput.type || !activitySchema[activityInput.type]) return null;
    const config = activitySchema[activityInput.type];

    return (
      <div className="space-y-2 mt-2">
        {config.fields?.map((field: string) => {
          if (field === "exercise_name") {
            return (
              <select
                key={field}
                value={activityInput.exercise_name || ""}
                onChange={(e) => setActivityInput({ ...activityInput, exercise_name: e.target.value })}
                className="border p-2 w-full rounded"
              >
                <option value="">-- Choisir exercice --</option>
                {config.exercises?.map((ex: string) => (
                  <option key={ex} value={ex}>{ex}</option>
                ))}
              </select>
            );
          }

          if (field === "sets") {
            return (
              <textarea
                key={field}
                placeholder='Séries JSON: [{"reps":10,"weight":"60kg","rest":"90s"}]'
                value={activityInput.sets || ""}
                onChange={(e) => setActivityInput({ ...activityInput, sets: e.target.value })}
                className="border p-2 w-full rounded"
                rows={3}
              />
            );
          }

          return (
            <input
              key={field}
              placeholder={field}
              className="border p-2 w-full rounded"
              value={activityInput[field] || ""}
              onChange={(e) => setActivityInput({ ...activityInput, [field]: e.target.value })}
            />
          );
        })}
      </div>
    );
  };

  const totalDuration = activities.reduce((acc, a) => {
    const dur = parseInt(a.duration_minutes || a.time || "0", 10);
    return acc + (isNaN(dur) ? 0 : dur);
  }, 0);

  return (
    <div className="border p-4 rounded-lg shadow bg-white mt-6 space-y-4">
      <h2 className="text-lg font-semibold flex items-center">
        🏃 Activités
      </h2>

      <div className="flex items-center gap-2">
        <select
          ref={selectRef}
          value={activityInput.type || ""}
          onChange={(e) => setActivityInput({ type: e.target.value })}
          className="border p-2 rounded w-full"
        >
          <option value="">-- Type d'activité --</option>
          {Object.keys(activitySchema).map((key) => (
            <option key={key} value={key}>{key}</option>
          ))}
        </select>
      </div>

      {renderActivityFields()}

      <button
        onClick={handleAddActivity}
        className="bg-blue-600 text-white px-3 py-2 rounded flex items-center gap-2"
      >
        <PlusCircle size={18} /> Ajouter activité
      </button>

      <table className="w-full border mt-4 text-sm">
        <thead>
          <tr className="bg-gray-100">
            <th className="border px-2 py-1">Type</th>
            <th className="border px-2 py-1">Détails</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((a, i) => (
            <tr key={i}>
              <td className="border px-2 py-1 font-semibold">{a.type}</td>
              <td className="border px-2 py-1 text-xs">
                {Object.entries(a)
                  .filter(([k]) => k !== "type")
                  .map(([k, v]) => `${k}: ${v}`)
                  .join(" | ")}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="mt-2 text-sm text-right font-medium">
        ⏱️ Temps total estimé : {totalDuration} min
      </div>
    </div>
  );
};

export default ActivitySection;