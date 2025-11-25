from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from typing import List

class AiAgent:
    def __init__(self, chain):
        self.chain = chain

        
        