from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def build() -> None:
    if shutil.which("pyinstaller") is None:
        print("PyInstaller is not installed. Install it with: pip install pyinstaller")
        sys.exit(1)

    build_dir = ROOT / "build" / "windows"
    dist_dir = ROOT / "dist" / "windows"
    build_dir.mkdir(parents=True, exist_ok=True)
    dist_dir.mkdir(parents=True, exist_ok=True)

    spec_path = ROOT / "aurora_installer.spec"
    spec_path.write_text(
        """
import os
from PyInstaller.utils.hooks import collect_data_files
block_cipher = None

a = Analysis(
    ['scripts/installer_wizard.py'],
    pathex=['.'],
    binaries=[],
    datas=collect_data_files('tkinter') + [('scripts', 'scripts')],
    hiddenimports=['tkinter', 'PIL', 'scripts.desktop_installer', 'scripts.installer_wizard'],
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
    icon=None,
)

coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name='AuroraMediaServerInstaller')
""".strip() + "\n",
        encoding="utf-8",
    )

    run(["pyinstaller", str(spec_path)], cwd=ROOT)
    print(f"Executable build created in {dist_dir}")


if __name__ == "__main__":
    build()
