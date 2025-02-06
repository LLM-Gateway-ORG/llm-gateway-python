import json
import os


def get_model_list() -> dict:
    filename = os.path.join(os.getcwd(), "src/provider/data/models_list.json")
    with open(filename, "r") as f:
        return json.loads(f.read())
