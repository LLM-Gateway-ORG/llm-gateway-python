from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def has_value(cls, value):
        return any(value == item.name for item in cls)

    @classmethod
    def fetch(cls, value):
        for item in cls:
            if item.value == value:
                return item
        raise ValueError(f"{value} is not a valid value for {cls.__name__}")


class ProviderEnum(BaseEnum):
    AI21 = "ai21"
    ALEPH_ALPHA = "aleph_alpha"
    ANTHROPIC = "anthropic"
    ANYSCALE = "anyscale"
    AZURE = "azure"
    AZURE_AI = "azure_ai"
    BEDROCK = "bedrock"
    CEREBRAS = "cerebras"
    CLOUDFLARE = "cloudflare"
    CODESTRAL = "codestral"
    COHERE = "cohere"
    COHERE_CHAT = "cohere_chat"
    DATABRICKS = "databricks"
    DEEPINFRA = "deepinfra"
    DEEPSEEK = "deepseek"
    FIREWORKS_AI = "fireworks_ai"
    FIREWORKS_AI_EMBEDDING = "fireworks_ai-embedding-models"
    FRIENDLIAI = "friendliai"
    GEMINI = "gemini"
    GROQ = "groq"
    HUGGINGFACE = "huggingface"  # Not in litellm
    MISTRAL = "mistral"
    NLP_CLOUD = "nlp_cloud"
    OLLAMA = "ollama"
    OLA_KRUTRIM = "ola_krutrim"
    OPENAI = "openai"
    OPENROUTER = "openrouter"
    PALM = "palm"
    PERPLEXITY = "perplexity"
    REPLICATE = "replicate"
    SAGEMAKER = "sagemaker"
    TEXT_COMPLETION_CODESTRAL = "text-completion-codestral"
    TEXT_COMPLETION_OPENAI = "text-completion-openai"
    TOGETHER_AI = "together_ai"
    VERTEX_AI_AI21 = "vertex_ai-ai21_models"
    VERTEX_AI_ANTHROPIC = "vertex_ai-anthropic_models"
    VERTEX_AI_CHAT = "vertex_ai-chat-models"
    VERTEX_AI_CODE_CHAT = "vertex_ai-code-chat-models"
    VERTEX_AI_CODE_TEXT = "vertex_ai-code-text-models"
    VERTEX_AI_EMBEDDING = "vertex_ai-embedding-models"
    VERTEX_AI_IMAGE = "vertex_ai-image-models"
    VERTEX_AI_LANGUAGE = "vertex_ai-language-models"
    VERTEX_AI_LLAMA = "vertex_ai-llama_models"
    VERTEX_AI_MISTRAL = "vertex_ai-mistral_models"
    VERTEX_AI_TEXT = "vertex_ai-text-models"
    VERTEX_AI_VISION = "vertex_ai-vision-models"
    VOYAGE = "voyage"
    XAI = "xai"
