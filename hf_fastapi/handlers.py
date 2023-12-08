from typing import Callable

from fastapi import FastAPI
from loguru import logger
import torch

from . import models


def _startup_model(app: FastAPI, pipeline_config: dict) -> models.HFModel:
    """
    Initializes and sets up the model for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
        pipeline_config (dict): Configuration for the huggingface pipeline.

    Returns:
        torch.device: The device on which the model is initialized.
    """
    app.state.model = models.HFModel(pipeline_config)
    return app.state.model


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None
    torch.cuda.empty_cache()


def start_app_handler(app: FastAPI, pipeline_config: dict) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        hf_model = _startup_model(app, pipeline_config)
        logger.info(f"Model name: {hf_model.model_name}")
        logger.info(f"Model loaded on device: {hf_model.device}")
        logger.info(f"Model dtype: {hf_model.torch_dtype}")

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
