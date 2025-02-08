from ...constants import ModesEnum
from .chat import LiteLLMChat
from .embedding import LiteLLMEmbeddings


def LiteLLMfactory(mode: str, **kwargs):
    if mode == ModesEnum.CHAT:
        return LiteLLMChat(**kwargs)
    elif mode == ModesEnum.EMBEDDING:
        return LiteLLMChat(**kwargs)
    raise ValueError("Invalid mdde for LiteLLM Provider")
