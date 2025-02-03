import json
import os
from pathlib import Path

import requests


def read_json_file(filepath: str) -> dict:
    with open(filepath, "r") as f:
        return json.load(f)


def write_json_file(filepath: str, data: dict) -> None:
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    try:
        BASE_FILE_PATH = Path("src/llmgateway/provider/data/")
        # Fetching the model data
        url = "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"
        response = requests.get(url)
        response.raise_for_status()
        litellm_models_list = response.json()

        # Filtering models except 'sample_spec'
        litellm_models_dict = dict()
        for key, value in litellm_models_list.items():
            if key != "sample_spec":
                litellm_models_dict[key] = {
                    **value,
                    "provider": value["litellm_provider"],
                }

        # Check if `models_list.json` exists
        other_models_path = os.path.join(BASE_FILE_PATH, "other_models_list.json")
        other_models_dict = {}
        if os.path.exists(other_models_path):
            with open(other_models_path, "r") as f:
                other_models_dict = json.load(f)

        # Update the `litellm_models` and retain `other_models`
        updated_data = litellm_models_dict | other_models_dict

        # Writing the updated data back to the JSON file
        write_json_file(
            os.path.join(BASE_FILE_PATH, "litellm_models_list.json"),
            litellm_models_dict,
        )
        write_json_file(os.path.join(BASE_FILE_PATH, "models_list.json"), updated_data)

        print("models_list.json updated successfully.")

    except requests.RequestException as e:
        print(f"Error fetching models list: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
