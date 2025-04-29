from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# InferenceClient로 연결
client = InferenceClient(
    model="google/flan-t5-small",
    token=api_token
)

# 직접 prompt 보내기
response = client.text_generation(prompt="Tell me a funny joke about cats.", max_new_tokens=50)

print(response)
