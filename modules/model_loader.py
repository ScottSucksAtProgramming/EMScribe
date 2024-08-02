from langchain_community.llms import Ollama

class ModelLoader:
    """
    A class to load and interact with AI models.

    Attributes:
        model_name (str): The name of the model to use.
        base_url (str): The base URL of the model API.
        context_window (int): The context window size for the model.
    """

    def __init__(self, model_name, base_url="http://localhost:11434", transcript_content=None):
        """
        Initializes the ModelLoader with the specified model name, base URL, and context window size.

        Args:
            model_name (str): The name of the model to use.
            base_url (str): The base URL of the model API.
            transcript_content (str): The content of the transcript to determine context window size.
        """
        self.base_url = base_url
        self.model_name = model_name
        self.context_window = self.calculate_context_window(len(transcript_content)) if transcript_content else 2048
        self.client = Ollama(base_url=base_url)

    def calculate_context_window(self, transcript_length):
        """
        Calculates the optimal context window size based on the transcript length.

        Args:
            transcript_length (int): The length of the transcript in characters.

        Returns:
            int: The optimal context window size.
        """
        # Estimate number of tokens (1 token ≈ 4 characters)
        num_tokens = transcript_length // 4

        # Define context window options
        context_window_options = [2048, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768]

        # Select the smallest context window size that can accommodate the transcript
        for window_size in context_window_options:
            if num_tokens <= window_size:
                return window_size
        return context_window_options[-1]

    def generate(self, prompt, stream=False):
        """
        Generates a response from the AI model based on the provided prompt.

        Args:
            prompt (str): The input prompt for the model.
            stream (bool): Whether to stream the response or get it in a single output.

        Returns:
            str: The generated response from the model.
        """
        response = self.client.generate(
            model=self.model_name,
            prompts=[prompt],
            options={"num_ctx": self.context_window}  # Ensure num_ctx is correctly placed in options
        )
        return response.generations[0][0].text.strip()