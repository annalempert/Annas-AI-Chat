import { MessageModel } from "./MessageModel";

/** Response payload returned after a successful chat request. */
export interface ChatResponseModel {
  conversationId: string;
  assistantMessage: MessageModel;
}
