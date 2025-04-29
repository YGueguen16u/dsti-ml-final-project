declare module "react-oidc-context" {
  import * as React from "react";

  // Tu peux préciser ici quelques types de base,
  // ou simplement déclarer un module générique.
  // Exemple minimal pour que TypeScript n'émette plus d'erreur :
  export interface OidcUser {
    profile: any;
    id_token: string;
    access_token: string;
    refresh_token?: string;
  }

  export interface AuthContextProps {
    user?: OidcUser;
    isAuthenticated: boolean;
    isLoading: boolean;
    error?: any;
    signinRedirect: () => void;
    removeUser: () => void;
  }

  export interface AuthProviderProps {
    children: React.ReactNode;
    authority: string;
    client_id: string;
    redirect_uri: string;
    response_type: string;
    scope: string;
  }

  export const AuthProvider: React.FC<AuthProviderProps>;

  export function useAuth(): AuthContextProps;
}
