from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base


class MediaItem(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    media_type = Column(String(64), nullable=False)
    file_path = Column(String(1024), nullable=False, index=True)
    thumbnail_path = Column(String(1024), nullable=True)
    runtime = Column(Integer, nullable=True)
    resolution = Column(String(64), nullable=True)
    codec = Column(String(64), nullable=True)
    bitrate = Column(Integer, nullable=True)
    file_size = Column(Integer, nullable=True)
    overview = Column(Text, nullable=True)
