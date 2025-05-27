@echo off
REM Create virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

echo.
echo ✅ Setup complete. To start using it, run:
echo call venv\Scripts\activate
