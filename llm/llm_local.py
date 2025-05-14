from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import os

# ✅ Model: Lightweight, chat-tuned, not gated
model_id = "TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0"

print("🔄 Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("🔄 Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

# ✅ Set pad_token_id to silence warnings
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    pad_token_id=tokenizer.eos_token_id
)

# 🧙 Chat loop
while True:
    prompt = input("\n🧙 You: ")
    if prompt.lower() in ["exit", "quit"]:
        break

    # Chat-style prompt format
    system_prompt = "<|system|>\nYou are a mystical medium who speaks like a medieval bard, channeling wisdom from beyond in poetic.\n"
    user_prompt = f"<|user|>\n{prompt.strip()}\n<|assistant|>\n"
    full_prompt = system_prompt + user_prompt

    print("🔮 Medium says:\n")
    output = generator(full_prompt, max_new_tokens=75, do_sample=True, temperature=1)
    response = output[0]["generated_text"].split("<|assistant|>")[-1].strip()
    print(response)
