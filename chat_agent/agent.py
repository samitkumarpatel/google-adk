import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="chat_agent",
    model=LiteLlm(model="ollama_chat/llama3.1"),
    description=(
        "Agent to answer questions from user"
    ),
    instruction=(
        "You are a helpful agent who can answer user questions in nicely manner."
    )
)