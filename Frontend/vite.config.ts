/**
 * Vite configuration for the React frontend.
 * Uses the React plugin and runs the dev server on port 5173.
 */
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173
  }
});
