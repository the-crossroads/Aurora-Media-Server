from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.library import Library
from app.schemas.library import LibraryCreate, LibraryOut

router = APIRouter()


@router.get("", response_model=list[LibraryOut])
def list_libraries(db: Session = Depends(get_db)) -> list[Library]:
    return db.query(Library).all()


@router.post("", response_model=LibraryOut)
def create_library(library: LibraryCreate, db: Session = Depends(get_db)) -> Library:
    db_library = Library(**library.model_dump())
    db.add(db_library)
    db.commit()
    db.refresh(db_library)
    return db_library


@router.get("/{library_id}", response_model=LibraryOut)
def get_library(library_id: int, db: Session = Depends(get_db)) -> Library:
    library = db.query(Library).filter(Library.id == library_id).first()
    if not library:
        raise HTTPException(status_code=404, detail="Library not found")
    return library
