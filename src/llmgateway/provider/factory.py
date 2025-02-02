from .base import BaseLLM
from .enum import ProviderEnum
from .huggingface import Huggingface
from .litellm import Litellm
from .ola_krutrim import OlaKrutrim


def LLM_Factory(provider: str, **kwargs) -> BaseLLM:
    # if provider == ProviderEnum.HUGGINGFACE.value:
    #     return Huggingface(**kwargs)
    # elif provider == ProviderEnum.OLA_KRUTRIM.value:
    #     return OlaKrutrim(**kwargs)
    if any(provider == e.value for e in ProviderEnum):
        return Litellm(**kwargs)
    raise Exception("Unsupported provider specified.")
