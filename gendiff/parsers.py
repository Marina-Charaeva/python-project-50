import json
from pathlib import Path

import yaml


def parse_file(file_path):
    extension = get_file_extension(file_path)
    with open(file_path, 'r') as f:
        if extension == '.json':
            return json.load(f)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(f) or {}
        raise ValueError(f"Unsupported file format: {extension}")


def get_file_extension(file_path):
    return Path(file_path).suffix.lower()
