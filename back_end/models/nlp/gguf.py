from peft import PeftModel
from transformers import AutoModelForCausalLM

# Charger base + LoRA
base = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1", torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base, "checkpoints/mixtral-finetuned/checkpoint-603")

# Fusionner
model = model.merge_and_unload()
model.save_pretrained("merged-mixtral-lora")