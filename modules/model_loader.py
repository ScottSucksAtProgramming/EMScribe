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

    def calculate_context_window(self, transcript):
        """
        Calculate the optimal context window size based on the transcript length.

        Args:
            transcript (str): The transcript text.

        Returns:
            int: The calculated context window size.
        """
        num_tokens = len(transcript) // 4  # Assuming average 4 characters per token

        # Define possible context window sizes
        context_sizes = [8192, 12288, 16384, 20480, 24576, 28672, 32768]
        optimal_context_window = max([size for size in context_sizes if size >= num_tokens] or [8192])
        return optimal_context_window

    def generate(self, prompt, context_window, stream=False):
        """
        Generates a response from the AI model based on the provided prompt and context window.

        Args:
            prompt (str): The input prompt for the model.
            context_window (int): The context window size for the model.
            stream (bool): Whether to stream the response or get it in a single output.

        Returns:
            str: The generated response from the model.
        """
        response = self.client.generate(
            model=self.model_name,
            prompts=[prompt],
            options={"num_ctx": context_window}  # Ensure num_ctx is correctly placed in options
        )
        return response.generations[0][0].text.strip()