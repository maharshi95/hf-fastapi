from transformers import pipeline, AutoTokenizer
from transformers.pipelines import Pipeline, TextGenerationPipeline


def get_custom_generate_kwargs(llm_pipeline: Pipeline):
    kwargs = {}
    if "mistral" in llm_pipeline.model.name_or_path:
        kwargs["pad_token_id"] = llm_pipeline.tokenizer.eos_token_id
    elif "pythia" in llm_pipeline.model.name_or_path:
        kwargs["pad_token_id"] = llm_pipeline.tokenizer.eos_token_id
    elif "falcon-" in llm_pipeline.model.name_or_path:
        kwargs["eos_token_id"] = llm_pipeline.tokenizer.eos_token_id
        kwargs["pad_token_id"] = llm_pipeline.tokenizer.eos_token_id
    if isinstance(llm_pipeline, TextGenerationPipeline):
        kwargs["return_full_text"] = False
    return kwargs


class HFModel:
    def __init__(self, pipeline_config: dict) -> None:
        self.model_name = pipeline_config["model"]
        tokenizer_name = pipeline_config.get("tokenizer", self.model_name)
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.pipe = pipeline(**pipeline_config, tokenizer=tokenizer)
        self.generate_kwargs = get_custom_generate_kwargs(self.pipe)

    @property
    def device(self):
        return self.pipe.device

    @property
    def torch_dtype(self):
        return self.pipe.model.dtype

    def generate(self, prompt: str, **kwargs) -> str:
        output = self.pipe(prompt, **self.generate_kwargs, **kwargs)
        return output[0]["generated_text"]
