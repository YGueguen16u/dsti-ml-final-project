// front_end/react_app/react_app_vite/src/pages/CreateProfile.tsx

import React, { useState, useEffect } from "react";
import axios from "axios";

const CreateProfile = () => {
  const [form, setForm] = useState({
    name: "",
    age: "",
    weight: "",
    target_weight: "",
    height: "",
    gender: "",
    diet_type: "",
    fitness_level: "",
    goals: [] as string[],
  });

  const [availableGoals, setAvailableGoals] = useState<string[]>([]);

  const BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");
  console.log("BASE_URL =", BASE_URL);
  console.log("import.meta.env =", import.meta.env);

    useEffect(() => {
      const fetchGoals = async () => {
        try {
          const res = await axios.get(`${BASE_URL}/api/user/goals`);
          const goalLabels = res.data.map((g: { value: string }) => g.value);
          setAvailableGoals(goalLabels);
        } catch (err: any) {
          console.error("Failed to fetch goals:", err.response?.data || err.message);
        }
      };
      fetchGoals();
    }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleGoalChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const selected = Array.from(e.target.selectedOptions).map((opt) => opt.value);
    setForm({ ...form, goals: selected });
  };


  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post(`${BASE_URL}/api/user/profile`, form);
      alert("Profile saved!");
    } catch (err: any) {
      console.error("Error while saving:", err.response?.data || err.message);
      alert("Error while saving.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto bg-white p-6 rounded shadow-md mt-10">
      <h2 className="text-2xl font-bold mb-4 text-center">Complete my profile</h2>
        <input
          className="w-full p-2 mb-3 border border-gray-300 rounded"
          name="name"
          type="text"
          placeholder="Name"
          value={form.name}
          onChange={handleChange}
        />
      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="age"
        type="number"
        placeholder="Age"
        value={form.age}
        onChange={handleChange}
      />

      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="weight"
        type="number"
        placeholder="Weight (kg)"
        value={form.weight}
        onChange={handleChange}
      />
      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="target_weight"
        type="number"
        placeholder="Target weight (kg)"
        value={form.target_weight}
        onChange={handleChange}
      />
      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="height"
        type="number"
        placeholder="Height (cm)"
        value={form.height}
        onChange={handleChange}
      />

      <select
        name="gender"
        value={form.gender}
        onChange={handleChange}
        className="w-full p-2 mb-3 border border-gray-300 rounded"
      >
        <option value="">Gender</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
        <option value="Other">Other</option>
      </select>

      <select
        name="diet_type"
        value={form.diet_type}
        onChange={handleChange}
        className="w-full p-2 mb-3 border border-gray-300 rounded"
      >
        <option value="">Diet type</option>
        <option value="Omnivore">Omnivore</option>
        <option value="Vegetarian">Vegetarian</option>
        <option value="Vegan">Vegan</option>
        <option value="Keto">Keto</option>
      </select>

      <select
        name="fitness_level"
        value={form.fitness_level}
        onChange={handleChange}
        className="w-full p-2 mb-3 border border-gray-300 rounded"
      >
        <option value="">Fitness level</option>
        <option value="Beginner">Beginner</option>
        <option value="Intermediate">Intermediate</option>
        <option value="Advanced">Advanced</option>
      </select>

        <label className="block text-sm text-gray-700 mb-1">
          Goals (Ctrl/Cmd + click to select multiple)
        </label>
        <select
          multiple
          name="goals"
          value={form.goals}
          onChange={handleGoalChange}
          className="w-full p-2 mb-4 border border-gray-300 rounded"
        >
          {availableGoals.map((goal) => (
            <option key={goal} value={goal}>
              {goal}
            </option>
          ))}
        </select>

      <button
        type="submit"
        className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 rounded"
      >
        Submit
      </button>
    </form>
  );
};

export default CreateProfile;