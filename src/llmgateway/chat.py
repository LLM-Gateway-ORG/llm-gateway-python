from typing import List, Optional

from helpers import get_model_list
from provider import BaseLLM, LLM_Factory


class Chat(object):
    def __init__(
        self,
        model_name: str,
        sync: bool = True,
        api_key: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        self.sync = sync
        self.model_name = model_name
        self.__api_key = api_key
        self.__username = username
        self.__password = password

        self.__model_details = self.__fetch_model_details(model_name)

        # Load Model
        self.__llm = self.__load_model()

    @property
    def api_key(self) -> str:
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        self.__api_key = api_key

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str) -> None:
        self.__username = username

    @property
    def passowrd(self) -> str:
        return self.__password

    @passowrd.setter
    def password(self, passowrd: str) -> None:
        self.__password = passowrd

    def __load_model(self) -> BaseLLM:
        provider = self.__fetch_provider()
        return LLM_Factory(
            provider=provider,
            api_key=self.api_key,
            username=self.username,
            password=self.password,
            model_name=self.model_name,
        )

    def __fetch_model_details(self, model_name: str) -> dict:
        models_list = get_model_list()
        if model_name not in models_list:
            raise ValueError("Model Not Found !!")
        return models_list[model_name]

    def __fetch_provider(self) -> str:
        return self.__model_details.get("provider")

    def generate(self, messages: List[str]) -> None:
        return (
            self.__llm.completion(messages)
            if self.sync
            else self.__llm.async_completion(messages)
        )


if __name__ == "__main__":
    import asyncio

    async def main():
        chat_obj = Chat(
            model_name="groq/gemma2-9b-it",
            sync=False,
            api_key="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",
        )
        response = await chat_obj.generate(
            [{"role": "user", "content": "How are you?"}]
        )
        async for chunk in response:
            print(chunk.choices[0].delta.content, end="")

    asyncio.run(main())
