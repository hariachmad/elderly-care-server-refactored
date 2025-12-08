from typing import List
from application.modules.ai_agent.AiAgent import AiAgent

class AiAgentBuilder:
    def __init__(self):
        self.predefined_intents = []
        self.blacklist_keywords = []
        self.prompt_template = None
        self.parser = None
        self.llm = None
    
    def set_predefined_intents(self, intents: List[str]):
        self.predefined_intents = intents
        return self
    
    def set_blacklist_keywords(self, keywords: List[str]):
        self.blaclist_keywords = keywords
        return self
        
    def set_prompt_template(self, prompt_template):
        self.prompt_template = prompt_template
        return self
    
    def set_llm(self, llm):
        self.llm = llm
        return self
    
    def set_parser(self, parser):
        self.parser = parser
        return self
    
    def build(self):
        if self.predefined_intents is None:
            raise ValueError("predefined_intents must be set")
        if self.blacklist_keywords is None:
            raise ValueError("blacklist_keywords must be set")
        if self.prompt_template is None:
            raise ValueError("template must be set")
        
        chain = self.prompt_template | self.llm | self.parser        
        
        return AiAgent(chain)