$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$python = 'python'

Write-Host 'Creating Windows installer assets...'
& $python scripts/desktop_installer.py

$dist = Join-Path $root 'dist/windows'
New-Item -ItemType Directory -Force -Path $dist | Out-Null

# Create a simple self-contained launcher batch file for Windows users
@'
@echo off
setlocal
cd /d "%~dp0"
python installer_wizard.py
'@ | Set-Content -Path (Join-Path $dist 'AuroraMediaServerInstaller.bat') -Encoding ascii

Write-Host "Installer assets ready in $dist"
