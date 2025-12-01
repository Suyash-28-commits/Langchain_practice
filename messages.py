from langchain_core.messages import HumanMessage, SystemMessage , AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    openai_api_key = OPENROUTER_API_KEY,
    openai_api_base = OPENROUTER_API_BASE
)

messages = [
    SystemMessage(content="You are a helpful AI assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)