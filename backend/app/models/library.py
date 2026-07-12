from sqlalchemy import Boolean, Column, Integer, String, Text

from app.core.database import Base


class Library(Base):
    __tablename__ = "libraries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    description = Column(Text, nullable=True)
    folder_path = Column(String(512), nullable=False)
    library_type = Column(String(64), nullable=False)
    poster_path = Column(String(512), nullable=True)
    background_path = Column(String(512), nullable=True)
    auto_scan = Column(Boolean, default=True)
    hidden = Column(Boolean, default=False)
