// front_end/react_app/react_app_vite/src/main.tsx

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import './index.css';
import { AuthProvider } from "react-oidc-context";

const oidcConfig = {
  authority: "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_LIC0zMQQT",
  client_id: "45tb3k722h9vrbdte36acdpfc0",
  redirect_uri: "http://localhost:5173",
  response_type: "code",
  scope: "phone openid email",
};

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <AuthProvider {...oidcConfig}>
      <App />
    </AuthProvider>
  </React.StrictMode>
);