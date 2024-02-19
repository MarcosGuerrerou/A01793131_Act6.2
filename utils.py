"""Utility functions for the project."""
import json


def load_json_data(file_path: str) -> dict:
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
