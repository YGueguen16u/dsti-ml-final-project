# AI Food & Activity Tracker

A full-stack SaaS project for personalized food and physical activity tracking, featuring an integrated fine-tuned AI assistant, food search via AWS S3, and user-specific data storage in AWS RDS.

---

## Project Objective

A complete web application allowing each user to:

* Search food products from a cleaned OpenFoodFacts database (hosted on S3).
* Add structured meals (breakfast, lunch, dinner, snacks) and physical activities.
* Interact with an AI assistant (chat-style) that can auto-fill logs.
* View and store daily logs in a PostgreSQL database tied to their account.
* Receive structured suggestions and completions based on their habits.

---

## Project Architecture

### Backend (FastAPI)

* Folder: `back_end/`
* FastAPI RESTful service
* SQLAlchemy ORM with PostgreSQL (hosted on AWS RDS)
* Handles:

  * Authentication (basic placeholder for now, AWS Cognito planned for future versions)
  * CRUD for meals, foods, activities
  * S3 product search (OpenFoodFacts integration)
  * Daily user logs (`user_daily_logs` table)
  * Chatbot assistant endpoint (model inference)
* LLM: Mixtral-8x7B-Instruct fine-tuned with QLoRA and Axolotl

### Frontend (React + Vite)

* Folder: `front_end/react_app/`
* Pages and components:

  * **Daily Log**: Meal/Activity input and visualization
  * **Search Page**: Query food items from S3
  * **Chat Interface**: Conversational assistant
  * **User Profile**: Dietary goals and tracking setup
* Hosted on **Vercel**

### Infrastructure

* **AWS S3**:

  * Storage of cleaned and transformed OpenFoodFacts data (in JSON format)
* **AWS RDS (PostgreSQL)**:

  * Stores all user-related logs and metadata
* **Render**:

  * Hosting backend FastAPI server with attached Docker image
* **CI/CD (GitHub Actions)**:

  * Automated tests and deployment on push to `main`
* **Containerization**:

  * `Dockerfile` and `docker-compose.yml` for local deployment
  * Backend image includes fine-tuned model and inference script

---

## Environment Setup & Launch

### Local Launch

```bash
# 1. Clone the repo
$ git clone <repo-url>
$ cd DSTI-ML-FINAL-PROJECT

# 2. Setup environment
$ cp .env.example .env

# 3. Build and launch services
$ docker-compose up --build

# 4. Launch frontend separately
$ cd front_end/react_app
$ npm install
$ npm run dev
```

### Backend Environment Variables (`.env`)

```env
POSTGRES_HOST=your-db-host
POSTGRES_DB=your-db-name
POSTGRES_USER=your-user
POSTGRES_PASSWORD=your-password
S3_BUCKET_NAME=your-bucket
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
MODEL_DIR=./checkpoints/mixtral-finetuned
```

---

## AI Fine-Tuning

* **Base model**: `mistralai/Mixtral-8x7B-Instruct-v0.1`
* **Method**: LoRA 4-bit with QLoRA (via Axolotl)
* **Dataset**: JSONL with multi-turn conversations using format:

```json
{
  "messages": [
    {"role": "user", "content": "j'ai mangé 3 pommes et fait du vélo"},
    {"role": "assistant", "content": "{ \"assistant_output\": ..., \"commands\": [{...}] }"}
  ]
}
```

* Prompts follow `[INST] ... [/INST]` template for instruction-based learning
* Checkpoints stored in `checkpoints/mixtral-finetuned/`

---

## Project Structure

```
DSTI-ML-FINAL-PROJECT/
├── back_end/
│   ├── main.py
│   ├── models/             # SQLAlchemy schemas
│   ├── routes/             # API endpoints
│   ├── services/           # S3, chatbot, product searcher
│   └── tests/              # Unit tests (pytest)
│
├── front_end/react_app/   # React + Vite frontend
│   ├── src/
│   ├── pages/
│   ├── components/
│   └── ...
│
├── data_train/            # JSONL training data for fine-tune
├── checkpoints/           # LoRA checkpoints
├── docker-compose.yml
├── Dockerfile (backend)
├── .github/workflows/     # CI/CD configs
└── README.md
```

---

## Future Improvements

* Mobile-responsive interface or PWA
* Visual analytics (charts for calories, training time, etc.)
* Personalized nutrition and fitness recommendations
* Internationalization (multilingual support)
* LLM quantized inference via `ggml` or `vLLM` for faster responses

---

## Academic Context

This project was built as part of the **DSTI** academic program. It showcases the integration of modern technologies:

* LLM fine-tuning (Mixtral + QLoRA)
* Data scraping and transformation (OpenFoodFacts)
* Full-stack architecture (FastAPI + React)
* AWS-based cloud storage and database
* Docker + GitHub CI/CD DevOps
