from ...constants import ModesEnum
from .chat import HuggingfaceChat


def HuggingFaceFactory(mode: str, **kwargs):
    # if mode == ModesEnum.CHAT:
    #     return HuggingfaceChat(**kwargs)
    raise ValueError("Invalid mdde for HuggingFace Provider")
