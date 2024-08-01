from modules.prompts.narrative_prompts import narrative_prompts
class NarrativeManager:
    """
    Manages the generation of narratives from extracted data using a language model.

    Attributes:
        model_loader (ModelLoader): The model loader used to generate text.
        prompt_manager (PromptManager): The prompt manager used to create prompts.
    """

    def __init__(self, model_loader, prompt_manager):
        """
        Initializes the NarrativeManager with a model loader and a prompt manager.

        Args:
            model_loader (ModelLoader): The model loader used to generate text.
            prompt_manager (PromptManager): The prompt manager used to create prompts.
        """
        self.model_loader = model_loader
        self.prompt_manager = prompt_manager

    def generate_narrative(self, data, max_tokens=4096):
        """
        Generates a narrative from the given data.

        Args:
            data (str): The extracted data to generate a narrative from.
            max_tokens (int, optional): The maximum number of tokens for the generated narrative. Defaults to 1024.

        Returns:
            str: The generated narrative.
        """
        prompt = self.prompt_manager.create_narrative_prompt(data)
        response = self.model_loader.generate(prompt, max_tokens=max_tokens)
        return response

    def generate_narrative_from_chunks(self, chunks):
        complete_narrative = ""
        
        for chunk in chunks:
            for section in narrative_prompts["presoaped_format"]:
                prompt_template = narrative_prompts["presoaped_format"][section]
                prompt = prompt_template.format(data=chunk)
                narrative_section = self.model_loader.generate(prompt)
                complete_narrative += narrative_section + "\n\n"
        
        return complete_narrative