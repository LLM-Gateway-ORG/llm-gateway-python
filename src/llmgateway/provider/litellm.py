from litellm import acompletion, completion

from .base import BaseLLM


class Litellm(BaseLLM):
    def __init__(self, api_key: str, **kwargs):
        if not api_key:
            raise ValueError("API Key Not Found !!")
        self.__api_key = api_key
        super().__init__(**kwargs)

    def completion(self, messages: list) -> dict:
        try:
            response = completion(
                model=self._model_name,
                messages=messages,
                api_key=self.__api_key,
                timeout=30,
            )
            return response
        except Exception as e:
            raise Exception(f"LiteLLM completion error: {str(e)}")

    async def async_completion(self, messages: list):
        try:
            response = await acompletion(
                model=self._model_name,
                messages=messages,
                api_key=self.__api_key,
                stream=True,
            )
            return response
        except Exception as e:
            raise Exception(f"LiteLLM async completion error: {str(e)}")
