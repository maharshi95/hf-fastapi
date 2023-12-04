import torch

default_configs = {
    "device_map": "auto",
    "torch_dtype": torch.float16,
    "max_new_tokens": 20,
    "model_kwargs": {},
}

PIPELINE_CONFIGS = {
    "llama2-chat-7b": {
        **default_configs,
        "model": "meta-llama/Llama-2-7b-chat-hf",
    },
    "llama2-chat-13b": {
        **default_configs,
        "model": "meta-llama/Llama-2-13b-chat-hf",
    },
    "llama2-chat-70b": {
        **default_configs,
        "model": "meta-llama/Llama-2-70b-chat-hf",
    },
    "opt-iml-max-30b": {
        **default_configs,
        "model": "facebook/opt-iml-max-30b",
        "torch_dtype": "auto",
        "model_kwargs": {"load_in_8bit": True},
    },
    "t5-xxl": {
        **default_configs,
        "model": "google/t5-v1_1-xxl",
        "torch_dtype": torch.bfloat16,
    },
    "T0pp-11b": {
        **default_configs,
        "model": "bigscience/T0pp",
        "torch_dtype": torch.bfloat16,
    },
    "T0p-11b": {
        **default_configs,
        "model": "bigscience/T0p",
        "torch_dtype": torch.bfloat16,
    },
    "T0-11b": {
        **default_configs,
        "model": "bigscience/T0",
        "torch_dtype": torch.bfloat16,
    },
    "mistral-7b": {
        **default_configs,
        "model": "mistralai/Mistral-7B-v0.1",
        "torch_dtype": torch.float16,
    },
    "mistral-7b-inst": {
        **default_configs,
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "torch_dtype": torch.float32,
    },
    "mistral-7b-open-orca": {
        **default_configs,
        "model": "Open-Orca/Mistral-7B-OpenOrca",
        "torch_dtype": torch.float32,
    },
    "zephyr-7b-beta": {
        **default_configs,
        "model": "HuggingFaceH4/zephyr-7b-beta",
        "torch_dtype": torch.float32,
    },
}
