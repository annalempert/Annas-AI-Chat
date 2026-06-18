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

For Docker, use the same `Backend/.env` file:

```bash
docker compose --env-file Backend/.env up --build -d
```

## Deploy on Ubuntu server (DigitalOcean Droplet)

`.env` files are **not** in GitHub on purpose. After `git clone`, create secrets on the server:

```bash
cd Annas-AI-Chat
cp Backend/.env.example Backend/.env
nano Backend/.env
chmod 600 Backend/.env
docker compose --env-file Backend/.env up --build -d
```

Set real values in `Backend/.env`, including:

- `MYSQL_ROOT_PASSWORD` — strong password for MySQL
- `OPENAI_API_KEY` — your OpenAI key
- `CORS_ORIGINS` — `http://YOUR_SERVER_IP` (or your domain; use port 80, no `:80` suffix)

Open in browser: `http://YOUR_SERVER_IP`

The frontend nginx container serves the app on port **80** and proxies `/api` to the backend internally, so the browser never calls `localhost:8000`.

### Alternative: DigitalOcean App Platform

If you use App Platform (`.do/app.yaml`) instead of `docker compose` on a Droplet, secrets are set in the DigitalOcean dashboard — no `Backend/.env` file on the server. App Platform provides managed MySQL and injects `DATABASE_URL` and `OPENAI_API_KEY` for you.

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
