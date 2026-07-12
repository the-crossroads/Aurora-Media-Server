from pathlib import Path

from app.services.media_scanner import scan_media_folder


def test_scan_media_folder_detects_supported_files(tmp_path: Path) -> None:
    videos_dir = tmp_path / "Videos"
    nested_dir = videos_dir / "Movies"
    nested_dir.mkdir(parents=True)

    (videos_dir / "sample.mp4").write_bytes(b"video")
    (nested_dir / "movie.mkv").write_bytes(b"movie")
    (nested_dir / "notes.txt").write_bytes(b"ignore me")
    (nested_dir / "sample.txt").write_bytes(b"ignore me")
    (nested_dir / "trailer.mp4").write_bytes(b"skip")

    scanned = scan_media_folder(str(videos_dir))

    assert len(scanned) == 2
    assert {item["title"] for item in scanned} == {"sample", "movie"}
    assert all(item["file_path"].endswith((".mp4", ".mkv")) for item in scanned)
