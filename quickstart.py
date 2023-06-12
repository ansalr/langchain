# pip install langchain
# pip install OpenAI


import os 
os.environ["OPENAI_API_KEY"]= "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"

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


llm = OpenAI(temperature=0.9)


prompt = PromptTemplate(input_variables=['food'],
                        template="top 5 destination in india to have {food}?")

print(llm(prompt.format(food="coffe")))