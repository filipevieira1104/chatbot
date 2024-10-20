from decouple import config
from langchain_cohere import ChatCohere
from langchain.schema import StrOutputParser
from prompting import chat_prompt_template

COHERE_API_KEY = config('COHERE_API_KEY')

model = ChatCohere(model="command-r-plus")

chain = (chat_prompt_template | model | StrOutputParser())