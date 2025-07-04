import json
from pathlib import Path
from typing import Dict


def load_novels(file_path: str = "novels.json") -> Dict[str, str]:
    try:
        with open(Path(__file__).parent.parent / file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
