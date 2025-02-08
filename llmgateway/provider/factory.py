from .base import BaseLLM
from .enum import ProviderEnum
from .huggingface.factory import HuggingFaceFactory
from .litellm.factory import LiteLLMfactory
from .ola_krutrim.factory import OlaKrutrimFactory


def LLM_Factory(provider: str, **kwargs) -> BaseLLM:
    if provider == ProviderEnum.HUGGINGFACE.value:
        return HuggingFaceFactory(**kwargs)
    elif provider == ProviderEnum.OLA_KRUTRIM.value:
        return OlaKrutrimFactory(**kwargs)
    elif provider == ProviderEnum.LITELLM.value:
        return LiteLLMfactory(**kwargs)
    raise ValueError("Unsupported provider specified.")
