from ..base import BaseLLM

# from krutrim_cloud import KrutrimCloud


class OlaKrutrimChat(BaseLLM):
    def __init__(self, api_key: str, **kwargs) -> None:
        self.client = None
        # self.client = KrutrimCloud(api_key=api_key)
        super().__init__(**kwargs)

    def completion(self, model_name: str, messages: list) -> dict:
        if not self.client:
            raise Exception("Client is not initialized. Please set the API key.")
        try:
            response = self.client.chat.completions.create(
                model=model_name, messages=messages
            )
            return response.model_dump()
        except Exception as e:
            raise Exception(f"Ola Krutrim completion error: {str(e)}")

    def async_completion(self, model_name: str, messages: list):
        if not self.client:
            raise Exception("Client is not initialized. Please set the API key.")
        try:
            response = self.client.chat.completions.create(
                model=model_name, messages=messages, stream=True
            )
            for chunk in response:
                yield chunk
        except Exception as e:
            raise Exception(f"Ola Krutrim async completion error: {str(e)}")
