/** Renders a single chat bubble for either the user or the assistant. */
import { MessageModel } from "../../Models/MessageModel";
import "./ChatMessage.css";

interface ChatMessageProps {
  message: MessageModel;
}

export function ChatMessage({ message }: ChatMessageProps) {
  return <div className={`chat-message ${message.senderType}`}>{message.content}</div>;
}
