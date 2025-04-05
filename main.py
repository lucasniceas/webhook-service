from fastapi import FastAPI, HTTPException, Request
from pydantic import ValidationError
from schemas import WebhookPayload

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    try:
        raw_data = await request.json()

        # Transformar camelCase para snake_case
        payload_dict = {
            "docker_image": raw_data.get("dockerImage"),
            "strategy": raw_data.get("strategyName"),
            "command": raw_data.get("command"),
            "args": raw_data.get("arguments"),
            "volumes": [f"{v['name']}:{v['mountPath']}" for v in raw_data.get("volumes", [])],
            "node_selector": dict(
                kv.strip().split("=") for kv in raw_data.get("nodeSelector", "").split(",") if "=" in kv
            ) if raw_data.get("nodeSelector") else {},
            "runtime_config": {v['key']: v['value'] for v in raw_data.get("envVars", [])},
        }

        payload = WebhookPayload(**payload_dict)

        return {
            "message": "Webhook received successfully",
            "data": payload.dict()
        }

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))