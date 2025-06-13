from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    SseServerParams,
)
#Uncomment below for debugging
# import litellm
#litellm._turn_on_debug()

toolset = MCPToolset(
      connection_params=SseServerParams(
        url="http://localhost:8080/sse",
      )
  )

root_agent = LlmAgent(
    name="mcp_sse_consumer",
    model=LiteLlm(model="azure/gpt-4o-mini"),
    description=(
        "Agent to answer questions about user Information and User timezone information."
    ),
    instruction=(
        """
        You are a helpful AI assistant. You can answer questions, provide information in a nicely manner, and assist with user-related tasks.
        Guidelines:
        1. Always respond in a friendly and helpful manner.
        5. Don't build any assumptions about the user or their data. Only provide information retrieved from the tool.
        """
    ),
    tools=[toolset]
)