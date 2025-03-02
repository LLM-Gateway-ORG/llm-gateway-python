from abc import ABC, abstractmethod
from typing import List

from langchain_core.documents.base import Document


class BaseLLM(ABC):
    def __init__(self, model_name: str, **kwargs) -> None:
        self._model_name = model_name

    @abstractmethod
    def completion(self, messages: list) -> dict:
        pass

    @abstractmethod
    def async_completion(self, messages: list) -> dict:
        pass


class AbstractVectorStore(ABC):
    @abstractmethod
    def persist(self, documents: List[Document]):
        pass

    @abstractmethod
    def retrieve(self, ids: List[str]) -> List[Document]:
        pass
