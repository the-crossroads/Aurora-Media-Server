from pathlib import Path

from scripts.desktop_installer import prepare_installation


def test_prepare_installation_creates_launchers_and_manifest(tmp_path: Path) -> None:
    source_root = tmp_path / "source"
    (source_root / "backend").mkdir(parents=True)
    (source_root / "frontend").mkdir(parents=True)
    (source_root / "backend" / "main.py").write_text("print('hello')", encoding="utf-8")
    (source_root / "frontend" / "package.json").write_text('{"name":"demo"}', encoding="utf-8")
    (source_root / "README.md").write_text("demo", encoding="utf-8")

    target_root = tmp_path / "install"
    manifest = prepare_installation(source_root, target_root)

    assert (target_root / "backend" / "main.py").exists()
    assert (target_root / "start_backend.bat").exists()
    assert (target_root / "start_frontend.bat").exists()
    assert manifest["target_dir"] == str(target_root)
