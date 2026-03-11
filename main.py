from dotenv import load_dotenv


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient # or Langchain ttavily for better experience
from langchain_tavily import tavily_search

tavily = TavilyClient()
@tool  #langchain is gng to format as metadata  and use in LLM call 
def Search(query: str) -> str:
    """
    Tool that searches over internet
    Args;
     query: The query to search for
     Returns: The Search results
    """
    print(f'Searching for {query}')
    return tavily.search(query)




llm = ChatOpenAI()
tools = [Search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-course")
    result = agent.invoke({"messages":HumanMessage(content="Bring the high paid job in iT roles from linkedIn")})
    print(result)


if __name__ == "__main__":
    main()
