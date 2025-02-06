from base import BaseEnum


class ModesEnum(BaseEnum):
    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"
    IMAGE_GENERATION = "image_generation"
    VECTOR_STORE = "vector_store"


class ProcessorType(Enum):
    WEB = "web"
    DOCUMENT = "document"
    YOUTUBE = "youtube"
