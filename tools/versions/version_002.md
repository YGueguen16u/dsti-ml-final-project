# 📁 Project Structure — Version 2
_Generated on 2025-04-27 23:34:12_

├── .github/
│   └── workflows/
│       └── deploy.yml
├── .idea/
│   ├── inspectionProfiles/
│   │   ├── profiles_settings.xml
│   │   └── Project_Default.xml
│   ├── .gitignore
│   ├── .name
│   ├── DSTI-ML-FINAL-PROJECT.iml
│   ├── misc.xml
│   ├── modules.xml
│   ├── vcs.xml
│   └── workspace.xml
├── .pytest_cache/
│   ├── v/
│   │   └── cache/
│   │       ├── nodeids
│   │       └── stepwise
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   └── README.md
├── back_end/
│   ├── api/
│   │   ├── dependencies/
│   │   │   ├── __init__.py
│   │   │   └── auth.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   └── __init__.py
│   ├── data_pipeline/
│   │   ├── dags/
│   │   │   └── __init__.py
│   │   ├── scripts/
│   │   │   ├── data/
│   │   │   │   ├── processed/
│   │   │   │   │   ├── nlp_analysis/
│   │   │   │   │   │   ├── length_Breakfast_Suggestion.png
│   │   │   │   │   │   ├── length_Dinner_Suggestion.png
│   │   │   │   │   │   ├── length_Lunch_Suggestion.png
│   │   │   │   │   │   ├── length_Snack_Suggestion.png
│   │   │   │   │   │   ├── similarity_Breakfast_Suggestion.png
│   │   │   │   │   │   ├── similarity_Dinner_Suggestion.png
│   │   │   │   │   │   ├── similarity_Lunch_Suggestion.png
│   │   │   │   │   │   └── similarity_Snack_Suggestion.png
│   │   │   │   │   ├── visuals/
│   │   │   │   │   │   ├── Activity Level_count.png
│   │   │   │   │   │   ├── Age_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Age_by_Gender.png
│   │   │   │   │   │   ├── Age_hist.png
│   │   │   │   │   │   ├── Carbohydrates_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Carbohydrates_by_Gender.png
│   │   │   │   │   │   ├── Carbohydrates_hist.png
│   │   │   │   │   │   ├── correlation_pearson.png
│   │   │   │   │   │   ├── correlation_spearman.png
│   │   │   │   │   │   ├── Daily Calorie Target_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Daily Calorie Target_by_Gender.png
│   │   │   │   │   │   ├── Daily Calorie Target_hist.png
│   │   │   │   │   │   ├── Dietary Preference_count.png
│   │   │   │   │   │   ├── Fat_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Fat_by_Gender.png
│   │   │   │   │   │   ├── Fat_hist.png
│   │   │   │   │   │   ├── Fitness Goal_count.png
│   │   │   │   │   │   ├── Gender_count.png
│   │   │   │   │   │   ├── Height_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Height_by_Gender.png
│   │   │   │   │   │   ├── Height_hist.png
│   │   │   │   │   │   ├── Protein_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Protein_by_Gender.png
│   │   │   │   │   │   ├── Protein_hist.png
│   │   │   │   │   │   ├── Weight_by_Fitness_Goal.png
│   │   │   │   │   │   ├── Weight_by_Gender.png
│   │   │   │   │   │   └── Weight_hist.png
│   │   │   │   │   ├── cleaned_stats.csv
│   │   │   │   │   └── nutrition_cleaned.csv
│   │   │   │   └── raw/
│   │   │   │       └── nutrition_raw.csv
│   │   │   ├── __init__.py
│   │   │   ├── analyze_cleaned_data.py
│   │   │   ├── clean_nutrition_data.py
│   │   │   └── load_nutrition_dataset.py
│   │   ├── utils/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── database/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── activity_log.py
│   │   │   ├── base.py
│   │   │   ├── meal_log.py
│   │   │   ├── shared_catalog.py
│   │   │   └── user_config.py
│   │   ├── queries/
│   │   │   └── __init__.py
│   │   ├── repository/
│   │   │   ├── __init__.py
│   │   │   └── user_repository.py
│   │   ├── __init__.py
│   │   ├── connect.py
│   │   ├── models.py
│   │   ├── reset.sql.py
│   │   └── seed_postgres.py
│   ├── models/
│   │   ├── model_utils/
│   │   │   └── __init__.py
│   │   ├── nlp/
│   │   │   ├── __init__.py
│   │   │   ├── model_training.py
│   │   │   ├── s3_nlp_controller.py
│   │   │   └── s3_nlp_manager.py
│   │   ├── regression/
│   │   │   └── __init__.py
│   │   ├── vision/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── __init__.py
│   └── main.py
├── best-practices/
│   ├── git/
│   │   ├── git-commands-basics.md
│   │   └── gitkeep.md
│   ├── personnal/
│   │   ├── 00_log/
│   │   │   └── 00_log_2025/
│   │   │       └── 04/
│   │   │           └── 10/
│   │   │               ├── 12h10.md
│   │   │               ├── 12h45.md
│   │   │               └── 15h45.md
│   │   ├── sqlalchemy/
│   │   │   ├── postgre_connection_with_sqlalchemy.md
│   │   │   └── seed_postgre.md
│   │   └── test/
│   │       └── conftest.md
│   ├── project_idea/
│   │   ├── 01_general_structure.md
│   │   └── 02_specific_cases_guideline.md
│   ├── .gitkeep
│   ├── DataEngineering_Plan_FitnessAI.md
│   └── postgre_activate.md
├── data/
│   ├── audio/
│   │   └── .gitkeep
│   ├── images/
│   │   └── .gitkeep
│   ├── logs/
│   │   └── .gitkeep
│   ├── nlp/
│   │   └── fine_tune_dataset.jsonl
│   ├── processed/
│   │   └── .gitkeep
│   └── raw/
│       └── .gitkeep
├── docker/
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
├── env_folder/
│   ├── .env.cognito
│   ├── .env.cognito.example
│   ├── .env.postgre
│   ├── .env.postgre.example
│   ├── .env.s3
│   ├── .env.s3.example
│   └── __init__.py
├── front_end/
│   ├── react_app/
│   │   ├── public/
│   │   │   ├── favicon.ico
│   │   │   ├── index.html
│   │   │   ├── logo192.png
│   │   │   ├── logo512.png
│   │   │   ├── manifest.json
│   │   │   └── robots.txt
│   │   ├── react_app_vite/
│   │   │   ├── public/
│   │   │   ├── src/
│   │   │   │   ├── pages/
│   │   │   │   │   └── CreateProfile.tsx
│   │   │   │   ├── App.tsx
│   │   │   │   ├── index.css
│   │   │   │   └── main.tsx
│   │   │   ├── index.html
│   │   │   ├── package-lock.json
│   │   │   ├── package.json
│   │   │   ├── postcss.config.cjs
│   │   │   ├── tailwind.config.js
│   │   │   └── vite.config.ts
│   │   ├── src/
│   │   │   ├── App.css
│   │   │   ├── App.test.tsx
│   │   │   ├── App.tsx
│   │   │   ├── index.css
│   │   │   ├── index.tsx
│   │   │   ├── logo.svg
│   │   │   ├── react-app-env.d.ts
│   │   │   ├── react-oidc-context.d.ts
│   │   │   ├── reportWebVitals.ts
│   │   │   └── setupTests.ts
│   │   ├── .gitignore
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   ├── README.md
│   │   └── tsconfig.json
│   ├── package-lock.json
│   └── package.json
├── Infrastructure/
│   ├── aws/
│   │   ├── s3/
│   │   │   ├── s3_exports/
│   │   │   │   ├── .gitkeep
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── s3_manager.py
│   │   │   └── utils.py
│   │   └── __init__.py
│   └── __init__.py
├── notebooks/
│   └── .gitkeep
├── tests/
│   ├── back_end/
│   │   ├── data_pipeline/
│   │   │   ├── .gitkeep
│   │   │   ├── __init__.py
│   │   │   ├── test_etl.py
│   │   │   └── test_utils.py
│   │   ├── database/
│   │   │   ├── .pytest_cache/
│   │   │   │   ├── v/
│   │   │   │   │   └── cache/
│   │   │   │   │       ├── lastfailed
│   │   │   │   │       ├── nodeids
│   │   │   │   │       └── stepwise
│   │   │   │   ├── .gitignore
│   │   │   │   ├── CACHEDIR.TAG
│   │   │   │   └── README.md
│   │   │   ├── repository/
│   │   │   │   ├── .pytest_cache/
│   │   │   │   │   ├── v/
│   │   │   │   │   │   └── cache/
│   │   │   │   │   │       ├── lastfailed
│   │   │   │   │   │       ├── nodeids
│   │   │   │   │   │       └── stepwise
│   │   │   │   │   ├── .gitignore
│   │   │   │   │   ├── CACHEDIR.TAG
│   │   │   │   │   └── README.md
│   │   │   │   ├── __init__.py
│   │   │   │   ├── fitness_ai.duckdb
│   │   │   │   └── test_user.py
│   │   │   ├── .gitkeep
│   │   │   ├── __init__.py
│   │   │   ├── test_connect.py
│   │   │   └── test_seed_postgres.py
│   │   ├── models/
│   │   │   ├── .gitkeep
│   │   │   ├── __init__.py
│   │   │   ├── test_nlp.py
│   │   │   ├── test_regression.py
│   │   │   └── test_vision.py
│   │   ├── services/
│   │   │   ├── .gitkeep
│   │   │   ├── __init__.py
│   │   │   └── test_api.py
│   │   ├── .gitkeep
│   │   └── __init__.py
│   ├── front_end/
│   │   ├── streamlit_app/
│   │   │   ├── .gitkeep
│   │   │   ├── __init__.py
│   │   │   └── test_dashboard.py
│   │   ├── .gitkeep
│   │   └── __init__.py
│   ├── Infrastructures/
│   │   ├── aws/
│   │   │   ├── s3/
│   │   │   │   ├── .pytest_cache/
│   │   │   │   │   ├── v/
│   │   │   │   │   │   └── cache/
│   │   │   │   │   │       ├── nodeids
│   │   │   │   │   │       └── stepwise
│   │   │   │   │   ├── .gitignore
│   │   │   │   │   ├── CACHEDIR.TAG
│   │   │   │   │   └── README.md
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_s3_manager.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── .gitkeep
│   ├── __init__.py
│   ├── conftest.py
│   └── test_main.py
├── user_exports/
│   └── .gitkeep
├── .gitignore
├── docker-compose.yml
├── Makefile
├── README.md
├── requirements.txt
└── test_env.py
