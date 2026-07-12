from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    backend = root / "backend"
    frontend = root / "frontend"

    print("Starting Aurora Media Server...")
    if os.name == "nt":
        subprocess.Popen([sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", str(backend)], cwd=root)
    else:
        subprocess.Popen(["bash", "-lc", f"cd '{root}' && python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --app-dir backend"], cwd=root)


if __name__ == "__main__":
    main()
