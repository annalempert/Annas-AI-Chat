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
2. Configure `Backend/.env` from `Backend/.env.example`.
3. Create backend virtual environment and install `Backend/requirements.txt`.
4. Configure `Frontend/.env` from `Frontend/.env.example`.
5. Install frontend dependencies and run the Vite dev server.

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
