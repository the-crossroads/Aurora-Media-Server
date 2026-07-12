from pydantic import BaseModel


class MediaItemOut(BaseModel):
    id: int
    title: str
    media_type: str
    file_path: str
    runtime: int | None = None
    resolution: str | None = None
    codec: str | None = None
    bitrate: int | None = None
    file_size: int | None = None
    overview: str | None = None

    class Config:
        from_attributes = True
