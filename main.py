from dotenv import load_dotenv


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import  TavilySearch
from pydantic import BaseModel,Field
from typing import List

class Source(BaseModel):
    url:str = Field(description="URl of the Source")



class AgentResponse(BaseModel):
    answer:str = Field(description="Answer to the query")
    sources:List[Source] = Field(default_factory=list,description="List of sources used to generate the Answer")
    


llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
    print("Hello from langchain-course")
    result = agent.invoke({"messages":HumanMessage(content="Bring the high paid job in iT roles from linkedIn")})
    print(f'{result}')


if __name__ == "__main__":
    main()
