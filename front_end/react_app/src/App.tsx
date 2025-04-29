import { useAuth } from "react-oidc-context";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import CreateProfile from "../react_app_vite/src/pages/CreateProfile";

function App() {
  const auth = useAuth();

  if (auth.isLoading) return <div>Chargement...</div>;
  if (auth.error) return <div>Erreur : {auth.error.message}</div>;

  return (
    <Router>
      <Routes>
        {!auth.isAuthenticated ? (
          <Route
            path="*"
            element={
              <div>
                <h2>Bienvenue</h2>
                <button onClick={() => auth.signinRedirect()}>
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
                <div>
                  <h2>Bonjour {auth.user?.profile.email}</h2>
                  <a href="/create-profile">Créer mon profil</a>
                  <br />
                  <button onClick={() => auth.removeUser()}>
                    Déconnexion (local)
                  </button>
                </div>
              }
            />
            <Route path="/create-profile" element={<CreateProfile />} />
            <Route path="*" element={<Navigate to="/" />} />
          </>
        )}
      </Routes>
    </Router>
  );
}

export default App;