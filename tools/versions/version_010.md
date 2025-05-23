# 📁 Project Structure — Version 10
_Generated on 2025-05-01 17:27:14_

├── .github/
│   └── workflows/
│       └── deploy.yml (9 o)
├── .idea/
│   ├── inspectionProfiles/
│   │   ├── profiles_settings.xml (174 o)
│   │   └── Project_Default.xml (503 o)
│   ├── .gitignore (176 o)
│   ├── .name (11 o)
│   ├── DSTI-ML-FINAL-PROJECT.iml (410 o)
│   ├── misc.xml (326 o)
│   ├── modules.xml (294 o)
│   ├── vcs.xml (167 o)
│   └── workspace.xml (15.3 Ko)
├── .pytest_cache/
│   ├── v/
│   │   └── cache/
│   │       ├── nodeids (2 o)
│   │       └── stepwise (2 o)
│   ├── .gitignore (37 o)
│   ├── CACHEDIR.TAG (191 o)
│   └── README.md (302 o)
├── back_end/
│   ├── api/
│   │   ├── dependencies/
│   │   │   ├── __init__.py (0 o)
│   │   │   └── auth.py (3.0 Ko)
│   │   ├── routes/
│   │   │   ├── __init__.py (0 o)
│   │   │   └── user.py (3.2 Ko)
│   │   └── __init__.py (0 o)
│   ├── config/
│   │   ├── __init__.py (0 o)
│   │   └── settings.py (1.3 Ko)
│   ├── data_pipeline/
│   │   ├── dags/
│   │   │   └── __init__.py (0 o)
│   │   ├── scripts/
│   │   │   ├── data/
│   │   │   │   ├── processed/
│   │   │   │   │   ├── nlp_analysis/
│   │   │   │   │   │   ├── length_Breakfast_Suggestion.png (27.9 Ko)
│   │   │   │   │   │   ├── length_Dinner_Suggestion.png (26.2 Ko)
│   │   │   │   │   │   ├── length_Lunch_Suggestion.png (25.8 Ko)
│   │   │   │   │   │   ├── length_Snack_Suggestion.png (28.2 Ko)
│   │   │   │   │   │   ├── similarity_Breakfast_Suggestion.png (41.5 Ko)
│   │   │   │   │   │   ├── similarity_Dinner_Suggestion.png (41.2 Ko)
│   │   │   │   │   │   ├── similarity_Lunch_Suggestion.png (41.3 Ko)
│   │   │   │   │   │   └── similarity_Snack_Suggestion.png (39.1 Ko)
│   │   │   │   │   ├── visuals/
│   │   │   │   │   │   ├── Activity Level_count.png (22.0 Ko)
│   │   │   │   │   │   ├── Age_by_Fitness_Goal.png (45.9 Ko)
│   │   │   │   │   │   ├── Age_by_Gender.png (33.2 Ko)
│   │   │   │   │   │   ├── Age_hist.png (20.6 Ko)
│   │   │   │   │   │   ├── Carbohydrates_by_Fitness_Goal.png (45.6 Ko)
│   │   │   │   │   │   ├── Carbohydrates_by_Gender.png (38.4 Ko)
│   │   │   │   │   │   ├── Carbohydrates_hist.png (21.3 Ko)
│   │   │   │   │   │   ├── correlation_pearson.png (58.7 Ko)
│   │   │   │   │   │   ├── correlation_spearman.png (58.7 Ko)
│   │   │   │   │   │   ├── Daily Calorie Target_by_Fitness_Goal.png (42.1 Ko)
│   │   │   │   │   │   ├── Daily Calorie Target_by_Gender.png (35.3 Ko)
│   │   │   │   │   │   ├── Daily Calorie Target_hist.png (22.2 Ko)
│   │   │   │   │   │   ├── Dietary Preference_count.png (16.9 Ko)
│   │   │   │   │   │   ├── Fat_by_Fitness_Goal.png (38.0 Ko)
│   │   │   │   │   │   ├── Fat_by_Gender.png (30.7 Ko)
│   │   │   │   │   │   ├── Fat_hist.png (18.5 Ko)
│   │   │   │   │   │   ├── Fitness Goal_count.png (19.5 Ko)
│   │   │   │   │   │   ├── Gender_count.png (13.0 Ko)
│   │   │   │   │   │   ├── Height_by_Fitness_Goal.png (41.9 Ko)
│   │   │   │   │   │   ├── Height_by_Gender.png (32.9 Ko)
│   │   │   │   │   │   ├── Height_hist.png (19.1 Ko)
│   │   │   │   │   │   ├── Protein_by_Fitness_Goal.png (42.6 Ko)
│   │   │   │   │   │   ├── Protein_by_Gender.png (36.7 Ko)
│   │   │   │   │   │   ├── Protein_hist.png (20.1 Ko)
│   │   │   │   │   │   ├── Weight_by_Fitness_Goal.png (42.2 Ko)
│   │   │   │   │   │   ├── Weight_by_Gender.png (32.2 Ko)
│   │   │   │   │   │   └── Weight_hist.png (20.5 Ko)
│   │   │   │   │   ├── cleaned_stats.csv (602 o)
│   │   │   │   │   └── nutrition_cleaned.csv (99.5 Ko)
│   │   │   │   └── raw/
│   │   │   │       └── nutrition_raw.csv (99.9 Ko)
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── analyze_cleaned_data.py (4.5 Ko)
│   │   │   ├── clean_nutrition_data.py (3.3 Ko)
│   │   │   └── load_nutrition_dataset.py (3.1 Ko)
│   │   ├── utils/
│   │   │   └── __init__.py (0 o)
│   │   └── __init__.py (0 o)
│   ├── database/
│   │   ├── models/
│   │   │   ├── __init__.py (243 o)
│   │   │   ├── activity_log.py (3.2 Ko)
│   │   │   ├── base.py (885 o)
│   │   │   ├── meal_log.py (1.6 Ko)
│   │   │   ├── shared_config.py (1.8 Ko)
│   │   │   └── user_config.py (1.9 Ko)
│   │   ├── queries/
│   │   │   └── __init__.py (0 o)
│   │   ├── repository/
│   │   │   ├── __init__.py (0 o)
│   │   │   └── user_repository.py (4.8 Ko)
│   │   ├── __init__.py (0 o)
│   │   ├── connect.py (1.9 Ko)
│   │   ├── initialize_db.py (1.6 Ko)
│   │   ├── models.py (3.9 Ko)
│   │   ├── reset.sql.py (729 o)
│   │   └── seed_postgres.py (2.0 Ko)
│   ├── models/
│   │   ├── model_utils/
│   │   │   └── __init__.py (0 o)
│   │   ├── nlp/
│   │   │   ├── __init__.py (0 o)
│   │   │   ├── model_training.py (532 o)
│   │   │   ├── s3_nlp_controller.py (2.0 Ko)
│   │   │   └── s3_nlp_manager.py (939 o)
│   │   ├── regression/
│   │   │   └── __init__.py (0 o)
│   │   ├── vision/
│   │   │   └── __init__.py (0 o)
│   │   └── __init__.py (0 o)
│   ├── services/
│   │   ├── __init__.py (0 o)
│   │   ├── product_searcher.py (1.5 Ko)
│   │   └── user_service.py (123 o)
│   ├── __init__.py (0 o)
│   ├── main.py (1.4 Ko)
│   └── show_tables.py (529 o)
├── best-practices/
│   ├── git/
│   │   ├── git-commands-basics.md (1.6 Ko)
│   │   └── gitkeep.md (1.1 Ko)
│   ├── personnal/
│   │   ├── 00_log/
│   │   │   └── 00_log_2025/
│   │   │       └── 04/
│   │   │           └── 10/
│   │   │               ├── 12h10.md (1.4 Ko)
│   │   │               ├── 12h45.md (2.3 Ko)
│   │   │               └── 15h45.md (2.1 Ko)
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
├── data/
│   ├── audio/
│   │   └── .gitkeep (0 o)
│   ├── images/
│   │   └── .gitkeep (0 o)
│   ├── logs/
│   │   └── .gitkeep (0 o)
│   ├── nlp/
│   │   └── fine_tune_dataset.jsonl (0 o)
│   ├── processed/
│   │   └── .gitkeep (0 o)
│   └── raw/
│       └── .gitkeep (0 o)
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
│   │   │   │   │   ├── index-C7IYe28I.js (313.1 Ko)
│   │   │   │   │   └── index-ChwZJ8QC.css (7.0 Ko)
│   │   │   │   └── index.html (393 o)
│   │   │   ├── public/
│   │   │   ├── src/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── AllUsers.tsx (1.9 Ko)
│   │   │   │   │   ├── CreateProfile.tsx (5.0 Ko)
│   │   │   │   │   └── SearchProducts.tsx (1.7 Ko)
│   │   │   │   ├── App.tsx (2.7 Ko)
│   │   │   │   ├── index.css (113 o)
│   │   │   │   └── main.tsx (640 o)
│   │   │   ├── .env (60 o)
│   │   │   ├── index.html (295 o)
│   │   │   ├── package-lock.json (113.6 Ko)
│   │   │   ├── package.json (660 o)
│   │   │   ├── postcss.config.cjs (82 o)
│   │   │   ├── tailwind.config.js (184 o)
│   │   │   ├── tsconfig.json (592 o)
│   │   │   ├── tsconfig.tsbuildinfo (153 o)
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
├── .gitignore (1.4 Ko)
├── __init__.py (0 o)
├── docker-compose.yml (290 o)
├── Makefile (430 o)
├── README.md (0 o)
├── requirements.txt (1.1 Ko)
└── test_env.py (315 o)
