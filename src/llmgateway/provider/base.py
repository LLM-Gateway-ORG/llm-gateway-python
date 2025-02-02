from abc import ABC, abstractmethod


class BaseLLM(ABC):
    def __init__(self, model_name: str, **kwargs) -> None:
        self._model_name = model_name

    @abstractmethod
    def completion(self, messages: list) -> dict:
        pass

    @abstractmethod
    def async_completion(self, messages: list) -> dict:
        pass
