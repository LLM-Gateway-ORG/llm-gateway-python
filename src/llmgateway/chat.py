from typing import List, Optional

from helpers import get_model_list
from provider import BaseLLM, LLM_Factory


class Chat(object):
    mode = "chat"

    def __init__(
        self, model_name: str, sync: bool = True, api_key: Optional[str] = None
    ) -> None:
        self.sync = sync
        self.model_name = model_name
        self.__api_key = api_key

        self.__model_details = self.__fetch_model_details(model_name)

        # Load Model
        self.__llm = self.__load_model()

    @property
    def api_key(self) -> str:
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        self.__api_key = api_key

    def __load_model(self) -> BaseLLM:
        provider = self.__fetch_provider()
        return LLM_Factory(
            provider=provider,
            api_key=self.api_key,
            model_name=self.model_name,
        )

    def __fetch_model_details(self, model_name: str) -> dict:
        models_list = get_model_list()
        if model_name not in models_list and models_list[model_name] == self.mode:
            raise ValueError("Model Not Found !!")
        return models_list[model_name]

    def __fetch_provider(self) -> str:
        return self.__model_details.get("provider")

    def generate(self, messages: List[str]) -> None:
        return (
            self.__llm.completion(messages)
            if self.sync
            else self.__llm.async_completion(messages)
        )
