from langchain_ollama import ChatOllama 
import os
from dotenv import load_dotenv
class LlmClient:
    def __init__(self, model_, temperature_, base_url_):
        self.instance = ChatOllama(
            model=model_,
            temperature=temperature_,
            base_url=base_url_)