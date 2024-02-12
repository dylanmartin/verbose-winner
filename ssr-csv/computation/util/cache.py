import json
import os

def save_cache(data, file_path):
    """Saves given data in JSON format to the specified file path.

    Args:
        data (dict): Data to be serialized and saved.
        file_path (str): Full path to the file where data should be saved.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)

def load_cache(file_path):
    """Loads data from a JSON file specified by the file path.

    Args:
        file_path (str): Full path to the file from which data should be loaded.

    Returns:
        dict: The data loaded from the JSON file.
    """
    if not os.path.exists(file_path):
        return {}  # Return an empty dict if file doesn't exist
    with open(file_path, 'r') as file:
        return json.load(file)
