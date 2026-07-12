Aurora Media Server Windows Installer
===================================

This project now includes a Windows-friendly installer workflow.

How to use it on Windows:
1. Open Command Prompt or PowerShell in the project folder.
2. Run:
   py scripts/installer_wizard.py
3. Or run the helper script:
   powershell -ExecutionPolicy Bypass -File .\scripts\build_windows_installer.ps1

What it creates:
- a local install folder with launcher batch files
- a manifest file describing the installation
- desktop/start-menu-friendly launcher assets

Note:
The current environment in this container is Linux-based, so the final native .exe packaging step must be run on a Windows machine.
