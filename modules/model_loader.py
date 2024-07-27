from langchain_community.llms import Ollama

class ModelLoader:
    def __init__(self, model_name, base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self.ollama = Ollama(base_url=self.base_url)

    def generate(self, prompt):
        response = self.ollama.generate(
            model=self.model_name,
            prompts=[prompt],
            stream=False
        )
        return response