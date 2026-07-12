from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ensure_tool(tool: str) -> None:
    if shutil.which(tool) is None:
        raise RuntimeError(f"Required tool '{tool}' is not installed or not on PATH")


def build_exe() -> Path:
    if os.name != "nt":
        raise RuntimeError("This builder must be run on Windows")

    ensure_tool("pyinstaller")
    dist_dir = ROOT / "dist" / "windows"
    dist_dir.mkdir(parents=True, exist_ok=True)

    spec = ROOT / "aurora_windows_installer.spec"
    spec.write_text(
        """
import os
from PyInstaller.utils.hooks import collect_data_files
block_cipher = None

a = Analysis(
    ['scripts/installer_wizard.py'],
    pathex=['.'],
    binaries=[],
    datas=collect_data_files('tkinter') + [('scripts', 'scripts')],
    hiddenimports=['tkinter', 'scripts.desktop_installer', 'scripts.installer_wizard'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AuroraMediaServerInstaller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name='AuroraMediaServerInstaller')
""".strip() + "\n",
        encoding="utf-8",
    )

    subprocess.run(["pyinstaller", str(spec)], cwd=ROOT, check=True)
    exe_path = dist_dir / "AuroraMediaServerInstaller" / "AuroraMediaServerInstaller.exe"
    if not exe_path.exists():
        raise RuntimeError(f"Expected installer executable at {exe_path}")
    return exe_path


if __name__ == "__main__":
    exe_path = build_exe()
    print(f"Windows installer created at: {exe_path}")
