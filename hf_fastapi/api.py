from fastapi import APIRouter, Request
from pydantic import BaseModel

from .models import HFModel

router = APIRouter()


class HeartbeatResult(BaseModel):
    is_alive: bool


class GenerationPayload(BaseModel):
    prompt: str
    max_new_tokens: int = 20
    return_full_text: bool = False


class GenerationResult(BaseModel):
    input_text: str
    generated_text: str
    model_name: str


@router.get("/heartbeat", response_model=HeartbeatResult, name="heartbeat")
def get_heartbeat() -> HeartbeatResult:
    heartbeat = HeartbeatResult(is_alive=True)
    return heartbeat


@router.post("/generate", response_model=GenerationResult, name="generate")
def generate(request: Request, payload: GenerationPayload) -> GenerationResult:
    model: HFModel = request.app.state.model
    generated_text = model.generate(**payload.model_dump())
    return GenerationResult(
        input_text=payload.prompt,
        generated_text=generated_text,
        model_name=model.model_name,
    )
