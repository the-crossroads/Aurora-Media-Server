from __future__ import annotations

import json
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

from scripts.desktop_installer import prepare_installation


class InstallerUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Aurora Media Server Installer")
        self.geometry("520x280")
        self.resizable(False, False)

        self.source_var = tk.StringVar(value=str(Path(__file__).resolve().parent.parent))
        self.target_var = tk.StringVar(value=str(Path.home() / "AuroraMediaServer"))

        tk.Label(self, text="Install Aurora Media Server", font=("Segoe UI", 16, "bold")).pack(pady=(16, 8))
        tk.Label(self, text="Choose the source folder and destination install location.", wraplength=480).pack(pady=(0, 10))

        tk.Label(self, text="Source folder").pack(anchor="w", padx=24)
        frame = tk.Frame(self)
        frame.pack(fill="x", padx=24, pady=4)
        tk.Entry(frame, textvariable=self.source_var, width=48).pack(side="left", fill="x", expand=True)
        tk.Button(frame, text="Browse", command=self.pick_source).pack(side="left", padx=6)

        tk.Label(self, text="Install folder").pack(anchor="w", padx=24)
        frame2 = tk.Frame(self)
        frame2.pack(fill="x", padx=24, pady=4)
        tk.Entry(frame2, textvariable=self.target_var, width=48).pack(side="left", fill="x", expand=True)
        tk.Button(frame2, text="Browse", command=self.pick_target).pack(side="left", padx=6)

        tk.Button(self, text="Install", command=self.install, width=20, bg="#2563eb", fg="white").pack(pady=16)

    def pick_source(self) -> None:
        folder = filedialog.askdirectory(initialdir=self.source_var.get())
        if folder:
            self.source_var.set(folder)

    def pick_target(self) -> None:
        folder = filedialog.askdirectory(initialdir=self.target_var.get())
        if folder:
            self.target_var.set(folder)

    def install(self) -> None:
        manifest = prepare_installation(self.source_var.get(), self.target_var.get())
        messagebox.showinfo("Installation complete", f"Aurora Media Server installed to\n{manifest['target_dir']}")


def main() -> None:
    app = InstallerUI()
    app.mainloop()


if __name__ == "__main__":
    main()
