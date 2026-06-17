/** Text input and submit button for sending chat messages. */
import { FormEvent, useState } from "react";
import "./ChatInput.css";

interface ChatInputProps {
  isSending: boolean;
  onSend: (message: string) => Promise<void>;
}

export function ChatInput({ isSending, onSend }: ChatInputProps) {
  const [message, setMessage] = useState("");

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    const trimmed = message.trim();
    if (!trimmed) {
      return;
    }

    setMessage("");
    await onSend(trimmed);
  };

  return (
    <form className="chat-input-form" onSubmit={handleSubmit}>
      <input
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        placeholder="Type your message..."
        disabled={isSending}
      />
      <button type="submit" disabled={isSending}>
        Send
      </button>
    </form>
  );
}
