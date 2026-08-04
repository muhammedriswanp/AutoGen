import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

MODEL_NAME = "openai/gpt-oss-120b"

llm_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    include_name_in_message=False,
    model_info={
        "vision":False,
        "function_calling":True,
        "json_output":True,
        "structured_output": True,
        "family": ModelFamily.UNKNOWN,
    }
)