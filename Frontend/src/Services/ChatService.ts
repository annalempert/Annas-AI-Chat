/**
 * Service layer for chat-related API calls.
 */
import { ChatRequestModel } from "../Models/ChatRequestModel";
import { ChatResponseModel } from "../Models/ChatResponseModel";
import { apiClient } from "../Utils/Interceptors";

/** Send a user message to the backend and receive the assistant reply. */
export async function sendChat(payload: ChatRequestModel): Promise<ChatResponseModel> {
  const response = await apiClient.post("/api/chat", payload);
  return response.data.data as ChatResponseModel;
}
