/**
 * Shared Axios client for all frontend API calls.
 * Components should use service modules instead of importing this directly.
 */
import axios from "axios";
import { AppConfig } from "./AppConfig";

export const apiClient = axios.create({
  baseURL: AppConfig.apiBaseUrl,
  headers: {
    "Content-Type": "application/json"
  }
});
