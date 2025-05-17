---
library_name: peft
license: apache-2.0
base_model: mistralai/Mixtral-8x7B-Instruct-v0.1
tags:
- generated_from_trainer
datasets:
- data_train/fine_tune_dataset_clean.jsonl
model-index:
- name: checkpoints/mixtral-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.10.0.dev0`
```yaml
# =====================
# 🧠 Base model config
# =====================
base_model: mistralai/Mixtral-8x7B-Instruct-v0.1
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer
trust_remote_code: true
use_auth_token: true

# =====================
# 📚 Dataset
# =====================
datasets:
  - path: data_train/fine_tune_dataset_clean.jsonl
    type: chat_template
    field_messages: messages
    message_field_role: role
    message_field_content: content
    roles_to_train:
      - user
      - assistant
chat_template: mistral_v2v3
val_set_size: 0.01

# =====================
# ⚙️ Adapter training (LoRA + 4-bit)
# =====================
adapter: lora
use_peft: true
load_in_4bit: true
bnb_4bit_quant_type: nf4
use_flash_attention: false

lora_r: 8
lora_alpha: 16
lora_dropout: 0.05
lora_target_modules:
  - q_proj
  - k_proj
  - v_proj
  - o_proj
  - gate_proj
  - up_proj
  - down_proj

# =====================
# 🧪 Training
# =====================
sequence_len: 512
sample_packing: false
pad_to_sequence_len: true

micro_batch_size: 1
gradient_accumulation_steps: 1
num_epochs: 1
learning_rate: 2e-5
optimizer: adamw_torch
lr_scheduler: cosine

use_gradient_checkpointing: true

# =====================
# 💾 Output
# =====================
output_dir: ./checkpoints/mixtral-finetuned
save_safetensors: true

# =====================
# 📊 Experiment tracking
# =====================
wandb_project: mixtral-finetune
wandb_run_name: mixtral-run
```

</details><br>

# checkpoints/mixtral-finetuned

This model is a fine-tuned version of [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) on the data_train/fine_tune_dataset_clean.jsonl dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6278

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 18
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.5456        | 1.0   | 603  | 0.6278          |


### Framework versions

- PEFT 0.15.2
- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.5.1
- Tokenizers 0.21.1