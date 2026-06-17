/** Button that starts a brand-new conversation. */
import "./NewChatButton.css";

interface NewChatButtonProps {
  onClick: () => void;
}

export function NewChatButton({ onClick }: NewChatButtonProps) {
  return (
    <button className="new-chat-button" onClick={onClick} type="button">
      New Chat
    </button>
  );
}
