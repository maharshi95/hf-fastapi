import requests
from pydantic import BaseModel


class HeartbeatResult(BaseModel):
    is_alive: bool


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
        self.heartbeat_endpoint = f"{self.base_url}/heartbeat"
        self.generate_endpoint = f"{self.base_url}/generate"

    def get_heartbeat(self) -> HeartbeatResult:
        resp = requests.get(self.heartbeat_endpoint).json()
        return HeartbeatResult(**resp)

    def generate(self, prompt: str, max_new_tokens: int = 20) -> GenerationResult:
        payload = {"prompt": prompt, "max_new_tokens": max_new_tokens}
        resp = requests.post(self.generate_endpoint, json=payload).json()
        return GenerationResult(**resp)
