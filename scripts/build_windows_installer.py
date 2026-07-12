import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTEND = ROOT / 'frontend'
DIST = ROOT / 'dist'


def run(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True)


if __name__ == '__main__':
    if shutil.which('pyinstaller') is None:
        print('pyinstaller is not installed. Install it with: pip install pyinstaller')
        sys.exit(1)

    if not (FRONTEND / 'package.json').exists():
        print('Frontend project not found')
        sys.exit(1)

    run(['npm', 'install'], cwd=FRONTEND)
    run(['npm', 'run', 'build'], cwd=FRONTEND)

    spec = ROOT / 'aurora_media_server.spec'
    spec.write_text(
        """
import os
from PyInstaller.utils.hooks import collect_data_files
block_cipher = None

a = Analysis(
    ['backend/app/main.py'],
    pathex=['backend'],
    binaries=[],
    datas=collect_data_files('fastapi') + collect_data_files('uvicorn') + [('frontend/dist', 'frontend/dist')],
    hiddenimports=['fastapi', 'uvicorn', 'sqlalchemy', 'pydantic', 'jwt', 'passlib'],
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
    name='AuroraMediaServer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name='AuroraMediaServer')
""".strip()
    )

    run(['pyinstaller', str(spec)])
    print(f'Installer artifacts created in {ROOT / "dist"}')
