@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Starting FastAPI server...
uvicorn app.main:app --reload

pause
