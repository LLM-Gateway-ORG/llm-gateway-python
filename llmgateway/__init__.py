from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from .constants import ModesEnum
from .provider import BaseLLM, LLM_Factory
from .provider.enum import ProviderEnum
from .utils import get_model_list


class BaseLLMGeneration(ABC):
    mode = None  # Should be set in the subclass
    provider = None

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        # Parse Model String
        self._parse_model()

        self._model_details = self._fetch_model_details()

        # Load model lazily
        self._llm = None

    def _parse_model(self) -> None:
        """Parses the model string into provider and model name."""
        if ":" not in self.model_name and self.model.count(":") > 0:
            raise ValueError("Invalid model format. Expected '<provider>:<model_name>'")

        parser_string = self.model_name.split(":", 1)
        self.provider = ProviderEnum.fetch(parser_string[0])
        self.model_name = parser_string[1]

    def _fetch_model_details(self) -> Dict[str, str]:
        """Fetches model details from available models."""
        models_list = get_model_list()
        if (
            self.model_name not in models_list
            or models_list[self.model_name].get("mode") != self.mode
        ):
            raise ValueError(
                f"Model '{self.model_name}' not found or incompatible with mode '{self.mode}'"
            )
        return models_list[self.model_name]

    def load_model(self):
        """Lazy loads the model when needed."""
        if self._llm is None:
            self._llm = self._load_model_impl()
        return self._llm

    @abstractmethod
    def _load_model_impl(self):
        """To be implemented by subclasses for model-specific loading."""
        pass

    @abstractmethod
    def generate(self, messages: List[str]):
        """Generates text based on messages using the LLM."""
        pass


class Chat(BaseLLMGeneration):
    mode = ModesEnum.CHAT

    def __init__(
        self, model_name: str, sync: bool = True, api_key: Optional[str] = None
    ) -> None:
        self.sync = sync
        self.__api_key = api_key

        super().__init__(model_name=model_name)

    @property
    def api_key(self) -> str:
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        self.__api_key = api_key

    def _load_model_impl(self) -> BaseLLM:
        return LLM_Factory(
            provider=self.provider,
            api_key=self.api_key,
            model_name=self.model_name,
        )

    def generate(self, messages: List[str]) -> None:
        return (
            self._llm.completion(messages)
            if self.sync
            else self._llm.async_completion(messages)
        )


class Completion(BaseLLMGeneration):
    mode = ModesEnum.COMPLETION

    def __init__(self) -> None:
        pass


class Embedding(object):
    def __init__(self, model_name: str, api_key: Optional[str] = None) -> None:
        self.model_name = model_name
        self.__api_key = api_key


class ImageGeneration(object):
    def __init__(self) -> None:
        pass


class VectorStore(object):
    def __init__(self) -> None:
        pass
