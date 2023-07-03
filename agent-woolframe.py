# pip install wolframalpha

import os
serp_api = input("SERPAPI : ")
openai_api = input("OPENAPI : ")
wolfram_api = input("WORLFARM_API : ")
os.environ["SERPAPI_API_KEY"] = serp_api
os.environ["OPENAI_API_KEY"] = openai_api
os.environ["WOLFRAM_ALPHA_APPID"] = wolfram_api

from langchain.agents import load_tools,initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

tool_names = ["wolfram-alpha","serpapi"]
tool = load_tools(tool_names)

agent = initialize_agent(llm=llm,tools=tool,agent="zero-shot-react-description",verbose=True)
agent.run("what is asthenosphere?")