from langchain.agents import create_agent
from app.agent.llm import get_llm
from app.agent.toolkit import get_tools
from app.agent.memory import get_checkpointer
from app.agent.prompt import SYSTEM_PROMPT


def build_agent():
    llm = get_llm()
    tools = get_tools()
    checkpointer = get_checkpointer()

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer
    )

    return agent