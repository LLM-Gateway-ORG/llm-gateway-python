from src.llmgateway.constants import ModesEnum

from .chat import OlaKrutrimChat


def OlaKrutrimFactory(mode: str, **kwargs):
    # if mode == ModesEnum.CHAT:
    #     return OlaKrutrimChat(**kwargs)
    raise ValueError("Invalid mdde for Ola Krutrim Provider")
