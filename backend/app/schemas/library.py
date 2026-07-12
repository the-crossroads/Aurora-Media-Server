from pydantic import BaseModel


class LibraryCreate(BaseModel):
    name: str
    description: str | None = None
    folder_path: str
    library_type: str
    poster_path: str | None = None
    background_path: str | None = None
    auto_scan: bool = True
    hidden: bool = False


class LibraryOut(LibraryCreate):
    id: int

    class Config:
        from_attributes = True
