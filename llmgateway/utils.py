import json
import os


def get_model_list() -> dict:
    # Get the absolute path of the current file (module)
    package_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to models_list.json within the package
    filename = os.path.join(package_dir, "models_list.json")

    # Read and return JSON data
    with open(filename, "r") as f:
        return json.load(f)
