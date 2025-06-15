import json
from pathlib import Path


def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def get_file_extension(file_path):
    return Path(file_path).suffix.lower()
