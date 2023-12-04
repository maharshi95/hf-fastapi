import argparse
from typing import Optional
from loguru import logger
import uvicorn

from . import app
from .model_factory import PIPELINE_CONFIGS, default_configs


def add_arguments(
    parser: Optional[argparse.ArgumentParser] = None,
) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model-name",
        "-m",
        type=str,
        default="gpt2-medium",
        help="The name of the model to use.",
    )
    parser.add_argument(
        "--port", "-p", type=int, default=8000, help="The port to run the server on."
    )

    return parser


def main(args: argparse.Namespace) -> None:
    if args.model_name in PIPELINE_CONFIGS:
        pipeline_config = PIPELINE_CONFIGS[args.model_name]
        logger.info(
            f"Found {args.model_name} in model factory. Using pipeline config: {pipeline_config}"
        )
    else:
        pipeline_config = {**default_configs, "model": args.model_name}
        logger.info(
            f"Did not find {args.model_name} in model factory. Using default pipeline config: {pipeline_config}"
        )
    fast_app = app.get_app(pipeline_config)
    uvicorn.run(fast_app, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    parser = add_arguments()
    args = parser.parse_args()
    main(args)
