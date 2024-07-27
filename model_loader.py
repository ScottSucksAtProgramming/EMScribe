from langchain_community.llms import Ollama

class ModelLoader:
    def __init__(self, base_url="http://localhost:11434", model_name="llama3.1"):
        self.base_url = base_url
        self.model_name = model_name
        self.model = Ollama(base_url=base_url)

    def generate(self, prompt):
        response = self.model.generate(
            model=self.model_name,
            prompts=[prompt],
            stream=False
        )
        return response.generations[0][0].text.strip()
    
    def set_model(self, model_name):
        self.model_name = model_name