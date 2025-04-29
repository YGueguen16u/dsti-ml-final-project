// front_end/react_app/react_app_vite/src/pages/CreateProfile.tsx

import { useEffect, useState } from "react";
import axios from "axios";
import { useAuth } from "react-oidc-context";

const AllUsers = () => {
  const auth = useAuth();
  const [users, setUsers] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const BASE_URL = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    const fetchUsers = async () => {
      setIsLoading(true);
      try {
        const response = await axios.get(`${BASE_URL}/api/user/all`);
        setUsers(response.data);
      } catch (error: any) {
        console.error("Erreur de récupération des utilisateurs :", error.response?.data || error.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUsers();
  }, [BASE_URL]);

  if (isLoading) {
    return <p className="text-center mt-10">Chargement...</p>;
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6 text-center">Tous les utilisateurs</h1>
      <div className="grid gap-6">
        {users.map((user, idx) => (
          <div key={idx} className="p-4 border rounded shadow">
            <p><strong>Age :</strong> {user.age}</p>
            <p><strong>Weight :</strong> {user.weight} kg</p>
            <p><strong>Height :</strong> {user.height} cm</p>
            <p><strong>Genre :</strong> {user.gender}</p>
            <p><strong>Diet Type :</strong> {user.diet_type}</p>
            <p><strong>Fitness Level :</strong> {user.fitness_level}</p>
            <p><strong>Goals :</strong> {user.goals.length > 0 ? user.goals.join(", ") : "Aucun"}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AllUsers;