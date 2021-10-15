from typing import Dict, Optional
from dotenv import dotenv_values

def load_env() -> Dict[str, Optional[str]]:
  config = dotenv_values(".env")

  return config
