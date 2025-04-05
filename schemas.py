from pydantic import BaseModel, Field
from typing import Optional, Dict

class WebhookPayload(BaseModel):
    docker_image: str = Field(..., description="Docker image name to deploy")
    strategy: Optional[str] = Field(None, description="Strategy name to run")
    command: Optional[str] = Field(None, description="Command to execute")
    args: Optional[list[str]] = Field(None, description="Arguments for the container")
    volumes: Optional[list[str]] = Field(None, description="Volume mounts (e.g., /data:/mnt/data)")
    node_selector: Optional[Dict[str, str]] = Field(None, description="Node selectors for Kubernetes scheduling")
    runtime_config: Optional[Dict[str, str]] = Field(None, description="Extra runtime configuration like risk, period, etc.")