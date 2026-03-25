import streamlit as st
from app.agent.builder import build_agent
from app.config.settings import settings
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


@st.cache_resource
def get_agent():
    return build_agent()


def process_user_query(prompt: str, thread_id: str | None = None) -> str:
    thread_id = thread_id or settings.DEFAULT_THREAD_ID
    agent = get_agent()

    logger.info("Processing user query: %s", prompt)

    try:
        response = agent.invoke(
            {"messages": [{"role": "user", "content": prompt}]},
            {"configurable": {"thread_id": thread_id}}
        )

        result = response["messages"][-1].content

        if isinstance(result, list):
            result = "\n".join(str(item) for item in result)

        return str(result)

    except Exception as e:
        logger.exception("Agent invoke failed")
        raise e