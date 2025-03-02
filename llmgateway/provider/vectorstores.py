import os

from base import AbstractVectorStore
from langchain_community.vectorstores.chroma import Chroma

from llmgateway.provider.enum import VectorStoreProviderEnum


def get_vector_store(
    type: str, collection: str, embedding: any, **kwargs
) -> AbstractVectorStore:
    if type == VectorStoreProviderEnum.CHROMA:
        return ChromaVectorStore()
    raise Exception("Invalid Vector Store")


class ChromaVectorStore(AbstractVectorStore):
    """
    Reference :- https://github.com/langchain-ai/langchain/issues/15944
    """

    def __init__(self, dbpath, *kwargs):
        dbpath = os.path.join(os.getcwd(), dbpath)
        self.db = Chroma(persist_directory=kwargs.get("persist_directory"))
        super().__init__()

    def persist(self, documents):
        pass
