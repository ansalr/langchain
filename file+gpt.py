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
os.environ["OPENAI_API_KEY"] = "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"

loader = DirectoryLoader('D:\Download 01\langchain\data\PaulGrahamEssaySmall',glob='**/*.txt')
document = loader.load()
print(document)
