/**
 * Frontend runtime configuration.
 * API URL defaults for local development; no secrets are stored in the frontend.
 */
export const AppConfig = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"
};
