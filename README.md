# Webhook Service

A lightweight, FastAPI-powered webhook microservice designed to receive deployment configurations from the frontend and trigger automated strategy deployments in a Kubernetes environment using Argo Workflows.

## 📦 Tech Stack

- **Python 3.9+**
- **FastAPI** – for building the API endpoints
- **Pydantic** – for payload validation
- **Uvicorn** – for running the ASGI server
- **Argo Events** (planned integration) – for Kubernetes-based orchestration

## 🚀 Features

- Accepts POST requests with payloads describing trading strategy deployments
- Validates incoming data using `Pydantic`
- Designed to connect seamlessly with frontend deploy panel
- Ready for Argo Sensor triggers via `webhook-sensor.yaml`
- Environment configuration and secrets via `.env` (excluded from version control)

## 📁 Folder Structure
webhook-service/
├── main.py             # FastAPI application entry point
├── schemas.py          # Pydantic model for request validation
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (ignored)
├── webhook-sensor.yaml # Argo Events sensor definition (K8s)
└── venv/               # Virtual environment (ignored)
## ⚙️ Running Locally

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
uvicorn main:app --reload --host 0.0.0.0 --port 8000

3. Start the service
uvicorn main:app --reload --host 0.0.0.0 --port 8000

4. Test webhook (optional)
curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "docker_image": "ghcr.io/myorg/strategy:latest",
    "strategy": "mean-reversion",
    "command": "python main.py"
  }'

🛠️ What’s Next
	•	Remove hardcoded fields like docker_image
	•	Add support for passing CPU & memory limits
	•	Include broker credential fields dynamically
	•	Forward payload to Argo Events for deployment trigger

🧠 Author

Developed by @lucasniceas for a client in London as part of a modular and scalable trading automation platform.
