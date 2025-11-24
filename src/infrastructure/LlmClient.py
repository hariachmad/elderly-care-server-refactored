from langchain_ollama import ChatOllama 
import os
from dotenv import load_dotenv
class LlmClient:
    def __init__(self):
        self.llm = ChatOllama(
            model=os.getenv("LLM_MODEL", "gemma2:2b"),
            temperature=int(os.getenv("LLM_TEMPERATURE", 0)),
            base_url=os.getenv("LLM_BASE_URL", "http://localhost:11434/")
        )