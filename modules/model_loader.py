from langchain_community.llms import Ollama
class ModelLoader:
    """
    A class to load and interact with AI models.

    Attributes:
        model_name (str): The name of the model to use.
        base_url (str): The base URL of the model API.
        context_window (int): The maximum context window size for the model.
    """

    def __init__(self, model_name, base_url="http://localhost:11434"):
        """
        Initializes the ModelLoader with the specified model name and base URL.

        Args:
            model_name (str): The name of the model to use.
            base_url (str): The base URL of the model API.
        """
        self.base_url = base_url
        self.model_name = model_name
        self.client = Ollama(base_url=base_url)
        self.context_window = 32768  # Fixed context window size

    def generate(self, prompt):
        """
        Generates a response from the AI model based on the provided prompt and context window.

        Args:
            prompt (str): The input prompt for the model.

        Returns:
            str: The generated response from the model.
        """
        response = self.client.generate(
            model=self.model_name,
            prompts=[prompt],
            options={"num_ctx": self.context_window}  # Ensure num_ctx is correctly placed in options
        )

        # Extract and return the text from the first generation response
        return response.generations[0][0].text.strip()