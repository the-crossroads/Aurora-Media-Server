from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.media import MediaItem
from app.schemas.media import MediaItemOut
from app.services.media_scanner import scan_media_folder

router = APIRouter()


@router.get("", response_model=list[MediaItemOut])
def list_media(db: Session = Depends(get_db)) -> list[MediaItem]:
    return db.query(MediaItem).all()


@router.post("/scan")
def scan_media(folder_path: str = Query(...), db: Session = Depends(get_db)) -> dict[str, object]:
    scanned = scan_media_folder(folder_path)
    for item in scanned:
        existing = db.query(MediaItem).filter(MediaItem.file_path == item["file_path"]).first()
        if existing:
            continue
        db_media = MediaItem(**item)
        db.add(db_media)
    db.commit()
    return {"scanned": len(scanned), "status": "ok"}


@router.get("/{media_id}", response_model=MediaItemOut)
def get_media(media_id: int, db: Session = Depends(get_db)) -> MediaItem:
    item = db.query(MediaItem).filter(MediaItem.id == media_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Media item not found")
    return item
