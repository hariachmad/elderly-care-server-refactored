import asyncio
import whisper


class SttClient:
    _instance = None
    _lock = asyncio.Lock()

    def __new__(cls, modelSize):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    async def init(self, modelSize):
        if self._initialized:
            return
        
        loop = asyncio.get_event_loop()
        self._instance = await loop.run_in_executor(
            None, whisper.load_model, modelSize
        )
        self._initialized = True