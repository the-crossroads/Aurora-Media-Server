from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, dashboard, health, libraries, media
from app.core.database import Base, engine

app = FastAPI(
    title="Aurora Media Server",
    version="0.1.0",
    description="A modern personal media server built with FastAPI and React.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


app.include_router(health.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(libraries.router, prefix="/api/libraries", tags=["libraries"])
app.include_router(media.router, prefix="/api/media", tags=["media"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
