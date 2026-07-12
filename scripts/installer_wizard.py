from __future__ import annotations

import json
import os
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

from scripts.desktop_installer import prepare_installation


class InstallerWizard(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Aurora Media Server Setup")
        self.geometry("620x360")
        self.resizable(False, False)

        self.source_var = tk.StringVar(value=str(Path(__file__).resolve().parent.parent))
        self.target_var = tk.StringVar(value=str(Path.home() / "AuroraMediaServer"))
        self.install_mode = tk.StringVar(value="portable")

        tk.Label(self, text="Aurora Media Server Setup", font=("Segoe UI", 18, "bold")).pack(pady=(16, 8))
        tk.Label(self, text="Choose installation options and create shortcuts for your desktop experience.", wraplength=560).pack(pady=(0, 12))

        tk.Label(self, text="Install mode").pack(anchor="w", padx=28)
        mode_frame = tk.Frame(self)
        mode_frame.pack(fill="x", padx=28, pady=4)
        tk.Radiobutton(mode_frame, text="Portable", variable=self.install_mode, value="portable").pack(side="left")
        tk.Radiobutton(mode_frame, text="Full desktop", variable=self.install_mode, value="desktop").pack(side="left", padx=12)

        tk.Label(self, text="Install folder").pack(anchor="w", padx=28)
        folder_frame = tk.Frame(self)
        folder_frame.pack(fill="x", padx=28, pady=4)
        tk.Entry(folder_frame, textvariable=self.target_var, width=54).pack(side="left", fill="x", expand=True)
        tk.Button(folder_frame, text="Browse", command=self.pick_target).pack(side="left", padx=6)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=18)
        tk.Button(button_frame, text="Install", command=self.install, width=18, bg="#2563eb", fg="white").pack(side="left", padx=8)
        tk.Button(button_frame, text="Cancel", command=self.destroy, width=14).pack(side="left")

    def pick_target(self) -> None:
        folder = filedialog.askdirectory(initialdir=self.target_var.get())
        if folder:
            self.target_var.set(folder)

    def install(self) -> None:
        manifest = prepare_installation(self.source_var.get(), self.target_var.get())
        if self.install_mode.get() == "desktop":
            self.create_shortcuts(manifest)
        messagebox.showinfo("Installation complete", f"Aurora Media Server installed to\n{manifest['target_dir']}")

    def create_shortcuts(self) -> None:
        target = Path(self.target_var.get()).resolve()
        if os.name == "nt":
            start_menu = Path(os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Aurora Media Server"
            start_menu.mkdir(parents=True, exist_ok=True)
            shortcut = start_menu / "Aurora Media Server.lnk"
            shortcut.write_text(str(target / "start_backend.bat"), encoding="utf-8")
        else:
            desktop = Path.home() / "Desktop"
            desktop.mkdir(exist_ok=True)
            (desktop / "Aurora Media Server.desktop").write_text(
                "[Desktop Entry]\nName=Aurora Media Server\nExec=sh \"%s\"\nType=Application\n" % (target / "start_backend.bat"),
                encoding="utf-8",
            )


def main() -> None:
    app = InstallerWizard()
    app.mainloop()


if __name__ == "__main__":
    main()
