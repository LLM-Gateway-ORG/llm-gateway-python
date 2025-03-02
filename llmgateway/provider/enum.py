from ..base import BaseEnum


class ProviderEnum(BaseEnum):
    HUGGINGFACE = "huggingface"
    OLA_KRUTRIM = "ola_krutrim"
    LITELLM = "litellm"


class VectorStoreProviderEnum(BaseEnum):
    INMEMORY = "in-memory"
    CHROMA = "chromadb"
    FAISS = "faiss"
    QDRANT = "qdrant"
    PINECONE = "pinecone"
    WEAVIATE = "weaviate"
    MILVUS = "milvus"
