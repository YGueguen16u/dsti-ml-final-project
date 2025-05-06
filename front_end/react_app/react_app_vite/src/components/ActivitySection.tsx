// front_end/react_app/react_app_vite/src/components/ActivitySection.tsx

import { useState } from "react";
import { Activity } from "../types/log";

interface ActivitySectionProps {
  activities: Activity[];
  setActivities: (activities: Activity[]) => void;
  activitySchema: any;
}

const ActivitySection = ({ activities, setActivities, activitySchema }: ActivitySectionProps) => {
  const [activityInput, setActivityInput] = useState<Activity>({ type: "" });

  const handleAddActivity = () => {
    setActivities([...activities, activityInput]);
    setActivityInput({ type: "" });
  };

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
      </div>
    );
  };

  return (
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
  );
};

export default ActivitySection;
