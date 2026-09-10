from transformers import AutoTokenizer

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

print("Downloading AI model tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Model tokenizer downloaded successfully!")
from transformers import AutoModelForCausalLM

print("Downloading AI model...")

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)            

print("AI model downloaded successfully!")