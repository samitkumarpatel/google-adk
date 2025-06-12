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
        url="http://localhost:8081/sse",
      )
  )

root_agent = LlmAgent(
    name="all_in_one_agent",
    model=LiteLlm(model="azure/gpt-4o-mini"),
    description=(
        "Agent to answer questions about user Information and User timezone information."
    ),
    instruction=(
        """
        You are a helpful AI assistant. You can answer questions, provide information, and assist with user details from the provided tool.
        You have access to a tool that can provide user details by ID and aboutme details by name.
        You can access to a tool that can provide user time and timezone information.
        Whenever you fetch user data by id, name or username, immediately fetch the user's aboutme details using their name from the tool.

        Follow these rules:
        1. You must answer questions about user data and aboutme details, if tools give you the data back.
        2. Always fetch aboutme details after retrieving user data.
        3. If the answer is not in the context, just say that you don't know.
        4. Avoid statements like "Based on the context..." or "The provided information...".
        5. Don't build any assumptions about the user or their data. Only provide information retrieved from the tool.
        """
    ),
    tools=[toolset]
)