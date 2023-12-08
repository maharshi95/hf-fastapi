from typing import Optional
import requests
from pydantic import BaseModel


class HeartbeatResult(BaseModel):
    is_alive: bool


class ModelInfoResult(BaseModel):
    is_ready: bool
    model: Optional[str] = None
    device: Optional[str] = None
    dtype: Optional[str] = None


class GenerationResult(BaseModel):
    input_text: str
    generated_text: str
    model_name: str


class HFClient:
    def __init__(self, host: str, port: int, version: str = "v1") -> None:
        self.host = host
        self.port = port
        self.version = version
        self.base_url = f"http://{host}:{port}/api/{version}"

        self.endpoints = {
            "heartbeat": f"{self.base_url}/heartbeat",
            "generate": f"{self.base_url}/generate",
            "model": f"{self.base_url}/model",
        }

    def get_heartbeat(self) -> HeartbeatResult:
        resp = requests.get(self.endpoints["heartbeat"]).json()
        return HeartbeatResult(**resp)

    def get_model_info(self) -> ModelInfoResult:
        resp = requests.get(self.endpoints["model"])
        resp.ok or resp.raise_for_status()
        return ModelInfoResult(**resp.json())

    def generate(self, prompt: str, max_new_tokens: int = 20) -> GenerationResult:
        payload = {"prompt": prompt, "max_new_tokens": max_new_tokens}
        resp = requests.post(self.endpoints["generate"], json=payload)
        resp.ok or resp.raise_for_status()
        return GenerationResult(**resp.json())
