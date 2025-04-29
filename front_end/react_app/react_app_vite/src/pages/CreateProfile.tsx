// front_end/react_app/react_app_vite/src/pages/CreateProfile.tsx

import React, { useState } from "react";
import axios from "axios";

const CreateProfile = () => {
  const [form, setForm] = useState({
    age: "",
    weight: "",
    target_weight: "",
    height: "",
    gender: "",
    diet_type: "",
    fitness_level: "",
    goals: [] as string[],
  });

  const BASE_URL = import.meta.env.VITE_API_BASE_URL;

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
      alert("Profil enregistré !");
    } catch (err: any) {
      console.error("Erreur lors de l’enregistrement :", err.response?.data || err.message);
      alert("Erreur lors de l’enregistrement.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto bg-white p-6 rounded shadow-md mt-10">
      <h2 className="text-2xl font-bold mb-4 text-center">Compléter mon profil</h2>

      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="age"
        type="number"
        placeholder="Âge"
        value={form.age}
        onChange={handleChange}
      />
      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="weight"
        type="number"
        placeholder="Poids (kg)"
        value={form.weight}
        onChange={handleChange}
      />
      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="target_weight"
        type="number"
        placeholder="Poids cible (kg)"
        value={form.target_weight}
        onChange={handleChange}
      />
      <input
        className="w-full p-2 mb-3 border border-gray-300 rounded"
        name="height"
        type="number"
        placeholder="Taille (cm)"
        value={form.height}
        onChange={handleChange}
      />

      <select
        name="gender"
        value={form.gender}
        onChange={handleChange}
        className="w-full p-2 mb-3 border border-gray-300 rounded"
      >
        <option value="">Genre</option>
        <option value="Homme">Homme</option>
        <option value="Femme">Femme</option>
        <option value="Autre">Autre</option>
      </select>

      <select
        name="diet_type"
        value={form.diet_type}
        onChange={handleChange}
        className="w-full p-2 mb-3 border border-gray-300 rounded"
      >
        <option value="">Type de régime</option>
        <option value="Omnivore">Omnivore</option>
        <option value="Végétarien">Végétarien</option>
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

      <label className="block text-sm text-gray-700 mb-1">Objectifs (Ctrl/Cmd + clic pour plusieurs)</label>
      <select
        multiple
        name="goals"
        value={form.goals}
        onChange={handleGoalChange}
        className="w-full p-2 mb-4 border border-gray-300 rounded"
      >
        <option value="Lose weight">Lose weight</option>
        <option value="Build muscle">Build muscle</option>
        <option value="Tone up">Tone up</option>
        <option value="Endurance">Endurance</option>
      </select>

      <button
        type="submit"
        className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 rounded"
      >
        Valider
      </button>
    </form>
  );
};

export default CreateProfile;