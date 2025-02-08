from litellm import embedding

# from ..base import BaseEmbedding


class LiteLLMEmbeddings(object):
    def load(self, model: str, api_key: str):
        return embedding(model=model, api_key=api_key, dimensions=5)
