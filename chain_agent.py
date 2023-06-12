from langchain import OpenAI, ConversationChain
import os
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)
conversation.predict(input="Hi there!")
conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
conversation.predict(input="What was the first thing I said to you?")
conversation.predict(input="what is an alternative phrase for the first thing I said to you?")
conversation.predict(input="how old are you ?")