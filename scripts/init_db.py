from app.core.database import Base, engine
from app.models.library import Library
from app.models.media import MediaItem
from app.models.user import User


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database initialized")
