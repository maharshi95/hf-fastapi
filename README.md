# hf-fastapi

This repo provides the FAST API server code for hosting huggingface models on local machine or on a cluster.

## Installation

```bash
git clone https://github.com/maharshi95/hf-fastapi.git
cd hf-fastapi
bash setup_env.sh
```

## Usage

##### Running the server from the host machine

```bash
conda activate hf-fastapi
python -m hf_fastapi.serve --model-name {MODEL_NAME} --port {PORT}
```

##### Submitting a SLURM job to run the server on a cluster

```bash
conda activate hf-fastapi
slaunch --exp-name="hf-serve" --config="slurm_configs/med_gpu_nexus.json" \
    hf_fastapi/serve.py -m "mistral-7b-inst" -p 8000
```
You can add a custom SLURM config file to the `slurm_configs` directory and use it to submit the job.
An example of a SLURM config file is given below:

```json
{
    "slurm_account": "$SLURM_ACCOUNT",
    "slurm_partition": "$SLURM_PARTITION",
    "slurm_qos": "default",
    "slurm_gres": "gpu:rtxa5000:1",
    "slurm_time": "10:00:00",
    "slurm_mem": "30G",
    "slurm_ntasks_per_node": 1,
    "slurm_cpus_per_task": 4
}
```

## Client API
[client/example.py](client/example.py) contains an example of how to use the API.

```python
from hf_client.client import HFClient
client = HFClient(host=HOST, port=PORT)

# Health check
resp = client.get_heartbeat()
print("Is alive?", resp.is_alive)

# Generate API
prompt = "Question: What is the meaning of life, the universe, and everything? Answer:"
resp = client.generate(prompt=prompt, max_new_tokens=50)
print(f'Input: "{resp.input_text}"')
print("Model:", resp.model_name)
print(f'Output: "{resp.generated_text.strip()}"')
```
