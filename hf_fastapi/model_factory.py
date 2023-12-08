import torch

default_configs = {
    "device_map": "auto",
    "torch_dtype": "auto",
    "model_kwargs": {},
}

_llama_pipeline_configs = {
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
}

_mistral_pipeline_configs = {
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

_bigscience_pipeline_configs = {
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
}

_falcon_pipeline_configs = {
    "falcon-rw-1b": {
        **default_configs,
        "model": "tiiuae/falcon-rw-1b",
        "torch_dtype": torch.bfloat16,
        "trust_remote_code": True,
    },
    "falcon-7b": {
        **default_configs,
        "model": "tiiuae/falcon-7b",
        "torch_dtype": torch.bfloat16,
        "trust_remote_code": True,
    },
    "falcon-7b-inst": {
        **default_configs,
        "model": "tiiuae/falcon-7b-instruct",
        "torch_dtype": torch.bfloat16,
        "trust_remote_code": True,
    },
    "falcon-40b": {
        **default_configs,
        "model": "tiiuae/falcon-40b",
        "torch_dtype": torch.bfloat16,
        "trust_remote_code": True,
    },
}

PIPELINE_CONFIGS = {
    **_llama_pipeline_configs,
    **_mistral_pipeline_configs,
    **_bigscience_pipeline_configs,
    **_falcon_pipeline_configs,
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
}
