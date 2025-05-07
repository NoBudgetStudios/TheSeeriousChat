from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Serve static files if needed (optional)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/favicon.ico")
def favicon():
    return FileResponse(os.path.join("app", "favicon.ico"))

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
