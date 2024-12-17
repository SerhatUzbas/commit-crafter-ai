import os
from dotenv import load_dotenv


env_path = "/Users/serhatuzbas/Documents/GitHub/commit-crafter-ai/.env"


load_dotenv(dotenv_path=env_path, override=True)


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise ValueError("Environment variables OPENAI_API_KEY must be set")
