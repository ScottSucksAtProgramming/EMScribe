from langchain_community.llms import Ollama

class ModelLoader:
    """
    A class to interface with the AI model.

    Attributes:
        base_url (str): The base URL of the Ollama server.
        model_name (str): The name of the model to use.
    """

    def __init__(self, base_url: str, model_name: str):
        """
        Initializes the ModelLoader with the base URL and model name.

        Args:
            base_url (str): The base URL of the Ollama server.
            model_name (str): The name of the model to use.
        """
        self.model = Ollama(base_url=base_url)
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        """
        Generates a response from the model for a given prompt.

        Args:
            prompt (str): The prompt to send to the model.

        Returns:
            str: The generated response from the model.
        """
        response = self.model.generate(
            model=self.model_name,
            prompts=[prompt],
            stream=False
        )
        return response.generations[0][0].text.strip()