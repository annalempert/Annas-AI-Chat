-- MySQL schema for the ChatGPT-like study project.
-- Creates the database, conversation table, message table, indexes, and foreign keys.

CREATE DATABASE IF NOT EXISTS chat_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE chat_app;

-- Stores one chat thread per row.
CREATE TABLE IF NOT EXISTS conversations (
    id CHAR(36) NOT NULL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    created_at DATETIME(6) NOT NULL,
    updated_at DATETIME(6) NOT NULL
);

-- Helps list conversations by most recent activity.
CREATE INDEX idx_conversations_updated_at ON conversations (updated_at DESC);

-- Stores individual user and assistant messages.
CREATE TABLE IF NOT EXISTS messages (
    id CHAR(36) NOT NULL PRIMARY KEY,
    conversation_id CHAR(36) NOT NULL,
    sender_type ENUM('user', 'assistant') NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME(6) NOT NULL,
    CONSTRAINT fk_messages_conversation
        FOREIGN KEY (conversation_id) REFERENCES conversations(id)
        ON DELETE CASCADE
);

-- Helps load a conversation history in chronological order.
CREATE INDEX idx_messages_conversation_created ON messages (conversation_id, created_at ASC);
