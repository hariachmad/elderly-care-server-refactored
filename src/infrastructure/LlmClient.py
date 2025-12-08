from langchain_ollama import ChatOllama 
class LlmClient:
    _instance = None
    def __new__(cls, model_, temperature_, base_url_):
        if cls._instance is None:
            cls._instance = super(LlmClient, cls).__new__(cls)
            cls._instance.instance = ChatOllama(
                model=model_,
                temperature=temperature_,
                base_url=base_url_,
            )
        return cls._instance