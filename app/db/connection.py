from langchain_community.utilities import SQLDatabase
from app.config.settings import settings


def get_database() -> SQLDatabase:
    return SQLDatabase.from_uri(settings.DATABASE_URL)