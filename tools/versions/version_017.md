# 📁 Project Structure — Version 17
_Generated on 2025-05-16 22:49:32_

├── .github/
│   └── workflows/
│       └── deploy.yml (1.1 Ko)
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
│   │   │   ├── repository/
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
