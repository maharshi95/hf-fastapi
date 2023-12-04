from fastapi import FastAPI

from . import handlers
from .router import api_router

APP_VERSION = "0.1.0"
APP_NAME = "Huggingface FastAPI Server"
API_PREFIX = "/api"
IS_DEBUG = False


def get_app(pipeline_config: dict) -> FastAPI:
    """
    Returns a FastAPI application with the specified model name.

    Args:
    - model_name (str): The name of the huggingface (model) pipeline to use.

    Returns:
    - FastAPI: The FastAPI application.

    """
    app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    app.include_router(api_router, prefix=API_PREFIX)

    app.add_event_handler("startup", handlers.start_app_handler(app, pipeline_config))
    app.add_event_handler("shutdown", handlers.stop_app_handler(app))
    return app
