# Aurora Media Server

Aurora Media Server is a polished, self-hosted personal media platform inspired by modern streaming experiences. The project combines a FastAPI backend, a React 19 frontend, SQLite by default, and a Docker-friendly deployment model.

## Features

- Media library management for movies, TV shows, anime, music videos, and home videos
- FastAPI REST API with OpenAPI documentation
- Responsive Netflix-inspired UI with dark mode and animated transitions
- User authentication and admin bootstrap
- Dashboard, library browsing, and extensible metadata foundation

## Project Structure

- backend/ — FastAPI application, models, routes, services
- frontend/ — Vite + React + TypeScript UI
- docker/ — Dockerfiles and compose configuration
- tests/ — pytest coverage
- docs/ — Architecture and usage guides
- scripts/ — helper scripts

## Quick Start

### Backend

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --app-dir backend
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker compose -f docker/docker-compose.yml up --build
```

## API

The backend exposes:

- GET /api/health
- POST /api/auth/register
- POST /api/auth/login
- GET /api/libraries
- GET /api/media
- GET /api/dashboard/overview

## Testing

```bash
pytest -q
```
