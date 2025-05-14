@echo off
REM Check if venv exists
if exist "venv\Scripts\activate.bat" (
    echo ✅ Virtual environment found. Activating...
    call venv\Scripts\activate
) else (
    echo ❌ Virtual environment not found. Running setup...
    call init_venv.bat
    call venv\Scripts\activate
)

REM Run the main script
echo 🚀 Launching the chat...
python llm_local.py
