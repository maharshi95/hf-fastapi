from transformers import pipeline


class HFModel:
    def __init__(self, pipeline_config: dict) -> None:
        self.model_name = pipeline_config["model_name"]
        self.pipe = pipeline(**pipeline_config)

    @property
    def device(self):
        return self.pipe.device

    def generate(self, prompt: str, **kwargs) -> str:
        output = self.pipe(prompt, **kwargs)
        return output[0]["generated_text"]
