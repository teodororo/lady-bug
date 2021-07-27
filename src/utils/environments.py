import os
from dotenv import load_dotenv
from pathlib import Path


def env(name):
    if os.environ.get("app_test"):
        path_env = Path('.') / '.env'
        load_dotenv(dotenv_path=path_env)
        return os.getenv(name)
    else:
        return os.environ.get(name)