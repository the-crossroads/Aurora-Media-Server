from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def prepare_installation(source_root: Path | str, target_root: Path | str) -> dict[str, Any]:
    source = Path(source_root).resolve()
    target = Path(target_root).resolve()
    target.mkdir(parents=True, exist_ok=True)

    for item in ["backend", "frontend", "docs", "scripts", "README.md", "requirements.txt"]:
        source_item = source / item
        if source_item.exists():
            destination = target / item
            if source_item.is_dir():
                shutil.copytree(source_item, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, destination)

    (target / "start_backend.bat").write_text(
        "@echo off\ncd /d \"%~dp0backend\"\npython -m pip install -r ../requirements.txt\npython -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --app-dir .\n",
        encoding="utf-8",
    )
    (target / "start_frontend.bat").write_text(
        "@echo off\ncd /d \"%~dp0frontend\"\nnpm install\nnpm run dev\n",
        encoding="utf-8",
    )
    (target / "run_aurora.desktop").write_text(
        "#!/usr/bin/env bash\ncd \"$(dirname \"$0\")\"\npython3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload --app-dir backend\n",
        encoding="utf-8",
    )

    manifest = {
        "target_dir": str(target),
        "created_at": "now",
        "launcher_files": ["start_backend.bat", "start_frontend.bat"],
    }
    (target / "install_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest
