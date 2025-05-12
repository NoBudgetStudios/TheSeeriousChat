
# The Seerious Chat 🔮👻

**A cheeky AI medium that “talks to spirits,” predicts your fate, and keeps things delightfully weird. Not your average chatbot.**

---

## 🚀 What is The Seerious Chat?

The Seerious Chat is a fun and relaxed AI chatbot designed to act like a **mystical medium**.  
It blends foresight, “spirit messages,” and quirky life advice, delivering it all in a chill, mystical tone. Built for good vibes, not serious business.

---

## 🛠️ Stack

- **Backend:** FastAPI (Python)
- **Model:** Hugging Face Inference API (e.g., `mistralai/Mistral-7B-Instruct`)
- **Frontend:** Minimal HTML + JS (optional)
- **Hosting:** Hugging Face Spaces (or free-tier cloud)
- **Testing:** pytest

---
### 📁 Project Structure

<pre>
TheSeeriousChat/
├── app/
│   └── main.py                  # FastAPI app logic
├── static/
│   ├── style.css                # Styling for the frontend
│   └── script.js                # JS handling the chat interaction
├── templates/
│   └── index.html               # HTML frontend template
├── requirements.txt             # Python dependencies
├── README.md                    # Project info and usage
└── venv/                        # (optional) Python virtual environment
</pre>
---

## 💻 How to Run

1️⃣ **Install dependencies:**

```
pip install -r requirements.txt
```

2️⃣ **Set your Hugging Face token:**

```
export HF_TOKEN=your_huggingface_api_token
```

3️⃣ **Run the app:**

```
uvicorn app.main:app --reload
```

4️⃣ **Send a chat message:**

```
POST /chat/
Body: { "message": "What does my future hold?" }
```

---

## 🧪 Run Tests

```
pytest tests/
```

---

## 🌟 Features

- Mystical AI vibes ✨
- Pretends to talk to spirits 👻
- Poetic foresight & life advice 🌙
- Clean + minimal structure 🛠️

---

## 🔒 License

This project is licensed under **CC BY-NC 4.0**.  
You can share and adapt, but **commercial use is not allowed**.  
[Read the full license here.](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 🙌 Credits

Made with ✨ and curiosity by [Your Name].
