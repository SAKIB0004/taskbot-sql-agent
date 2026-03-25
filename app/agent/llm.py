from langchain_groq import ChatGroq
from app.config.settings import settings


def get_llm() -> ChatGroq:
    return ChatGroq(
        model=settings.MODEL_NAME,
        temperature=0,
        max_retries=2,
    )