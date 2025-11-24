from langchain_classic.output_parsers import ResponseSchema
from langchain_core.prompts import PromptTemplate
from typing import List

class AiAgent:
    def __init__(self):
        self.predefined_intents = []
        self.blaclist_keywords = []
        self.blacklist_contexts = []
        self.response_schemas : List[ResponseSchema]= []
        self.prompt_template : PromptTemplate = None
        
        