/**
 * Frontend runtime configuration.
 * Values come from Vite environment variables in Frontend/.env.
 */
export const AppConfig = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"
};
