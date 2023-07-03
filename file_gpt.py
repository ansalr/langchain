# pip install unstructured
# pip install python-magic-bin
# pip install chromadb

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI,VectorDBQA
from langchain.document_loaders import DirectoryLoader
import magic
import nltk

import os
openai_api = input("OPENAPI : ")
os.environ["OPENAI_API_KEY"] = openai_api

loader = DirectoryLoader('D:\Download 01\langchain\data\PaulGrahamEssaySmall',glob='**/*.txt')
document = loader.load()
text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0)
texts = text_splitter.split_documents(document)
embedding = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
docsearch = chroma.from_documents(texts,embedding)



