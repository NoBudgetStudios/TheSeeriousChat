# llm_model.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

model_id = "TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0"

print("🔄 Loading tokenizer and model...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    pad_token_id=tokenizer.eos_token_id
)

def generate_mystical_response(prompt: str) -> str:
    system_prompt = "<|system|>\nYou are a mystical medium who speaks like a medieval bard, channeling wisdom from beyond in poetic.\n"
    user_prompt = f"<|user|>\n{prompt.strip()}\n<|assistant|>\n"
    full_prompt = system_prompt + user_prompt

    output = generator(full_prompt, max_new_tokens=100, do_sample=True, temperature=0.7)
    response = output[0]["generated_text"].split("<|assistant|>")[-1].strip()
    return response
