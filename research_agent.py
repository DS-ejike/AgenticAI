import os

from deepagents import create_deep_agent
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
    raise RuntimeError(
        "GOOGLE_API_KEY is required. Set it in the shell or in a .env file."
    )

internet_search = {"google_search": {}}

research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    tools=[internet_search],
    system_prompt=research_instructions,
)


def main() -> None:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is langgraph?"}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
