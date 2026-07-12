from __future__ import annotations

from pathlib import Path
from typing import Any

SUPPORTED_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm", ".m4v"}
SKIP_NAMES = {"extra", "extras", "trailer", "trailers", "duplicate", "duplicates"}


def _should_skip(path: Path) -> bool:
    lower_name = path.name.lower()
    if any(token in lower_name for token in SKIP_NAMES):
        return True
    return any(part.lower() in SKIP_NAMES for part in path.parts)


def scan_media_folder(folder_path: str) -> list[dict[str, Any]]:
    root = Path(folder_path)
    if not root.exists():
        return []

    discovered: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if _should_skip(path):
            continue
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        discovered.append(
            {
                "title": path.stem,
                "media_type": "video",
                "file_path": str(path),
                "runtime": None,
                "resolution": None,
                "codec": None,
                "bitrate": None,
                "file_size": path.stat().st_size,
                "overview": None,
            }
        )
    return sorted(discovered, key=lambda item: item["file_path"])
