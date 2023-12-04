from fastapi import APIRouter

from . import api

api_router = APIRouter()
api_router.include_router(api.router, tags=["v1"], prefix="/v1")
