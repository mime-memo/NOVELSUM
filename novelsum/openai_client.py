from openai import OpenAI
import os

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise RuntimeError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)
