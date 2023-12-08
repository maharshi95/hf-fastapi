from typing import Optional
from fastapi import APIRouter, Request
from pydantic import BaseModel

from .models import HFModel

router = APIRouter()


class HeartbeatResult(BaseModel):
    is_alive: bool


class GenerationResult(BaseModel):
    input_text: str
    generated_text: str
    model_name: str


class ModelInfoResult(BaseModel):
    is_ready: bool
    model: Optional[str] = None
    device: Optional[str] = None
    dtype: Optional[str] = None


class GenerationPayload(BaseModel):
    prompt: str
    max_new_tokens: int = 20


@router.get("/heartbeat", response_model=HeartbeatResult, name="heartbeat")
def get_heartbeat() -> HeartbeatResult:
    return HeartbeatResult(is_alive=True)


@router.get("/model", response_model=ModelInfoResult, name="model")
def get_model_info(request: Request) -> ModelInfoResult:
    model: HFModel = request.app.state.model
    if model is None:
        return ModelInfoResult(is_ready=False)
    return ModelInfoResult(
        is_ready=True,
        model=model.model_name,
        device=str(model.device),
        dtype=str(model.torch_dtype),
    )


@router.post("/generate", response_model=GenerationResult, name="generate")
def generate(request: Request, payload: GenerationPayload) -> GenerationResult:
    model: HFModel = request.app.state.model
    generated_text = model.generate(**payload.model_dump())
    return GenerationResult(
        input_text=payload.prompt,
        generated_text=generated_text,
        model_name=model.model_name,
    )
