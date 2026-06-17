/**
 * Service layer for conversation CRUD API calls.
 */
import { ConversationModel } from "../Models/ConversationModel";
import { MessageModel } from "../Models/MessageModel";
import { apiClient } from "../Utils/Interceptors";

/** Create a new empty conversation on the backend. */
export async function createConversation(): Promise<ConversationModel> {
  const response = await apiClient.post("/api/conversations");
  return response.data.data as ConversationModel;
}

/** Fetch all saved conversations. */
export async function getConversations(): Promise<ConversationModel[]> {
  const response = await apiClient.get("/api/conversations");
  return response.data.data as ConversationModel[];
}

/** Fetch all messages for one conversation. */
export async function getConversationMessages(conversationId: string): Promise<MessageModel[]> {
  const response = await apiClient.get(`/api/conversations/${conversationId}/messages`);
  return response.data.data as MessageModel[];
}

/** Delete a conversation and its messages. */
export async function deleteConversation(conversationId: string): Promise<void> {
  await apiClient.delete(`/api/conversations/${conversationId}`);
}
