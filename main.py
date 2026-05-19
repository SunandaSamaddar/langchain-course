from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
# from tavily import TavilyClient


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )

# llm = ChatOpenAI(model="gpt-5")
llm = ChatOpenAI(model="gpt-5-nano-2025-08-07")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)  # The Agent now must return an AgentResponse object not string

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over the internet for information.
#     Args:
#         query: The query to search for.
#     Returns:
#         The search result.
#     """
#     print(f"Searching for {query}")
#     # print("Kolkata weather is sunny")
#     # print("Tokyo weather is sunny")
#     return tavily.search(query=query)


# llm = ChatOpenAI(model="gpt-5-nano-2025-08-07")
# tools = [search]
# agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    # result = agent.invoke({
    #     "messages": HumanMessage(content="What is the weather in Tokyo?")
    # })
    result = agent.invoke(
        {
            "messages": HumanMessage(
                # content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"
                content="search for 3 job postings for an ai engineer using langchain in the Bangalore area on linkedin and list their details?"
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
