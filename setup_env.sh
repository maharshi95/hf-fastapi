#!/bin/bash
# This script sets up the conda environment for the project.
# Example usage: ./setup_env.sh [env_name]

set -e

env_name="${1:-hf-serve}"

if ! command -v conda &>/dev/null; then
    echo "conda could not be found; install it here: https://www.anaconda.com/products/distribution"
    exit 1
fi

if ! { conda env list | grep "${env_name}"; } >/dev/null 2>&1; then
    conda create -y -n "${env_name}" python=3.10
fi

eval "$(conda shell.bash hook)"
conda activate "${env_name}"

# Install ipykernels and widgets
conda install -c conda-forge -y ipykernel ipywidgets --update-deps

# Torch installs
pip install torch torchvision torchaudio pytorch-lightning[extra]

# huggingface installs
pip install --no-cache transformers tokenizers accelerate datasets evaluate seqeval sentencepiece bitsandbytes xformers

# FastAPI installs
pip install loguru fastapi "uvicorn[standard]"

# Slurm installs
pip install submititnow

echo "Environment setup complete. Activate and use conda/pip list to inspect."
