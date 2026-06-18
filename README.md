# ChatGPT-like Study Project

This repository contains a full-stack study project:

- `Database`: MySQL schema
- `Backend`: FastAPI REST API
- `Frontend`: React + TypeScript SPA (Vite)

## Architecture notes

- The frontend never calls OpenAI directly.
- All chat and conversation requests go through the FastAPI backend.
- Conversations and messages are persisted in MySQL.

## Local setup (high level)

1. Create a MySQL database and run `Database/schema.sql`.
2. Configure `Backend/.env` from `Backend/.env.example` (all secrets and keys live here).
3. Create backend virtual environment and install `Backend/requirements.txt`.
4. Install frontend dependencies and run the Vite dev server.

For Docker, use the same `Backend/.env` file: `docker compose up --build`.

## Useful commands

### Backend

```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.app:app --reload
```

### Frontend

```bash
cd Frontend
npm install
npm run dev
```
