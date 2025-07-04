import os
import asyncio
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from i18n_readme.prompt import (
    TRANSLATE_SYSTEM_PROMPT,
    TRANSLATE_USER_PROMPT_TEMPLATE,
    TRANSLATE_AGENT_DESCRIPTION,
)


def create_litellm_model(
    model: str = os.getenv("API_MODEL_NAME"),
    api_key: str = os.getenv("API_KEY"),
    api_base: str = os.getenv("API_BASE_URL"),
):
    return LiteLlm(
        model=f"openai/{model}",
        api_key=api_key,
        api_base=api_base,
    )


def get_agent() -> LlmAgent:
    root_agent = LlmAgent(
        model=create_litellm_model(),
        name="clip_agent",
        description=TRANSLATE_AGENT_DESCRIPTION,
        instruction=TRANSLATE_SYSTEM_PROMPT,
    )
    return root_agent


async def run_agent(target_language: str, source_content: str) -> str:
    prompt = TRANSLATE_USER_PROMPT_TEMPLATE.format(
        target_language=target_language, source_content=source_content
    )
    app_name = "translate_app"
    user_id = "user_01"
    session_id = "session_01"

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )

    runner = Runner(
        app_name=app_name, agent=get_agent(), session_service=session_service
    )

    content = types.Content(role="user", parts=[types.Part(text=prompt)])
    events_async = runner.run_async(
        session_id=session_id, user_id=user_id, new_message=content
    )
    res = ""
    async for event in events_async:
        if event.is_final_response():
            res = event.content.parts[0].text

    return res


if __name__ == "__main__":
    with open("./README.md", "r", encoding="utf-8") as f:
        source_content = f.read()
    res = asyncio.run(run_agent(target_language="en", source_content=source_content))
    print(res)
