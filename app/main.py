from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel  # ✅ required for request body
import os
import random

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/favicon.ico")
def favicon():
    return FileResponse(os.path.join("app", "favicon.ico"))

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ Message model for POST request
class Message(BaseModel):
    message: str

# Function returning static response
def generate_random_reply():
    responses = [
        "The veil between worlds is thin today. 🌫️",
        "A great change approaches you from the mist. 🔮",
        "The spirits murmur… but not all messages are meant to be understood. 👁️",
        "Your fate dances on the edge of shadow and flame. 🕯️",
        "A forgotten name echoes around you. Listen well. 🌀",
        "A black cat has crossed your path... twice. 🐈‍⬛",
        "The stars refuse to answer right now. Try again later. ✨",
        "Something ancient stirs in your soul. 💀",
        "Your question has awoken something. Be cautious. ⚠️",
        "An unexpected encounter lies ahead. Be ready. 🪞",
        "The wind carries whispers, but not all are truthful. 🍃",
        "You are being watched... but not with malice. 👤",
        "A message will arrive when the moon is high. 🌕",
        "You already know the answer. Deep down. 💭",
        "A door will open soon—don't hesitate to walk through. 🚪",
        "Beware of red threads and old promises. 🧵",
        "Your energy calls to someone far away. 📡",
        "The spirits like you today. Don’t waste it. 🎁",
        "Something lost will return—changed. 🔁",
        "The past is not done with you yet. 📜"
    ]
    return random.choice(responses)


@app.post("/chat/")
async def chat_response(msg: Message):
    return {"reply": generate_random_reply()}
