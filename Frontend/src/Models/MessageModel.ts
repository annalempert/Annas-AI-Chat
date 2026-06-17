/** Allowed message authors in the chat UI and API contract. */
export type SenderType = "user" | "assistant";

/** TypeScript model for a single chat message. */
export interface MessageModel {
  id: string;
  conversationId: string;
  senderType: SenderType;
  content: string;
  createdAt: string;
}
