/** Request payload sent from the frontend to POST /api/chat. */
export interface ChatRequestModel {
  conversationId?: string | null;
  userMessage: string;
}
