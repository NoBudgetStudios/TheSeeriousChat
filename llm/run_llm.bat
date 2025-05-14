@echo off
REM Check if venv exists
if exist "venv\Scripts\activate.bat" (
    echo ✅ Virtual environment found. Activating...
    call venv\Scripts\activate
) else (
    echo ❌ Virtual environment not found. Running setup...
    call setup_mistral.bat
    call venv\Scripts\activate
)

REM Run the main script
echo 🚀 Launching Mistral chat...
python mistral_local.py
