
# The Seerious Chat 🔮👻

**A cheeky AI medium that “talks to spirits,” predicts your fate, and keeps things delightfully weird. Not your average chatbot.**

---

## 🚀 What is The Seerious Chat?

The Seerious Chat is a fun and relaxed AI chatbot designed to act like a **mystical medium**.  
It blends foresight, “spirit messages,” and quirky life advice, delivering it all in a chill, mystical tone. Built for good vibes, not serious business.

---

## 🛠️ Stack

- **Backend:** FastAPI (Python)
- **Model:** Local LLM (`TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0`)
- **Frontend:** Minimal HTML + JS
- **Hosting:** Local server / Self-hosted
- **Testing:** pytest (optional)

---
### 📁 Project Structure

<pre>
TheSeeriousChat/
├── app/
│   └── main.py                  # FastAPI app logic
├── static/
│   ├── style.css                # Styling for the frontend
│   └── script.js                # JS handling the chat interaction
├── local offline llm/
│   └── llm_model.py             # TinyLLaMA loading and generation logic
├── local online llm/
│   └── llm_model.py             # TinyLLaMA loading and generation logic
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

This project is licensed under the **MIT License**.  
You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.  
[Read the full license here.](https://opensource.org/licenses/MIT)

---

## 🙌 Credits

Made with ✨ and curiosity by Konstantinos Klimantakis.
