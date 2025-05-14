from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
import torch
from huggingface_hub import whoami
print(whoami())

# 🔐 Authenticate with your Hugging Face token (once per session)
# Replace YOUR_TOKEN_HERE with your actual token
#login(token)


# Model info
model_id = "HuggingFaceH4/zephyr-7b-alpha"#"mistralai/Mistral-7B-v0.1"#"mistralai/Mistral-7B-Instruct"

print("🔄 Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("🔄 Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("✅ Creating text generation pipeline...")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Chat loop
while True:
    prompt = input("\n🧙 You: ")
    if prompt.lower() in ['exit', 'quit']:
        break

    print("🔮 Mistral says:\n")
    output = generator(prompt, max_new_tokens=150, do_sample=True)
    print(output[0]["generated_text"])
