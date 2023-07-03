import os
serp_api = input("SERPAPI : ")
openai_api = input("OPENAPI : ")
os.environ["SERPAPI_API_KEY"] = serp_api
os.environ["OPENAI_API_KEY"] = openai_api

from langchain.agents import load_tools,initialize_agent
from langchain.prompts import prompt
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

tool_name = ['serpapi']
tools = load_tools(tool_name)

agent = initialize_agent(tools,llm=llm,agent="zero-shot-react-description",verbose=True)
agent.run('what is lang chain?')
agent.run('ceo of microsoft')