import os
import logging

import chainlit as cl
from chainlit.data.chainlit_data_layer import ChainlitDataLayer
from chainlit.data.storage_clients.s3 import S3StorageClient
from openai import AsyncOpenAI
import httpx
from dotenv import load_dotenv
from typing import Optional, Dict
from dataclasses import dataclass


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("chainliterate")


load_dotenv()

@dataclass
class AppConfig:
    api_key: str = os.getenv("OPENROUTER_API_KEY")
    base_url: str = "https://openrouter.ai/api/v1"
    model: str = "openrouter/auto"
    temperature: float = 0.2
    referrer: str = "http://localhost"
    title: str = "chainliterate"
    system_prompt: str = "You are chainliterate, a helpful, concise assistant."
    ref: str = "http://localhost"
    title: str = "chainliterate"
    httpx_timeout_s: int = 300  # Timeout for HTTPX client in seconds

config = AppConfig()




if config.api_key:
    logger.info("OPENROUTER_API_KEY ending in " + config.api_key[-2:] + " detected")
else:
    raise ValueError("OPENROUTER_API_KEY environment variable is required")
logger.info(f"using OpenRouter base URL: {config.base_url} for model {config.model}")

@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user

@cl.on_chat_start
async def on_chat_start():
    system_prompt = os.getenv(
        "SYSTEM_PROMPT",
        config.system_prompt,
    )
    cl.user_session.set(
        "history",
        [{"role": "system", "content": system_prompt}],
    )
    http_client = httpx.AsyncClient(timeout=config.httpx_timeout_s)
    oai_client = AsyncOpenAI(
        base_url=config.base_url,
        api_key=config.api_key,
        http_client=http_client,
    )
    cl.user_session.set("oai_client", oai_client)
    logger.info(f"Beginning chat for session {cl.user_session.get('id')}")


@cl.on_message
async def on_message(message: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    client = cl.user_session.get("oai_client")
   
    logger.info("Streaming response from OpenRouter via OpenAI SDK")
    

    with cl.Step(type="tool",name=config.model):
        stream = await client.chat.completions.create(
        model=config.model,
        messages=history,
        temperature=config.temperature,
        extra_headers={
            "HTTP-Referer": config.referrer,
            "X-Title": config.title,
        },
        stream=True,
        )
        async for part in stream:
            token = part.choices[0].delta.content or ""
            if token:
                await msg.stream_token(token)

        await msg.update()
        history.append({"role": "assistant", "content": msg.content})
        cl.user_session.set("history", history)


@cl.on_chat_end
async def on_chat_end():
    '''
    Perform any cleanup actions needed at the end of a chat session.
    '''
    logging.info(f"Chat ended for session{cl.user_session.get('id')}")
    try:
        client = cl.user_session.get("oai_client")
        if client:
            await client.close()
    except Exception as e:
        logging.warning(f"Error closing OpenAI client: {e}")