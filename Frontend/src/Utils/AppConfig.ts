/**
 * Frontend runtime configuration.
 * API URL defaults for local development; no secrets are stored in the frontend.
 */
const configuredApiBaseUrl = import.meta.env.VITE_API_BASE_URL;

export const AppConfig = {
  // Docker production uses "" so /api is proxied by nginx on the same host.
  apiBaseUrl:
    configuredApiBaseUrl === ""
      ? ""
      : configuredApiBaseUrl || "http://localhost:8000",
};
