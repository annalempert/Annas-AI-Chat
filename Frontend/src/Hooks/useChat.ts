import { useCallback, useEffect, useRef, useState } from "react";

import { ChatResponseModel } from "../Models/ChatResponseModel";
import { ConversationModel } from "../Models/ConversationModel";
import { MessageModel } from "../Models/MessageModel";
import { sendChat } from "../Services/ChatService";
import { createConversation, getConversationMessages } from "../Services/ConversationService";

interface UseChatResult {
  conversations: ConversationModel[];
  activeConversationId: string | null;
  messages: MessageModel[];
  isSending: boolean;
  error: string | null;
  startNewChat: () => Promise<void>;
  selectConversation: (conversationId: string) => Promise<void>;
  sendMessage: (userMessage: string) => Promise<void>;
}

export function useChat(): UseChatResult {
  const [conversations, setConversations] = useState<ConversationModel[]>([]);
  const [activeConversationId, setActiveConversationId] = useState<string | null>(null);
  const [messages, setMessages] = useState<MessageModel[]>([]);
  const [isSending, setIsSending] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const didAutoStart = useRef(false);

  const startNewChat = useCallback(async () => {
    try {
      setError(null);
      const conversation = await createConversation();
      setConversations([conversation]);
      setActiveConversationId(conversation.id);
      setMessages([]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to start new chat");
    }
  }, []);

  useEffect(() => {
    if (didAutoStart.current) {
      return;
    }
    didAutoStart.current = true;
    void startNewChat();
  }, [startNewChat]);

  const selectConversation = useCallback(async (conversationId: string) => {
    try {
      setError(null);
      setActiveConversationId(conversationId);
      const history = await getConversationMessages(conversationId);
      setMessages(history);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load messages");
    }
  }, []);

  const sendMessage = useCallback(
    async (userMessage: string) => {
      const trimmed = userMessage.trim();
      if (!trimmed) {
        return;
      }

      const optimisticMessage: MessageModel = {
        id: `temp-${Date.now()}`,
        conversationId: activeConversationId || "pending",
        senderType: "user",
        content: trimmed,
        createdAt: new Date().toISOString()
      };

      setMessages((prev) => [...prev, optimisticMessage]);
      setIsSending(true);
      setError(null);

      try {
        const response: ChatResponseModel = await sendChat({
          conversationId: activeConversationId,
          userMessage: trimmed
        });

        setActiveConversationId(response.conversationId);
        const history = await getConversationMessages(response.conversationId);
        setMessages(history);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Failed to send message");
      } finally {
        setIsSending(false);
      }
    },
    [activeConversationId]
  );

  return {
    conversations,
    activeConversationId,
    messages,
    isSending,
    error,
    startNewChat,
    selectConversation,
    sendMessage
  };
}
