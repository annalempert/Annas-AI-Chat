/** Reusable error banner for API and UI failures. */
import "./ErrorMessage.css";

interface ErrorMessageProps {
  message: string;
}

export function ErrorMessage({ message }: ErrorMessageProps) {
  return <div className="error-message">{message}</div>;
}
