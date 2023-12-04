from fastapi import APIRouter

from . import apis

api_router = APIRouter()
api_router.include_router(apis.router, tags=["v1"], prefix="/v1")
