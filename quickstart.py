# pip install langchain
# pip install OpenAI


import os 
openai_api = input("OPENAPI : ")
os.environ["OPENAI_API_KEY"] = openai_api
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


llm = OpenAI(temperature=0.9)


prompt = PromptTemplate(input_variables=['food'],
                        template="top 5 destination in india to have {food}?")

print(llm(prompt.format(food="coffe")))