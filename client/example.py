import argparse
from hf_client import HFClient

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, default="localhost")
args = parser.parse_args()

host = args.host
if not host.endswith("umiacs.umd.edu"):
    host = f"{host}.umiacs.umd.edu"

PORT = 8000

client = HFClient(host=host, port=PORT)

print("\n\nTesting health endpoint...")
resp = client.get_heartbeat()
print("Is alive?", resp.is_alive)

print("\n\nTesting generate endpoint...")
prompt = "Question: What is the meaning of life, the universe, and everything? Answer:"
resp = client.generate(
    prompt=prompt,
    max_new_tokens=50,
)
resp = client.generate(prompt=prompt, max_new_tokens=50)
print(f'Input: "{resp.input_text}"')
print("Model:", resp.model_name)
print(f'Output: "{resp.generated_text.strip()}"')
