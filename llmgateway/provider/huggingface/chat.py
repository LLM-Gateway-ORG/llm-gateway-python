from ..base import BaseLLM


class HuggingfaceChat(BaseLLM):
    def __init__(self):
        super().__init__()

    def completion(self, model_name: str, messages: list) -> dict:
        raise Exception("Not Implemented")
