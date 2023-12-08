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
        "--torch-dtype",
        "-t",
        default=None,
        help="The torch dtype to use. If not specified, will use the default for the model.",
    )
    parser.add_argument(
        "--port", "-p", type=int, default=8000, help="The port to run the server on."
    )

    return parser


def find_port(base_port: int) -> int:
    """Find an open port."""
    import socket

    sock = socket.socket()
    for port in range(base_port, base_port + 100):
        try:
            sock.bind(("localhost", port))
        except OSError:
            pass
        else:
            sock.close()
            return port
    raise OSError("Could not find an open port")


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
    if args.torch_dtype:
        pipeline_config["torch_dtype"] = args.torch_dtype
    fast_app = app.get_app(pipeline_config)
    port = find_port(args.port)
    logger.info(f"Found open port: {port}")
    uvicorn.run(fast_app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    parser = add_arguments()
    args = parser.parse_args()
    main(args)
