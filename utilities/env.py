from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

env_path = Path('..') / '.env'

load_dotenv(dotenv_path=env_path)

import os

class Env:
    @staticmethod
    def get(var: str):
        return os.environ.get(var)
