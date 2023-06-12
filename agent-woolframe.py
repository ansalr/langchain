# pip install wolframalpha

import os
os.environ["SERPAPI_API_KEY"] = "09e893ba144668563a78ec381a731dd6bee17e703e51729ead944f1c9f19a0a3"
os.environ["OPENAI_API_KEY"] = "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"
os.environ["WOLFRAM_ALPHA_APPID"] ="56HE7A-KKLKR7XA8L"

from langchain.agents import load_tools,initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

tool_names = ["wolfram-alpha","serpapi"]
tool = load_tools(tool_names)

agent = initialize_agent(llm=llm,tools=tool,agent="zero-shot-react-description",verbose=True)
agent.run("what is asthenosphere?")