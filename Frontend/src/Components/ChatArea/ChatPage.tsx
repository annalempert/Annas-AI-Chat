/**
 * Main chat screen with prompt header, messages, input, and loading/error states.
 */
import { useChat } from "../../Hooks/useChat";
import { ChatInput } from "./ChatInput";
import { ChatMessage } from "./ChatMessage";
import { NewChatButton } from "./NewChatButton";
import { Spinner } from "../SharedArea/Spinner";
import { ErrorMessage } from "../SharedArea/ErrorMessage";
import "./ChatPage.css";

export function ChatPage() {
  const chat = useChat();

  const handleSend = async (message: string) => {
    await chat.sendMessage(message);
  };

  const handleNewChat = async () => {
    await chat.startNewChat();
  };

  return (
    <div className="chat-page">
      <section className="chat-main">
        <div className="chat-main-top">
          <div className="chat-main-prompt">
            <span className="chat-main-prompt-label">AI Companion</span>
            <p>What is on your mind today?</p>
          </div>
          <NewChatButton onClick={() => void handleNewChat()} />
        </div>
        {chat.error && <ErrorMessage message={chat.error} />}
        <div className="chat-messages">
          {chat.messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          {chat.isSending && <Spinner />}
        </div>
        <ChatInput isSending={chat.isSending} onSend={handleSend} />
      </section>
    </div>
  );
}
