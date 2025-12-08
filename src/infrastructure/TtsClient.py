from TTS.api import TTS

class TtsClient:
    _instance = None  # static variable untuk singleton

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TtsClient, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self.instance = TTS("tts_models/en/ljspeech/tacotron2-DDC", gpu=True)
        self._initialized = True