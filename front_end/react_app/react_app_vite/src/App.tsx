// front_end/react_app/react_app_vite/src/App.tsx

// import { useAuth } from "react-oidc-context";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import CreateProfile from "./pages/CreateProfile";
import SearchProducts from "./pages/SearchProducts"; // 👈 AJOUT ICI
import AllUsers from "./pages/AllUsers";

function App() {
  // const auth = useAuth();

  // if (auth.isLoading) return <div>Chargement...</div>;
  // if (auth.error) return <div>Erreur : {auth.error.message}</div>;

  // TEMPORAIRE : considérer l'utilisateur comme toujours connecté
  const isAuthenticated = true;

  return (
    <Router>
      <Routes>
        {!isAuthenticated ? (
          <Route
            path="*"
            element={
              <div className="text-center mt-40">
                <h2 className="text-2xl font-bold">Bienvenue</h2>
                <button
                  className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
                  onClick={() => console.log("Se connecter")}
                >
                  Se connecter
                </button>
              </div>
            }
          />
        ) : (
          <>
            <Route
              path="/"
              element={
                <div className="text-center mt-40">
                  <h2 className="text-2xl font-bold">
                    Bonjour {/* {auth.user?.profile.email} --> COMME PAS CONNECTÉ */}
                    invité
                  </h2>
                  <div className="mt-6">
                    <a href="/create-profile" className="block text-blue-600 underline">
                      Créer mon profil
                    </a>
                    <a href="/search-product" className="block text-green-600 underline mt-4">
                      Rechercher un aliment
                    </a>
                    <a href="/all-users" className="block text-purple-600 underline mt-4">
                      Voir tous les utilisateurs
                    </a>
                    <button
                      onClick={() => console.log("Déconnexion")}
                      className="block mt-6 px-4 py-2 bg-red-500 text-white rounded"
                    >
                      Déconnexion (local)
                    </button>
                  </div>
                </div>
              }
            />
            <Route path="/create-profile" element={<CreateProfile />} />
            <Route path="/search-product" element={<SearchProducts />} />
            <Route path="/all-users" element={<AllUsers />} />
            <Route path="*" element={<Navigate to="/" />} />
          </>
        )}
      </Routes>
    </Router>
  );
}

export default App;