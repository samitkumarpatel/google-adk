import requests
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

class ExternalAgentLiteLlm(LiteLlm):
    def __init__(self, endpoint):
        super().__init__(self, "")  # Call the parent class's __init__ method
        self.endpoint = endpoint
        print(f"#######LiteLlm initialized with endpoint: {self.endpoint}")

    def predict(self, prompt):
        """
        Sends the prompt to the external agent and returns the response.
        """
        try:
            response = requests.get(f"{self.endpoint}?prompt={prompt}")
            response.raise_for_status()  # Raise an error for HTTP issues
            return response.text  # Assuming the response is plain text
        except requests.exceptions.RequestException as e:
            print(f"Error calling external agent: {e}")
            return None

# Create an instance of the custom LiteLlm
external_llm = ExternalAgentLiteLlm(endpoint="http://localhost:8080/ai")

# Create the root agent using the custom LiteLlm
root_agent = Agent(
    name="spring_ai_agent",
    llm=external_llm  # Use the custom LiteLlm
)