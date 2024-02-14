from typing import Any, Optional
import os
import json

cache_path = "cache/cache.json"

def load_cache() -> Optional[Any]:
    """
    Load JSON data from a file if it exists.

    Returns:
        The loaded JSON data if the file exists, None otherwise.
    """
    if os.path.exists(cache_path):
        with open(cache_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_cache(data: Any) -> None:
    """
    Save JSON data to a file, creating directories if necessary.

    Args:
        data: The data to be saved in JSON format.
    """
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
