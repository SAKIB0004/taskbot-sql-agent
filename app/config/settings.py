import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_TITLE: str = os.getenv("APP_TITLE", "TaskBot - Task Management Agent")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "qwen/qwen3-32b")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data/my_tasks.db")
    DEFAULT_THREAD_ID: str = os.getenv("DEFAULT_THREAD_ID", "taskbot-thread-1")


settings = Settings()