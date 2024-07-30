from langchain_community.llms import Ollama


class ModelLoader:
    """
    A class to load and interact with AI models.

    Attributes:
        model_name (str): The name of the model to use.
        base_url (str): The base URL of the model API.
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

    def generate(self, prompt, stream=False):
        """
        Generates a response from the AI model based on the provided prompt.

        Args:
            prompt (str): The input prompt for the model.
            stream (bool): Whether to stream the response or get it in a single output.

        Returns:
            str: The generated response from the model.
        """
        response = self.client.generate(model=self.model_name, prompts=[prompt])
        return response.generations[0][0].text.strip()
