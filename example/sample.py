import asyncio

from llm_gateway_core import Chat


async def main():
    chat_obj = Chat(
        model_name="groq/gemma2-9b-it",
        sync=False,
        api_key="<api-key>",
    )
    response = await chat_obj.generate([{"role": "user", "content": "How are you?"}])
    async for chunk in response:
        print(chunk.choices[0].delta.content, end="")


asyncio.run(main())
