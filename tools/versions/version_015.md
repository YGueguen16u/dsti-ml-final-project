# 📁 Project Structure — Version 15
_Generated on 2025-05-16 22:26:34_

├── .github/
│   └── workflows/
│       └── deploy.yml (1.1 Ko)
├── .pytest_cache/
│   ├── v/
│   │   └── cache/
│   │       ├── nodeids (2 o)
│   │       └── stepwise (2 o)
│   ├── .gitignore (37 o)
│   ├── CACHEDIR.TAG (191 o)
│   └── README.md (302 o)
├── axolotl/
│   ├── .github/
│   │   ├── ISSUE_TEMPLATE/
│   │   │   ├── bug-report.yaml (3.4 Ko)
│   │   │   ├── config.yml (294 o)
│   │   │   ├── docs.yml (1.8 Ko)
│   │   │   └── feature-request.yaml (2.4 Ko)
│   │   ├── workflows/
│   │   │   ├── base.yml (3.4 Ko)
│   │   │   ├── docs.yml (892 o)
│   │   │   ├── lint.yml (538 o)
│   │   │   ├── main.yml (6.7 Ko)
│   │   │   ├── multi-gpu-e2e.yml (2.5 Ko)
│   │   │   ├── nightlies.yml (4.0 Ko)
│   │   │   ├── precommit-autoupdate.yml (1.3 Ko)
│   │   │   ├── preview-docs.yml (1.5 Ko)
│   │   │   ├── pypi.yml (1.6 Ko)
│   │   │   ├── tests-nightly.yml (7.4 Ko)
│   │   │   └── tests.yml (11.7 Ko)
│   │   ├── CODE_OF_CONDUCT.md (5.1 Ko)
│   │   ├── CONTRIBUTING.md (3.5 Ko)
│   │   ├── FUNDING.yml (1.0 Ko)
│   │   ├── PULL_REQUEST_TEMPLATE.md (857 o)
│   │   ├── release-drafter.yml (643 o)
│   │   ├── SECURITY.md (407 o)
│   │   └── SUPPORT.md (474 o)
│   ├── .runpod/
│   │   ├── src/
│   │   │   ├── config/
│   │   │   │   └── config.yaml (20.7 Ko)
│   │   │   ├── handler.py (1.7 Ko)
│   │   │   ├── test_input.json (1.5 Ko)
│   │   │   ├── train.py (1.4 Ko)
│   │   │   └── utils.py (2.7 Ko)
│   │   ├── .gitignore (3.0 Ko)
│   │   ├── Dockerfile (606 o)
│   │   ├── hub.json (2.3 Ko)
│   │   ├── README.md (14.5 Ko)
│   │   ├── requirements.txt (341 o)
│   │   ├── test-input.json (2.0 Ko)
│   │   └── tests.json (2.2 Ko)
│   ├── .vscode/
│   │   ├── launch.json (2.1 Ko)
│   │   ├── README.md (118 o)
│   │   └── tasks.json (888 o)
│   ├── cicd/
│   │   ├── cicd.sh (1.5 Ko)
│   │   ├── Dockerfile.jinja (2.1 Ko)
│   │   ├── e2e_tests.py (2.2 Ko)
│   │   ├── multigpu.py (2.2 Ko)
│   │   └── multigpu.sh (757 o)
│   ├── deepspeed_configs/
│   │   ├── zero1.json (484 o)
│   │   ├── zero1_torch_compile.json (552 o)
│   │   ├── zero2.json (574 o)
│   │   ├── zero3.json (798 o)
│   │   ├── zero3_bf16.json (604 o)
│   │   ├── zero3_bf16_cpuoffload_all.json (845 o)
│   │   └── zero3_bf16_cpuoffload_params.json (763 o)
│   ├── devtools/
│   │   ├── dev_chat_template.yml (940 o)
│   │   └── README.md (158 o)
│   ├── docker/
│   │   ├── Dockerfile (1.2 Ko)
│   │   ├── Dockerfile-base (1.7 Ko)
│   │   ├── Dockerfile-base-next (1.5 Ko)
│   │   ├── Dockerfile-base-nightly (1.5 Ko)
│   │   ├── Dockerfile-cloud (1.0 Ko)
│   │   ├── Dockerfile-cloud-no-tmux (905 o)
│   │   └── Dockerfile-tests (1.2 Ko)
│   ├── docs/
│   │   ├── dataset-formats/
│   │   │   ├── conversation.qmd (6.7 Ko)
│   │   │   ├── index.qmd (17.3 Ko)
│   │   │   ├── inst_tune.qmd (3.7 Ko)
│   │   │   ├── pretraining.qmd (764 o)
│   │   │   ├── stepwise_supervised.qmd (683 o)
│   │   │   ├── template_free.qmd (6.3 Ko)
│   │   │   └── tokenized.qmd (910 o)
│   │   ├── images/
│   │   │   ├── 4d-mask.png (238.7 Ko)
│   │   │   └── ray-cluster-dashboard.png (292.3 Ko)
│   │   ├── .gitignore (40 o)
│   │   ├── amd_hpc.qmd (3.3 Ko)
│   │   ├── batch_vs_grad.qmd (3.0 Ko)
│   │   ├── cli.qmd (7.4 Ko)
│   │   ├── config.qmd (34.3 Ko)
│   │   ├── custom_integrations.qmd (3.2 Ko)
│   │   ├── dataset_loading.qmd (6.7 Ko)
│   │   ├── dataset_preprocessing.qmd (2.0 Ko)
│   │   ├── debugging.qmd (14.0 Ko)
│   │   ├── docker.qmd (3.2 Ko)
│   │   ├── faq.qmd (6.2 Ko)
│   │   ├── fsdp_qlora.qmd (1.7 Ko)
│   │   ├── getting-started.qmd (3.7 Ko)
│   │   ├── inference.qmd (2.8 Ko)
│   │   ├── input_output.qmd (200 o)
│   │   ├── installation.qmd (3.4 Ko)
│   │   ├── lora_optims.qmd (4.4 Ko)
│   │   ├── lr_groups.qmd (738 o)
│   │   ├── mac.qmd (608 o)
│   │   ├── multi-gpu.qmd (3.5 Ko)
│   │   ├── multi-node.qmd (2.8 Ko)
│   │   ├── multimodal.qmd (4.2 Ko)
│   │   ├── multipack.qmd (2.0 Ko)
│   │   ├── nccl.qmd (3.0 Ko)
│   │   ├── ray-integration.qmd (3.8 Ko)
│   │   ├── reward_modelling.qmd (2.0 Ko)
│   │   ├── rlhf.qmd (12.3 Ko)
│   │   ├── sequence_parallelism.qmd (3.7 Ko)
│   │   ├── torchao.qmd (731 o)
│   │   └── unsloth.qmd (1.4 Ko)
│   ├── examples/
│   │   ├── cerebras/
│   │   │   ├── btlm-ft.yml (1.5 Ko)
│   │   │   └── qlora.yml (992 o)
│   │   ├── cloud/
│   │   │   └── modal.yaml (523 o)
│   │   ├── code-llama/
│   │   │   ├── 13b/
│   │   │   │   ├── lora.yml (1.0 Ko)
│   │   │   │   └── qlora.yml (1.1 Ko)
│   │   │   ├── 34b/
│   │   │   │   ├── lora.yml (1.0 Ko)
│   │   │   │   └── qlora.yml (1.1 Ko)
│   │   │   ├── 7b/
│   │   │   │   ├── lora.yml (1.0 Ko)
│   │   │   │   └── qlora.yml (1.1 Ko)
│   │   │   └── README.md (769 o)
│   │   ├── cohere/
│   │   │   └── command-r-7b-qlora.yml (1006 o)
│   │   ├── colab-notebooks/
│   │   │   └── colab-axolotl-example.ipynb (14.6 Ko)
│   │   ├── dbrx/
│   │   │   ├── 16bit-lora.yaml (1.5 Ko)
│   │   │   ├── 8bit-lora.yaml (1.5 Ko)
│   │   │   ├── fft-ds-zero3.yaml (924 o)
│   │   │   └── README.md (1.1 Ko)
│   │   ├── deepcoder/
│   │   │   └── deepcoder-14B-preview-lora.yml (1.0 Ko)
│   │   ├── deepcogito/
│   │   │   ├── cogito-v1-preview-llama-3B-lora.yml (1.0 Ko)
│   │   │   └── cogito-v1-preview-qwen-14B-lora.yml (1.0 Ko)
│   │   ├── deepseek-v2/
│   │   │   ├── fft-fsdp-16b.yaml (1.2 Ko)
│   │   │   └── qlora-fsdp-2_5.yaml (1.6 Ko)
│   │   ├── falcon/
│   │   │   ├── config-7b-lora.yml (1.2 Ko)
│   │   │   ├── config-7b-qlora.yml (2.1 Ko)
│   │   │   └── config-7b.yml (1.2 Ko)
│   │   ├── gemma/
│   │   │   └── qlora.yml (1.0 Ko)
│   │   ├── gemma2/
│   │   │   ├── qlora.yml (1.1 Ko)
│   │   │   └── reward-model.yaml (1.0 Ko)
│   │   ├── gemma3/
│   │   │   ├── gemma-3-1b-qlora.yml (1.2 Ko)
│   │   │   ├── gemma-3-4b-qlora.yml (1.1 Ko)
│   │   │   └── gemma-3-4b-vision-qlora.yml (1.2 Ko)
│   │   ├── glm4/
│   │   │   └── qlora-32b.yaml (1.0 Ko)
│   │   ├── gptj/
│   │   │   └── qlora.yml (979 o)
│   │   ├── jamba/
│   │   │   ├── qlora.yaml (1002 o)
│   │   │   ├── qlora_deepspeed.yaml (1.0 Ko)
│   │   │   ├── qlora_fsdp_large.yaml (1.6 Ko)
│   │   │   └── README.md (318 o)
│   │   ├── jeopardy-bot/
│   │   │   └── config.yml (1.0 Ko)
│   │   ├── llama-2/
│   │   │   ├── fft_optimized.yml (1.1 Ko)
│   │   │   ├── gptq-lora.yml (1.3 Ko)
│   │   │   ├── lisa.yml (1.2 Ko)
│   │   │   ├── loftq.yml (1011 o)
│   │   │   ├── lora.yml (1011 o)
│   │   │   ├── qlora-fsdp.yml (1.4 Ko)
│   │   │   ├── qlora.yml (1017 o)
│   │   │   ├── README.md (823 o)
│   │   │   └── relora.yml (990 o)
│   │   ├── llama-3/
│   │   │   ├── fft-8b-liger-fsdp.yaml (1.6 Ko)
│   │   │   ├── fft-8b.yaml (848 o)
│   │   │   ├── instruct-dpo-lora-8b.yml (1.3 Ko)
│   │   │   ├── instruct-lora-8b.yml (1.2 Ko)
│   │   │   ├── lora-1b-deduplicate-dpo.yml (1.7 Ko)
│   │   │   ├── lora-1b-deduplicate-sft.yml (1.2 Ko)
│   │   │   ├── lora-1b-kernels.yml (1.2 Ko)
│   │   │   ├── lora-1b-ray.yml (1.1 Ko)
│   │   │   ├── lora-1b-sample-packing-sequentially.yml (1.2 Ko)
│   │   │   ├── lora-1b.yml (1.0 Ko)
│   │   │   ├── lora-8b.yml (1.1 Ko)
│   │   │   ├── qlora-1b-kto.yaml (1.2 Ko)
│   │   │   ├── qlora-1b.yml (1.1 Ko)
│   │   │   ├── qlora-fsdp-405b.yaml (1.4 Ko)
│   │   │   ├── qlora-fsdp-70b.yaml (1.5 Ko)
│   │   │   ├── qlora.yml (1.0 Ko)
│   │   │   ├── README.md (361 o)
│   │   │   └── sparse-finetuning.yaml (1.5 Ko)
│   │   ├── llama-3-vision/
│   │   │   └── lora-11b.yaml (1.3 Ko)
│   │   ├── llama-4/
│   │   │   ├── do-no-use-fa2/
│   │   │   │   ├── maverick-qlora-fsdp1.yaml (1.9 Ko)
│   │   │   │   ├── scout-qlora-fsdp1.yaml (2.0 Ko)
│   │   │   │   ├── scout-qlora-single-h100.yaml (1.7 Ko)
│   │   │   │   └── scout-vision-qlora-fsdp.yaml (2.0 Ko)
│   │   │   ├── README.md (1.5 Ko)
│   │   │   ├── scout-qlora-flexattn-fsdp2.yaml (1.9 Ko)
│   │   │   ├── scout-qlora-single-h100-flex.yaml (1.9 Ko)
│   │   │   └── scout-vision-qlora-fsdp2-flex.yaml (2.1 Ko)
│   │   ├── llava/
│   │   │   └── lora-7b.yaml (1.1 Ko)
│   │   ├── mamba/
│   │   │   └── config.yml (997 o)
│   │   ├── mistral/
│   │   │   ├── bigstral-ds-zero3.yaml (1.2 Ko)
│   │   │   ├── config.yml (895 o)
│   │   │   ├── lora-mps.yml (1.2 Ko)
│   │   │   ├── lora.yml (1.2 Ko)
│   │   │   ├── mistral-dpo-qlora.yml (1.7 Ko)
│   │   │   ├── mistral-qlora-fsdp.yml (1.5 Ko)
│   │   │   ├── mistral-qlora-orpo.yml (1.3 Ko)
│   │   │   ├── mistral-small-3.1-24B-lora.yml (1.2 Ko)
│   │   │   ├── mixtral-8x22b-qlora-fsdp.yml (1.5 Ko)
│   │   │   ├── mixtral-qlora-fsdp.yml (1.6 Ko)
│   │   │   ├── mixtral.yml (1.6 Ko)
│   │   │   ├── mixtral_22.yml (1.2 Ko)
│   │   │   ├── qlora.yml (1.2 Ko)
│   │   │   └── README.md (419 o)
│   │   ├── mpt-7b/
│   │   │   ├── config.yml (1.2 Ko)
│   │   │   └── README.md (89 o)
│   │   ├── openllama-3b/
│   │   │   ├── config.yml (1.1 Ko)
│   │   │   ├── lora.yml (1.2 Ko)
│   │   │   ├── qlora.yml (1.1 Ko)
│   │   │   └── README.md (294 o)
│   │   ├── orpheus/
│   │   │   ├── finetune.yml (984 o)
│   │   │   └── README.md (9.7 Ko)
│   │   ├── phi/
│   │   │   ├── lora-3.5.yaml (1.2 Ko)
│   │   │   ├── phi-ft.yml (1.1 Ko)
│   │   │   ├── phi-qlora.yml (1.2 Ko)
│   │   │   ├── phi2-ft.yml (1.1 Ko)
│   │   │   ├── phi3-ft-fsdp.yml (1.5 Ko)
│   │   │   ├── phi3-ft.yml (1.2 Ko)
│   │   │   └── README.md (284 o)
│   │   ├── pixtral/
│   │   │   └── lora-12b.yml (1.2 Ko)
│   │   ├── pythia/
│   │   │   └── lora.yml (778 o)
│   │   ├── pythia-12b/
│   │   │   ├── config.yml (1005 o)
│   │   │   └── README.md (205 o)
│   │   ├── qwen/
│   │   │   ├── lora.yml (1.0 Ko)
│   │   │   ├── qlora.yml (1.0 Ko)
│   │   │   ├── qwen2-moe-lora.yaml (953 o)
│   │   │   ├── qwen2-moe-qlora.yaml (994 o)
│   │   │   └── README.md (118 o)
│   │   ├── qwen2/
│   │   │   ├── dpo.yaml (1.0 Ko)
│   │   │   ├── prm.yaml (1.1 Ko)
│   │   │   ├── qlora-fsdp.yaml (1.3 Ko)
│   │   │   └── reward-model.yaml (1.0 Ko)
│   │   ├── qwen2-vl/
│   │   │   └── lora-7b.yaml (1.1 Ko)
│   │   ├── qwen3/
│   │   │   ├── 32b-qlora.yaml (1.3 Ko)
│   │   │   └── qlora-fsdp.yaml (1.3 Ko)
│   │   ├── redpajama/
│   │   │   ├── config-3b.yml (1.1 Ko)
│   │   │   └── README.md (117 o)
│   │   ├── replit-3b/
│   │   │   └── config-lora.yml (906 o)
│   │   ├── stablelm-2/
│   │   │   ├── 1.6b/
│   │   │   │   ├── fft.yml (1.1 Ko)
│   │   │   │   └── lora.yml (1.1 Ko)
│   │   │   └── README.md (1.5 Ko)
│   │   ├── starcoder2/
│   │   │   └── qlora.yml (945 o)
│   │   ├── tiny-llama/
│   │   │   ├── lora-mps.yml (1.0 Ko)
│   │   │   ├── lora.yml (1006 o)
│   │   │   ├── pretrain.yml (875 o)
│   │   │   ├── qlora.yml (1.0 Ko)
│   │   │   └── README.md (319 o)
│   │   ├── xgen-7b/
│   │   │   └── xgen-7b-8k-qlora.yml (2.1 Ko)
│   │   └── yi-34B-chat/
│   │       ├── qlora.yml (1.1 Ko)
│   │       └── README.md (348 o)
│   ├── image/
│   │   ├── axolotl-badge-web-legacy.png (11.4 Ko)
│   │   ├── axolotl-badge-web.png (24.5 Ko)
│   │   ├── axolotl.png (934.7 Ko)
│   │   ├── axolotl_logo_digital_black.svg (3.2 Ko)
│   │   ├── axolotl_logo_digital_white.svg (6.6 Ko)
│   │   ├── axolotl_symbol_digital_black.svg (1.6 Ko)
│   │   ├── axolotl_symbol_digital_white.svg (5.0 Ko)
│   │   ├── axolotl_wordmark_digital_black.svg (2.1 Ko)
│   │   ├── axolotl_wordmark_digital_white.svg (2.3 Ko)
│   │   └── sticker_fixed.png (370.4 Ko)
│   ├── scripts/
│   │   ├── chat_datasets.py (1.8 Ko)
│   │   ├── cloud-entrypoint-term.sh (2.3 Ko)
│   │   ├── cloud-entrypoint.sh (2.3 Ko)
│   │   ├── cutcrossentropy_install.py (814 o)
│   │   ├── motd (1.3 Ko)
│   │   └── unsloth_install.py (1.0 Ko)
│   ├── src/
│   │   ├── axolotl/
│   │   │   ├── cli/
│   │   │   │   ├── cloud/
│   │   │   │   │   ├── __init__.py (1.7 Ko)
│   │   │   │   │   ├── base.py (374 o)
│   │   │   │   │   └── modal_.py (10.1 Ko)
│   │   │   │   ├── __init__.py (173 o)
│   │   │   │   ├── args.py (3.5 Ko)
│   │   │   │   ├── art.py (1.3 Ko)
│   │   │   │   ├── checks.py (1.6 Ko)
│   │   │   │   ├── config.py (7.8 Ko)
│   │   │   │   ├── delinearize_llama4.py (5.6 Ko)
│   │   │   │   ├── evaluate.py (2.2 Ko)
│   │   │   │   ├── inference.py (8.5 Ko)
│   │   │   │   ├── main.py (11.2 Ko)
│   │   │   │   ├── merge_lora.py (3.3 Ko)
│   │   │   │   ├── merge_sharded_fsdp_weights.py (7.8 Ko)
│   │   │   │   ├── preprocess.py (3.4 Ko)
│   │   │   │   ├── sweeps.py (2.8 Ko)
│   │   │   │   ├── train.py (4.1 Ko)
│   │   │   │   ├── utils.py (10.0 Ko)
│   │   │   │   └── vllm_serve.py (1.6 Ko)
│   │   │   ├── common/
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── architectures.py (355 o)
│   │   │   │   ├── const.py (86 o)
│   │   │   │   └── datasets.py (4.7 Ko)
│   │   │   ├── core/
│   │   │   │   ├── chat/
│   │   │   │   │   ├── format/
│   │   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   │   ├── chatml.py (902 o)
│   │   │   │   │   │   ├── llama3x.py (1.1 Ko)
│   │   │   │   │   │   └── shared.py (1.9 Ko)
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── messages.py (7.3 Ko)
│   │   │   │   ├── datasets/
│   │   │   │   │   ├── transforms/
│   │   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   │   └── chat_builder.py (5.1 Ko)
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── chat.py (1.5 Ko)
│   │   │   │   ├── trainers/
│   │   │   │   │   ├── dpo/
│   │   │   │   │   │   ├── __init__.py (1010 o)
│   │   │   │   │   │   ├── args.py (277 o)
│   │   │   │   │   │   └── trainer.py (9.5 Ko)
│   │   │   │   │   ├── grpo/
│   │   │   │   │   │   ├── __init__.py (5.9 Ko)
│   │   │   │   │   │   ├── args.py (295 o)
│   │   │   │   │   │   └── trainer.py (2.8 Ko)
│   │   │   │   │   ├── mixins/
│   │   │   │   │   │   ├── __init__.py (299 o)
│   │   │   │   │   │   ├── optimizer.py (8.1 Ko)
│   │   │   │   │   │   ├── rng_state_loader.py (2.4 Ko)
│   │   │   │   │   │   ├── scheduler.py (5.7 Ko)
│   │   │   │   │   │   └── sequence_parallel.py (11.0 Ko)
│   │   │   │   │   ├── __init__.py (439 o)
│   │   │   │   │   ├── base.py (23.0 Ko)
│   │   │   │   │   ├── mamba.py (873 o)
│   │   │   │   │   ├── relora.py (1.4 Ko)
│   │   │   │   │   ├── trl.py (8.5 Ko)
│   │   │   │   │   └── utils.py (1.2 Ko)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── trainer_builder.py (48.5 Ko)
│   │   │   │   └── training_args.py (9.0 Ko)
│   │   │   ├── integrations/
│   │   │   │   ├── cut_cross_entropy/
│   │   │   │   │   ├── monkeypatch/
│   │   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   │   ├── cohere.py (7.4 Ko)
│   │   │   │   │   │   ├── gemma.py (6.2 Ko)
│   │   │   │   │   │   ├── gemma3.py (18.2 Ko)
│   │   │   │   │   │   ├── glm4.py (1.9 Ko)
│   │   │   │   │   │   ├── llama.py (6.1 Ko)
│   │   │   │   │   │   ├── llama4.py (15.9 Ko)
│   │   │   │   │   │   ├── mistral3.py (15.4 Ko)
│   │   │   │   │   │   ├── mllama.py (14.5 Ko)
│   │   │   │   │   │   ├── patch.py (4.1 Ko)
│   │   │   │   │   │   ├── qwen2.py (1.2 Ko)
│   │   │   │   │   │   ├── qwen2_5_vl.py (9.8 Ko)
│   │   │   │   │   │   ├── qwen2_moe.py (6.7 Ko)
│   │   │   │   │   │   ├── qwen2_vl.py (9.9 Ko)
│   │   │   │   │   │   ├── qwen3.py (1.2 Ko)
│   │   │   │   │   │   ├── qwen3_moe.py (6.8 Ko)
│   │   │   │   │   │   └── utils.py (1.0 Ko)
│   │   │   │   │   ├── __init__.py (2.9 Ko)
│   │   │   │   │   ├── ACKNOWLEDGEMENTS.md (16.4 Ko)
│   │   │   │   │   ├── args.py (1.3 Ko)
│   │   │   │   │   ├── LICENSE (2.6 Ko)
│   │   │   │   │   └── README.md (1.4 Ko)
│   │   │   │   ├── grokfast/
│   │   │   │   │   ├── __init__.py (1.4 Ko)
│   │   │   │   │   ├── args.py (274 o)
│   │   │   │   │   ├── LICENSE (1.1 Ko)
│   │   │   │   │   ├── optimizer.py (1.9 Ko)
│   │   │   │   │   └── README.md (455 o)
│   │   │   │   ├── kd/
│   │   │   │   │   ├── kernels/
│   │   │   │   │   │   └── __init__.py (0 o)
│   │   │   │   │   ├── topk_logprob/
│   │   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   │   └── forward_kl.py (8.9 Ko)
│   │   │   │   │   ├── __init__.py (1.1 Ko)
│   │   │   │   │   ├── args.py (1.3 Ko)
│   │   │   │   │   ├── chat_template.py (7.3 Ko)
│   │   │   │   │   ├── collator.py (10.6 Ko)
│   │   │   │   │   ├── README.md (616 o)
│   │   │   │   │   └── trainer.py (4.2 Ko)
│   │   │   │   ├── liger/
│   │   │   │   │   ├── models/
│   │   │   │   │   │   ├── deepseekv2.py (4.5 Ko)
│   │   │   │   │   │   ├── jamba.py (6.2 Ko)
│   │   │   │   │   │   ├── llama4.py (6.9 Ko)
│   │   │   │   │   │   ├── qwen3.py (6.0 Ko)
│   │   │   │   │   │   └── qwen3_moe.py (7.2 Ko)
│   │   │   │   │   ├── __init__.py (8.0 Ko)
│   │   │   │   │   ├── args.py (1.8 Ko)
│   │   │   │   │   ├── LICENSE (11.1 Ko)
│   │   │   │   │   ├── README.md (1.2 Ko)
│   │   │   │   │   └── utils.py (804 o)
│   │   │   │   ├── llm_compressor/
│   │   │   │   │   ├── __init__.py (136 o)
│   │   │   │   │   ├── args.py (999 o)
│   │   │   │   │   ├── plugin.py (5.5 Ko)
│   │   │   │   │   ├── README.md (3.8 Ko)
│   │   │   │   │   └── utils.py (1.2 Ko)
│   │   │   │   ├── lm_eval/
│   │   │   │   │   ├── __init__.py (1.2 Ko)
│   │   │   │   │   ├── args.py (373 o)
│   │   │   │   │   ├── cli.py (3.9 Ko)
│   │   │   │   │   └── README.md (1.1 Ko)
│   │   │   │   ├── spectrum/
│   │   │   │   │   ├── model_snr_results/
│   │   │   │   │   │   ├── snr_results_google-gemma-2-2b.json (33.1 Ko)
│   │   │   │   │   │   ├── snr_results_meta-llama-Llama-3.2-1B-Instruct.json (16.4 Ko)
│   │   │   │   │   │   ├── snr_results_meta-llama-Llama-3.2-1B.json (16.5 Ko)
│   │   │   │   │   │   ├── snr_results_meta-llama-Llama-3.2-3B-Instruct.json (28.7 Ko)
│   │   │   │   │   │   ├── snr_results_meta-llama-Llama-3.2-3B.json (28.7 Ko)
│   │   │   │   │   │   ├── snr_results_Qwen-Qwen2.5-1.5B-Instruct.json (28.5 Ko)
│   │   │   │   │   │   ├── snr_results_Qwen-Qwen2.5-1.5B.json (28.5 Ko)
│   │   │   │   │   │   ├── snr_results_Qwen-Qwen2.5-3B-Instruct.json (36.5 Ko)
│   │   │   │   │   │   ├── snr_results_Qwen-Qwen2.5-3B.json (36.5 Ko)
│   │   │   │   │   │   ├── snr_results_Qwen-Qwen2.5-7B-Instruct.json (28.5 Ko)
│   │   │   │   │   │   └── snr_results_Qwen-Qwen2.5-7B.json (28.5 Ko)
│   │   │   │   │   ├── __init__.py (3.8 Ko)
│   │   │   │   │   ├── args.py (1.5 Ko)
│   │   │   │   │   ├── LICENSE (11.1 Ko)
│   │   │   │   │   └── README.md (1.1 Ko)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── base.py (18.6 Ko)
│   │   │   │   ├── config.py (2.6 Ko)
│   │   │   │   └── LICENSE.md (4.8 Ko)
│   │   │   ├── kernels/
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── geglu.py (5.0 Ko)
│   │   │   │   ├── lora.py (22.1 Ko)
│   │   │   │   ├── quantize.py (4.7 Ko)
│   │   │   │   ├── swiglu.py (5.3 Ko)
│   │   │   │   └── utils.py (401 o)
│   │   │   ├── models/
│   │   │   │   ├── mamba/
│   │   │   │   │   ├── __init__.py (656 o)
│   │   │   │   │   ├── configuration_mamba.py (1.1 Ko)
│   │   │   │   │   └── modeling_mamba.py (4.4 Ko)
│   │   │   │   └── __init__.py (0 o)
│   │   │   ├── monkeypatch/
│   │   │   │   ├── accelerate/
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── fsdp2.py (2.3 Ko)
│   │   │   │   ├── attention/
│   │   │   │   │   ├── ring_attn/
│   │   │   │   │   │   ├── adapters/
│   │   │   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   │   │   └── batch.py (7.2 Ko)
│   │   │   │   │   │   ├── __init__.py (242 o)
│   │   │   │   │   │   └── patch.py (4.5 Ko)
│   │   │   │   │   ├── __init__.py (557 o)
│   │   │   │   │   ├── flex_attn.py (7.3 Ko)
│   │   │   │   │   ├── mllama.py (8.6 Ko)
│   │   │   │   │   └── xformers.py (6.0 Ko)
│   │   │   │   ├── mixtral/
│   │   │   │   │   └── __init__.py (2.0 Ko)
│   │   │   │   ├── models/
│   │   │   │   │   └── llama4/
│   │   │   │   │       ├── __init__.py (0 o)
│   │   │   │   │       └── modeling.py (3.5 Ko)
│   │   │   │   ├── peft/
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── utils.py (2.6 Ko)
│   │   │   │   ├── trainer/
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── lr.py (1.4 Ko)
│   │   │   │   ├── xformers_/
│   │   │   │   │   └── __init__.py (1.6 Ko)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── btlm_attn_hijack_flash.py (2.3 Ko)
│   │   │   │   ├── gemma3.py (9.2 Ko)
│   │   │   │   ├── llama_attn_hijack_flash.py (30.9 Ko)
│   │   │   │   ├── llama_attn_hijack_xformers.py (5.4 Ko)
│   │   │   │   ├── llama_expand_mask.py (673 o)
│   │   │   │   ├── llama_patch_multipack.py (1.0 Ko)
│   │   │   │   ├── lora_kernels.py (14.9 Ko)
│   │   │   │   ├── mistral_attn_hijack_flash.py (22.3 Ko)
│   │   │   │   ├── multipack.py (1.9 Ko)
│   │   │   │   ├── relora.py (17.0 Ko)
│   │   │   │   ├── stablelm_attn_hijack_flash.py (15.1 Ko)
│   │   │   │   ├── trainer_accelerator_args.py (2.4 Ko)
│   │   │   │   ├── trainer_eval_guard.py (2.0 Ko)
│   │   │   │   ├── trainer_fsdp_optim.py (2.2 Ko)
│   │   │   │   ├── transformers_fa_utils.py (2.4 Ko)
│   │   │   │   ├── unsloth_.py (9.0 Ko)
│   │   │   │   └── utils.py (8.2 Ko)
│   │   │   ├── prompt_strategies/
│   │   │   │   ├── bradley_terry/
│   │   │   │   │   ├── __init__.py (1.2 Ko)
│   │   │   │   │   ├── chat_template.py (4.3 Ko)
│   │   │   │   │   ├── llama3.py (1.0 Ko)
│   │   │   │   │   └── README.md (193 o)
│   │   │   │   ├── dpo/
│   │   │   │   │   ├── __init__.py (199 o)
│   │   │   │   │   ├── chat_template.py (3.2 Ko)
│   │   │   │   │   ├── chatml.py (4.8 Ko)
│   │   │   │   │   ├── llama3.py (5.5 Ko)
│   │   │   │   │   ├── passthrough.py (345 o)
│   │   │   │   │   ├── user_defined.py (1.5 Ko)
│   │   │   │   │   └── zephyr.py (547 o)
│   │   │   │   ├── kto/
│   │   │   │   │   ├── __init__.py (199 o)
│   │   │   │   │   ├── chatml.py (3.3 Ko)
│   │   │   │   │   ├── llama3.py (3.8 Ko)
│   │   │   │   │   └── user_defined.py (1.4 Ko)
│   │   │   │   ├── messages/
│   │   │   │   │   ├── __init__.py (1.1 Ko)
│   │   │   │   │   └── chat.py (3.1 Ko)
│   │   │   │   ├── orpo/
│   │   │   │   │   ├── __init__.py (201 o)
│   │   │   │   │   └── chat_template.py (9.1 Ko)
│   │   │   │   ├── __init__.py (1.8 Ko)
│   │   │   │   ├── alpaca_chat.py (3.6 Ko)
│   │   │   │   ├── alpaca_instruct.py (638 o)
│   │   │   │   ├── alpaca_w_system.py (5.4 Ko)
│   │   │   │   ├── base.py (1.1 Ko)
│   │   │   │   ├── chat_template.py (30.8 Ko)
│   │   │   │   ├── completion.py (2.5 Ko)
│   │   │   │   ├── context_qa.py (3.1 Ko)
│   │   │   │   ├── creative_acr.py (6.4 Ko)
│   │   │   │   ├── input_output.py (1.7 Ko)
│   │   │   │   ├── jinja_template_analyzer.py (12.1 Ko)
│   │   │   │   ├── llama2_chat.py (8.0 Ko)
│   │   │   │   ├── metharme.py (2.4 Ko)
│   │   │   │   ├── orcamini.py (1.5 Ko)
│   │   │   │   ├── pretrain.py (1.7 Ko)
│   │   │   │   ├── pygmalion.py (3.5 Ko)
│   │   │   │   ├── stepwise_supervised.py (3.9 Ko)
│   │   │   │   └── user_defined.py (2.6 Ko)
│   │   │   ├── utils/
│   │   │   │   ├── callbacks/
│   │   │   │   │   ├── __init__.py (35.1 Ko)
│   │   │   │   │   ├── comet_.py (1.5 Ko)
│   │   │   │   │   ├── lisa.py (3.1 Ko)
│   │   │   │   │   ├── mlflow_.py (1.6 Ko)
│   │   │   │   │   ├── perplexity.py (2.4 Ko)
│   │   │   │   │   └── profiler.py (1.4 Ko)
│   │   │   │   ├── collators/
│   │   │   │   │   ├── __init__.py (319 o)
│   │   │   │   │   ├── batching.py (8.8 Ko)
│   │   │   │   │   ├── core.py (61 o)
│   │   │   │   │   ├── mamba.py (966 o)
│   │   │   │   │   └── mm_chat.py (2.7 Ko)
│   │   │   │   ├── config/
│   │   │   │   │   ├── models/
│   │   │   │   │   │   └── __init__.py (0 o)
│   │   │   │   │   └── __init__.py (10.5 Ko)
│   │   │   │   ├── gradient_checkpointing/
│   │   │   │   │   ├── __init__.py (1.1 Ko)
│   │   │   │   │   └── unsloth.py (2.2 Ko)
│   │   │   │   ├── optimizers/
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── adopt.py (19.5 Ko)
│   │   │   │   ├── samplers/
│   │   │   │   │   ├── __init__.py (145 o)
│   │   │   │   │   ├── multipack.py (15.6 Ko)
│   │   │   │   │   └── utils.py (675 o)
│   │   │   │   ├── schemas/
│   │   │   │   │   ├── internal/
│   │   │   │   │   │   └── __init__.py (559 o)
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   ├── config.py (52.9 Ko)
│   │   │   │   │   ├── datasets.py (5.3 Ko)
│   │   │   │   │   ├── deprecated.py (2.3 Ko)
│   │   │   │   │   ├── enums.py (2.5 Ko)
│   │   │   │   │   ├── integrations.py (3.1 Ko)
│   │   │   │   │   ├── model.py (1.6 Ko)
│   │   │   │   │   ├── multimodal.py (1.9 Ko)
│   │   │   │   │   ├── peft.py (4.4 Ko)
│   │   │   │   │   ├── training.py (3.3 Ko)
│   │   │   │   │   ├── trl.py (5.6 Ko)
│   │   │   │   │   ├── utils.py (3.1 Ko)
│   │   │   │   │   └── vllm.py (1.4 Ko)
│   │   │   │   ├── __init__.py (1.5 Ko)
│   │   │   │   ├── bench.py (3.1 Ko)
│   │   │   │   ├── chat_templates.py (47.9 Ko)
│   │   │   │   ├── comet_.py (3.5 Ko)
│   │   │   │   ├── dict.py (1.2 Ko)
│   │   │   │   ├── distributed.py (8.7 Ko)
│   │   │   │   ├── environment.py (805 o)
│   │   │   │   ├── freeze.py (8.3 Ko)
│   │   │   │   ├── lora.py (3.0 Ko)
│   │   │   │   ├── lora_embeddings.py (375 o)
│   │   │   │   ├── mlflow_.py (706 o)
│   │   │   │   ├── model_shard_quant.py (9.5 Ko)
│   │   │   │   ├── models.py (62.7 Ko)
│   │   │   │   ├── schedulers.py (10.2 Ko)
│   │   │   │   ├── tokenization.py (4.1 Ko)
│   │   │   │   ├── trainer.py (22.5 Ko)
│   │   │   │   └── wandb_.py (609 o)
│   │   │   ├── __init__.py (188 o)
│   │   │   ├── convert.py (1.8 Ko)
│   │   │   ├── datasets.py (8.1 Ko)
│   │   │   ├── evaluate.py (4.7 Ko)
│   │   │   ├── logging_config.py (1.9 Ko)
│   │   │   ├── processing_strategies.py (10.5 Ko)
│   │   │   ├── prompt_tokenizers.py (10.7 Ko)
│   │   │   ├── prompters.py (10.6 Ko)
│   │   │   └── train.py (19.1 Ko)
│   │   ├── axolotl.egg-info/
│   │   │   ├── dependency_links.txt (56 o)
│   │   │   ├── entry_points.txt (50 o)
│   │   │   ├── PKG-INFO (11.9 Ko)
│   │   │   ├── requires.txt (1.2 Ko)
│   │   │   ├── SOURCES.txt (10.7 Ko)
│   │   │   └── top_level.txt (48 o)
│   │   └── setuptools_axolotl_dynamic_dependencies.py (4.4 Ko)
│   ├── tests/
│   │   ├── cli/
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── conftest.py (683 o)
│   │   │   ├── test_cli_base.py (2.3 Ko)
│   │   │   ├── test_cli_evaluate.py (2.2 Ko)
│   │   │   ├── test_cli_fetch.py (1.4 Ko)
│   │   │   ├── test_cli_inference.py (903 o)
│   │   │   ├── test_cli_interface.py (1.2 Ko)
│   │   │   ├── test_cli_merge_lora.py (1.9 Ko)
│   │   │   ├── test_cli_merge_sharded_fsdp_weights.py (655 o)
│   │   │   ├── test_cli_preprocess.py (2.7 Ko)
│   │   │   ├── test_cli_sweeps.py (1.7 Ko)
│   │   │   ├── test_cli_train.py (2.7 Ko)
│   │   │   ├── test_cli_version.py (313 o)
│   │   │   └── test_utils.py (2.2 Ko)
│   │   ├── core/
│   │   │   ├── chat/
│   │   │   │   ├── format/
│   │   │   │   │   └── __init__.py (0 o)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   └── test_messages.py (7.0 Ko)
│   │   │   └── test_trainer_builder.py (1.9 Ko)
│   │   ├── e2e/
│   │   │   ├── integrations/
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── test_cut_cross_entropy.py (4.5 Ko)
│   │   │   │   ├── test_hooks.py (6.7 Ko)
│   │   │   │   ├── test_kd.py (4.0 Ko)
│   │   │   │   ├── test_liger.py (3.8 Ko)
│   │   │   │   └── test_llm_compressor.py (3.8 Ko)
│   │   │   ├── kernels/
│   │   │   │   ├── test_geglu.py (2.5 Ko)
│   │   │   │   ├── test_lora.py (15.2 Ko)
│   │   │   │   ├── test_quantize.py (2.9 Ko)
│   │   │   │   └── test_swiglu.py (2.6 Ko)
│   │   │   ├── multigpu/
│   │   │   │   ├── patched/
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── test_sp.py (4.4 Ko)
│   │   │   │   ├── solo/
│   │   │   │   │   ├── __init__.py (138 o)
│   │   │   │   │   ├── test_flex.py (2.8 Ko)
│   │   │   │   │   └── test_grpo.py (11.6 Ko)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── test_eval.py (5.4 Ko)
│   │   │   │   ├── test_gemma3.py (3.1 Ko)
│   │   │   │   ├── test_llama.py (31.7 Ko)
│   │   │   │   ├── test_qwen2.py (3.2 Ko)
│   │   │   │   └── test_ray.py (4.4 Ko)
│   │   │   ├── patched/
│   │   │   │   ├── lora_kernels/
│   │   │   │   │   ├── __init__.py (0 o)
│   │   │   │   │   └── test_lora_kernel_patching.py (14.5 Ko)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── test_4d_multipack_llama.py (3.9 Ko)
│   │   │   │   ├── test_activation_checkpointing.py (2.4 Ko)
│   │   │   │   ├── test_cli_integrations.py (1.5 Ko)
│   │   │   │   ├── test_fa_xentropy.py (2.8 Ko)
│   │   │   │   ├── test_falcon_samplepack.py (3.8 Ko)
│   │   │   │   ├── test_fused_llama.py (2.2 Ko)
│   │   │   │   ├── test_llama_s2_attention.py (3.7 Ko)
│   │   │   │   ├── test_lora_llama_multipack.py (4.1 Ko)
│   │   │   │   ├── test_mistral_samplepack.py (3.6 Ko)
│   │   │   │   ├── test_mixtral_samplepack.py (3.5 Ko)
│   │   │   │   ├── test_model_patches.py (2.9 Ko)
│   │   │   │   ├── test_peft_embeddings.py (2.0 Ko)
│   │   │   │   ├── test_phi_multipack.py (3.9 Ko)
│   │   │   │   ├── test_resume.py (3.1 Ko)
│   │   │   │   ├── test_sp.py (14.2 Ko)
│   │   │   │   ├── test_unsloth_integration.py (737 o)
│   │   │   │   └── test_unsloth_qlora.py (6.1 Ko)
│   │   │   ├── solo/
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── test_flex.py (2.2 Ko)
│   │   │   │   └── test_relora_llama.py (3.0 Ko)
│   │   │   ├── .gitignore (18 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── test_deepseekv3.py (4.5 Ko)
│   │   │   ├── test_dpo.py (13.7 Ko)
│   │   │   ├── test_embeddings_lr.py (3.6 Ko)
│   │   │   ├── test_evaluate.py (1.9 Ko)
│   │   │   ├── test_falcon.py (5.7 Ko)
│   │   │   ├── test_gemma2.py (4.5 Ko)
│   │   │   ├── test_gemma3_text.py (4.3 Ko)
│   │   │   ├── test_imports.py (642 o)
│   │   │   ├── test_llama.py (7.0 Ko)
│   │   │   ├── test_llama_pretrain.py (2.6 Ko)
│   │   │   ├── test_llama_vision.py (4.1 Ko)
│   │   │   ├── test_load_model.py (3.0 Ko)
│   │   │   ├── test_lora_llama.py (2.0 Ko)
│   │   │   ├── test_mamba.py (2.1 Ko)
│   │   │   ├── test_mistral.py (3.7 Ko)
│   │   │   ├── test_mixtral.py (9.6 Ko)
│   │   │   ├── test_optimizers.py (8.3 Ko)
│   │   │   ├── test_packing_loss.py (2.1 Ko)
│   │   │   ├── test_phi.py (3.9 Ko)
│   │   │   ├── test_process_reward_model_smollm2.py (2.2 Ko)
│   │   │   ├── test_qwen.py (2.8 Ko)
│   │   │   ├── test_reward_model_smollm2.py (2.6 Ko)
│   │   │   ├── test_schedulers.py (2.1 Ko)
│   │   │   └── utils.py (4.8 Ko)
│   │   ├── fixtures/
│   │   │   ├── alpaca/
│   │   │   │   └── alpaca.json (680 o)
│   │   │   ├── conversation.json (8.8 Ko)
│   │   │   ├── conversation.missingturns.json (8.2 Ko)
│   │   │   ├── conversation.tokenized.json (28.1 Ko)
│   │   │   └── conversation.tokenized_llama2chat.json (67.2 Ko)
│   │   ├── integrations/
│   │   │   ├── __init__.py (0 o)
│   │   │   └── test_liger.py (2.3 Ko)
│   │   ├── monkeypatch/
│   │   │   └── test_llama_attn_hijack_flash.py (3.6 Ko)
│   │   ├── patched/
│   │   │   └── test_validation.py (45.9 Ko)
│   │   ├── prompt_strategies/
│   │   │   ├── messages/
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   └── test_chat.py (1.9 Ko)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── conftest.py (11.2 Ko)
│   │   │   ├── test_alpaca.py (4.6 Ko)
│   │   │   ├── test_chat_template_utils.py (4.5 Ko)
│   │   │   ├── test_chat_templates.py (24.7 Ko)
│   │   │   ├── test_chat_templates_advanced.py (47.8 Ko)
│   │   │   ├── test_chat_templates_thinking.py (4.3 Ko)
│   │   │   ├── test_dpo_chat_templates.py (7.2 Ko)
│   │   │   ├── test_dpo_chatml.py (1.8 Ko)
│   │   │   ├── test_jinja_template_analyzer.py (5.8 Ko)
│   │   │   ├── test_raw_io.py (2.9 Ko)
│   │   │   └── test_stepwise.py (2.2 Ko)
│   │   ├── utils/
│   │   │   ├── __init__.py (0 o)
│   │   │   └── test_models.py (7.0 Ko)
│   │   ├── __init__.py (0 o)
│   │   ├── conftest.py (16.9 Ko)
│   │   ├── constants.py (934 o)
│   │   ├── hf_offline_utils.py (3.3 Ko)
│   │   ├── test_data.py (2.2 Ko)
│   │   ├── test_datasets.py (16.6 Ko)
│   │   ├── test_dict.py (3.1 Ko)
│   │   ├── test_exact_deduplication.py (17.6 Ko)
│   │   ├── test_expand_mask.py (1.4 Ko)
│   │   ├── test_freeze.py (8.7 Ko)
│   │   ├── test_lora.py (2.0 Ko)
│   │   ├── test_normalize_config.py (2.6 Ko)
│   │   ├── test_packed_batch_sampler.py (3.3 Ko)
│   │   ├── test_packed_dataset.py (2.3 Ko)
│   │   ├── test_packed_pretraining.py (3.5 Ko)
│   │   ├── test_perplexity.py (2.8 Ko)
│   │   ├── test_prompt_tokenizers.py (8.7 Ko)
│   │   ├── test_prompters.py (4.7 Ko)
│   │   ├── test_schedulers.py (1.8 Ko)
│   │   ├── test_tokenizers.py (4.8 Ko)
│   │   └── test_validation_dataset.py (11.1 Ko)
│   ├── .bandit (38 o)
│   ├── .coveragerc (213 o)
│   ├── .editorconfig (186 o)
│   ├── .flake8 (88 o)
│   ├── .gitattributes (49 o)
│   ├── .gitignore (3.3 Ko)
│   ├── .isort.cfg (87 o)
│   ├── .mypy.ini (899 o)
│   ├── .pre-commit-config.yaml (998 o)
│   ├── .pylintrc (697 o)
│   ├── _quarto.yml (7.8 Ko)
│   ├── CNAME (16 o)
│   ├── codecov.yml (1019 o)
│   ├── docker-compose.yaml (701 o)
│   ├── FAQS.md (648 o)
│   ├── favicon.jpg (4.5 Ko)
│   ├── index.qmd (487 o)
│   ├── LICENSE (11.1 Ko)
│   ├── MANIFEST.in (145 o)
│   ├── pyproject.toml (757 o)
│   ├── README.md (8.8 Ko)
│   ├── requirements-dev.txt (73 o)
│   ├── requirements-tests.txt (85 o)
│   ├── requirements.txt (1.0 Ko)
│   ├── setup.py (5.7 Ko)
│   ├── styles.css (4.9 Ko)
│   └── TODO.md (262 o)
├── back_end/
│   ├── api/
│   │   ├── dependencies/
│   │   │   ├── __init__.py (0 o)
│   │   │   └── auth.py (3.0 Ko)
│   │   ├── routes/
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── activity_schema.json (4.9 Ko)
│   │   │   ├── daily_log.py (2.6 Ko)
│   │   │   └── user.py (3.2 Ko)
│   │   └── __init__.py (0 o)
│   ├── config/
│   │   ├── __init__.py (0 o)
│   │   ├── mixtral-finetune.yaml (1.1 Ko)
│   │   └── settings.py (1.2 Ko)
│   ├── data_pipeline/
│   │   ├── dags/
│   │   │   └── __init__.py (0 o)
│   │   ├── scripts/
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── analyze_cleaned_data.py (4.5 Ko)
│   │   │   ├── clean_nutrition_data.py (3.3 Ko)
│   │   │   └── load_nutrition_dataset.py (3.1 Ko)
│   │   ├── utils/
│   │   │   └── __init__.py (0 o)
│   │   └── __init__.py (0 o)
│   ├── database/
│   │   ├── models/
│   │   │   ├── __init__.py (284 o)
│   │   │   ├── activity_log.py (3.2 Ko)
│   │   │   ├── base.py (885 o)
│   │   │   ├── meal_log.py (1.6 Ko)
│   │   │   ├── shared_config.py (1.8 Ko)
│   │   │   ├── user_config.py (1.9 Ko)
│   │   │   └── user_daily_log.py (1.3 Ko)
│   │   ├── queries/
│   │   │   └── __init__.py (0 o)
│   │   ├── repository/
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── user_daily_log_repository.py (970 o)
│   │   │   └── user_repository.py (4.8 Ko)
│   │   ├── __init__.py (0 o)
│   │   ├── connect.py (1.9 Ko)
│   │   ├── initialize_db.py (1.6 Ko)
│   │   ├── models.py (3.9 Ko)
│   │   ├── reset.sql.py (720 o)
│   │   └── seed_postgres.py (2.0 Ko)
│   ├── models/
│   │   ├── model_utils/
│   │   │   └── __init__.py (0 o)
│   │   ├── nlp/
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── gguf.py (385 o)
│   │   │   ├── model_training.py (519 o)
│   │   │   └── s3_nlp_manager.py (1.2 Ko)
│   │   ├── regression/
│   │   │   └── __init__.py (0 o)
│   │   ├── vision/
│   │   │   └── __init__.py (0 o)
│   │   ├── __init__.py (0 o)
│   │   └── calories_calculator_function.py (4.0 Ko)
│   ├── services/
│   │   ├── __init__.py (0 o)
│   │   ├── product_searcher.py (2.0 Ko)
│   │   └── user_service.py (123 o)
│   ├── __init__.py (0 o)
│   ├── main.py (3.2 Ko)
│   └── show_tables.py (529 o)
├── best-practices/
│   ├── git/
│   │   ├── git-commands-basics.md (1.6 Ko)
│   │   └── gitkeep.md (1.1 Ko)
│   ├── personnal/
│   │   ├── 00_log/
│   │   │   └── 00_log_2025/
│   │   │       ├── 04/
│   │   │       │   └── 10/
│   │   │       │       ├── 12h10.md (1.4 Ko)
│   │   │       │       ├── 12h45.md (2.3 Ko)
│   │   │       │       └── 15h45.md (2.1 Ko)
│   │   │       └── 05/
│   │   │           └── 06/
│   │   │               └── 1h52.md (3.6 Ko)
│   │   ├── sqlalchemy/
│   │   │   ├── postgre_connection_with_sqlalchemy.md (5.5 Ko)
│   │   │   └── seed_postgre.md (4.9 Ko)
│   │   └── test/
│   │       └── conftest.md (2.5 Ko)
│   ├── project_idea/
│   │   ├── 01_general_structure.md (6.4 Ko)
│   │   └── 02_specific_cases_guideline.md (6.0 Ko)
│   ├── .gitkeep (0 o)
│   ├── DataEngineering_Plan_FitnessAI.md (3.8 Ko)
│   └── postgre_activate.md (1.6 Ko)
├── checkpoints/
│   └── mixtral-finetuned/
│       ├── checkpoint-603/
│       │   ├── adapter_config.json (867 o)
│       │   ├── adapter_model.safetensors (26657.3 Ko)
│       │   ├── config.json (1.3 Ko)
│       │   ├── optimizer.pt (53457.7 Ko)
│       │   ├── README.md (5.0 Ko)
│       │   ├── rng_state.pth (13.9 Ko)
│       │   ├── scheduler.pt (1.0 Ko)
│       │   ├── special_tokens_map.json (437 o)
│       │   ├── tokenizer.json (3423.4 Ko)
│       │   ├── tokenizer.model (481.9 Ko)
│       │   ├── tokenizer_config.json (1.5 Ko)
│       │   ├── trainer_state.json (34.9 Ko)
│       │   └── training_args.bin (6.9 Ko)
│       ├── adapter_config.json (867 o)
│       ├── adapter_model.safetensors (26657.3 Ko)
│       ├── config.json (1.3 Ko)
│       ├── README.md (3.3 Ko)
│       ├── special_tokens_map.json (437 o)
│       ├── tokenizer.json (3423.4 Ko)
│       ├── tokenizer.model (481.9 Ko)
│       └── tokenizer_config.json (1.5 Ko)
├── data_train/
│   ├── __init__.py (0 o)
│   ├── clean.py (840 o)
│   ├── fine_tune_dataset.jsonl (698.4 Ko)
│   └── fine_tune_dataset_clean.jsonl (760.4 Ko)
├── docker/
│   ├── Dockerfile.backend (0 o)
│   └── Dockerfile.frontend (0 o)
├── env_folder/
│   ├── .env.cognito (110 o)
│   ├── .env.cognito.example (81 o)
│   ├── .env.postgre.docker (228 o)
│   ├── .env.postgre.example (161 o)
│   ├── .env.postgre.local (231 o)
│   ├── .env.rds (180 o)
│   ├── .env.s3 (159 o)
│   ├── .env.s3.example (137 o)
│   └── __init__.py (0 o)
├── fake_bnb/
│   └── bitsandbytes/
│       ├── __init__.py (0 o)
│       ├── nn.py (0 o)
│       └── optim.py (0 o)
├── front_end/
│   ├── react_app/
│   │   ├── public/
│   │   │   ├── favicon.ico (3.8 Ko)
│   │   │   ├── index.html (1.7 Ko)
│   │   │   ├── logo192.png (5.2 Ko)
│   │   │   ├── logo512.png (9.4 Ko)
│   │   │   ├── manifest.json (492 o)
│   │   │   └── robots.txt (67 o)
│   │   ├── react_app_vite/
│   │   │   ├── dist/
│   │   │   │   ├── assets/
│   │   │   │   │   ├── index-BGSvPzvV.js (494.6 Ko)
│   │   │   │   │   └── index-DiNfpFWO.css (31.7 Ko)
│   │   │   │   └── index.html (393 o)
│   │   │   ├── public/
│   │   │   ├── src/
│   │   │   │   ├── components/
│   │   │   │   │   ├── ActivitySection.tsx (4.3 Ko)
│   │   │   │   │   ├── ChatSection.tsx (2.4 Ko)
│   │   │   │   │   └── MealSection.tsx (7.4 Ko)
│   │   │   │   ├── pages/
│   │   │   │   │   ├── AllUsers.tsx (2.0 Ko)
│   │   │   │   │   ├── CreateProfile.tsx (5.0 Ko)
│   │   │   │   │   ├── DailyLog.tsx (5.2 Ko)
│   │   │   │   │   └── SearchProducts.tsx (1.7 Ko)
│   │   │   │   ├── types/
│   │   │   │   │   └── log.ts (498 o)
│   │   │   │   ├── App.tsx (2.5 Ko)
│   │   │   │   ├── index.css (113 o)
│   │   │   │   └── main.tsx (640 o)
│   │   │   ├── .env (60 o)
│   │   │   ├── index.html (295 o)
│   │   │   ├── package-lock.json (119.2 Ko)
│   │   │   ├── package.json (767 o)
│   │   │   ├── postcss.config.cjs (82 o)
│   │   │   ├── tailwind.config.js (184 o)
│   │   │   ├── tsconfig.json (592 o)
│   │   │   ├── tsconfig.tsbuildinfo (310 o)
│   │   │   ├── vercel.json (69 o)
│   │   │   └── vite.config.ts (149 o)
│   │   ├── src/
│   │   │   ├── App.css (1.7 Ko)
│   │   │   ├── App.test.tsx (273 o)
│   │   │   ├── App.tsx (1.4 Ko)
│   │   │   ├── index.css (366 o)
│   │   │   ├── index.tsx (670 o)
│   │   │   ├── logo.svg (2.6 Ko)
│   │   │   ├── react-app-env.d.ts (40 o)
│   │   │   ├── react-oidc-context.d.ts (868 o)
│   │   │   ├── reportWebVitals.ts (425 o)
│   │   │   └── setupTests.ts (241 o)
│   │   ├── .gitignore (310 o)
│   │   ├── package-lock.json (654.2 Ko)
│   │   ├── package.json (1.2 Ko)
│   │   └── README.md (2.1 Ko)
│   ├── package-lock.json (1.8 Ko)
│   └── package.json (95 o)
├── infrastructure/
│   ├── aws/
│   │   ├── s3/
│   │   │   ├── s3_exports/
│   │   │   │   ├── .gitkeep (0 o)
│   │   │   │   └── __init__.py (0 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── config.py (916 o)
│   │   │   ├── s3_manager.py (3.8 Ko)
│   │   │   └── utils.py (32 o)
│   │   └── __init__.py (0 o)
│   └── __init__.py (0 o)
├── notebooks/
│   ├── .gitkeep (0 o)
│   ├── April_21_DL_fitness_coach.ipynb (125.5 Ko)
│   └── DL_fitness_coach.ipynb (128.3 Ko)
├── tests/
│   ├── back_end/
│   │   ├── data_pipeline/
│   │   │   ├── .gitkeep (0 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── test_etl.py (0 o)
│   │   │   └── test_utils.py (0 o)
│   │   ├── database/
│   │   │   ├── .pytest_cache/
│   │   │   │   ├── v/
│   │   │   │   │   └── cache/
│   │   │   │   │       ├── lastfailed (2 o)
│   │   │   │   │       ├── nodeids (364 o)
│   │   │   │   │       └── stepwise (2 o)
│   │   │   │   ├── .gitignore (37 o)
│   │   │   │   ├── CACHEDIR.TAG (191 o)
│   │   │   │   └── README.md (302 o)
│   │   │   ├── repository/
│   │   │   │   ├── .pytest_cache/
│   │   │   │   │   ├── v/
│   │   │   │   │   │   └── cache/
│   │   │   │   │   │       ├── lastfailed (2 o)
│   │   │   │   │   │       ├── nodeids (55 o)
│   │   │   │   │   │       └── stepwise (2 o)
│   │   │   │   │   ├── .gitignore (37 o)
│   │   │   │   │   ├── CACHEDIR.TAG (191 o)
│   │   │   │   │   └── README.md (302 o)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   ├── fitness_ai.duckdb (3340.0 Ko)
│   │   │   │   └── test_user.py (0 o)
│   │   │   ├── .gitkeep (0 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── test_connect.py (2.9 Ko)
│   │   │   └── test_seed_postgres.py (3.3 Ko)
│   │   ├── models/
│   │   │   ├── .gitkeep (0 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── test_nlp.py (0 o)
│   │   │   ├── test_regression.py (0 o)
│   │   │   └── test_vision.py (0 o)
│   │   ├── services/
│   │   │   ├── .gitkeep (0 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── run_model.py (630 o)
│   │   │   └── test_api.py (0 o)
│   │   ├── .gitkeep (0 o)
│   │   └── __init__.py (0 o)
│   ├── front_end/
│   │   ├── streamlit_app/
│   │   │   ├── .gitkeep (0 o)
│   │   │   ├── __init__.py (0 o)
│   │   │   └── test_dashboard.py (0 o)
│   │   ├── .gitkeep (0 o)
│   │   └── __init__.py (0 o)
│   ├── Infrastructures/
│   │   ├── aws/
│   │   │   ├── s3/
│   │   │   │   ├── .pytest_cache/
│   │   │   │   │   ├── v/
│   │   │   │   │   │   └── cache/
│   │   │   │   │   │       ├── nodeids (286 o)
│   │   │   │   │   │       └── stepwise (2 o)
│   │   │   │   │   ├── .gitignore (37 o)
│   │   │   │   │   ├── CACHEDIR.TAG (191 o)
│   │   │   │   │   └── README.md (302 o)
│   │   │   │   ├── __init__.py (0 o)
│   │   │   │   └── test_s3_manager.py (4.9 Ko)
│   │   │   └── __init__.py (0 o)
│   │   └── __init__.py (0 o)
│   ├── .gitkeep (0 o)
│   ├── __init__.py (0 o)
│   ├── conftest.py (1.1 Ko)
│   └── test_main.py (0 o)
├── user_exports/
│   └── .gitkeep (0 o)
├── .gitignore (1.6 Ko)
├── __init__.py (0 o)
├── docker-compose.yml (941 o)
├── Makefile (430 o)
├── README.md (4.5 Ko)
├── requirements.txt (1.1 Ko)
├── test_env.py (315 o)
└── upload hugging face (310 o)
