/** Home page that hosts the main chat experience. */
import { ChatPage } from "../ChatArea/ChatPage";
import "./Home.css";

export function Home() {
  return (
    <section className="home">
      <ChatPage />
    </section>
  );
}
