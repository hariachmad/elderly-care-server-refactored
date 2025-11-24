from langchain_classic.output_parsers import ResponseSchema
from typing import List

class AiAgent:
    def __init__(self):
        self.predefined_intents = []
        self.blaclist_keywords = []
        self.blacklist_contexts = []
        self.response_schemas : List[ResponseSchema]= []
        
        