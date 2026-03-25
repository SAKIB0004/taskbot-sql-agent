from langchain_community.agent_toolkits import SQLDatabaseToolkit
from app.db.connection import get_database
from app.agent.llm import get_llm


def get_tools():
    db = get_database()
    llm = get_llm()
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return toolkit.get_tools()