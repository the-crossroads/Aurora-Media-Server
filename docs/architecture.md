# Aurora Architecture

## Overview

Aurora Media Server uses a layered architecture:

- API layer: FastAPI routers that expose REST endpoints
- Domain layer: service modules for metadata and scanning logic
- Data layer: SQLAlchemy models and repositories
- UI layer: React, React Router, TanStack Query, and Zustand

## Design Principles

- Modular and dependency-oriented
- Clear separation of API and business logic
- SQLite-first with support for PostgreSQL later
- Asynchronous-friendly background tasks for scanning and metadata refresh
