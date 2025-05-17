import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import warnings

warnings.filterwarnings("ignore", message="No module named 'triton'")

# 1. Tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "checkpoints/mixtral-finetuned/checkpoint-603",
    local_files_only=True,
    trust_remote_code=True
)

# 2. Modèle de base (CPU/MPS compatible)
base_model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    torch_dtype=torch.float32,  # M1/M2 n’a pas float16 efficace sans CUDA
    device_map={"": "mps"} if torch.backends.mps.is_available() else "cpu",
    trust_remote_code=True
)

# 3. Ajout des poids LoRA
model = PeftModel.from_pretrained(
    base_model,
    "checkpoints/mixtral-finetuned/checkpoint-603",
    torch_dtype=torch.float32,
    device_map={"": "mps"} if torch.backends.mps.is_available() else "cpu"
)

# 4. Génération
prompt = "[INST] J'ai mangé 3 pommes et fais 15 minutes de vélo [/INST]"
inputs = tokenizer(prompt, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=100)

# 5. Résultat
print(tokenizer.decode(outputs[0], skip_special_tokens=True))