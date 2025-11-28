from application.modules.cor.Handler import Handler
import os
from utils.utils import clean_for_tts
from infrastructure.TtsClient import TtsClient

class AudioFileDispatcherHandler(Handler):
    def handle(self, state)->bool:
        tts = TtsClient()
        UPLOAD_DIR = "uploads"
        REPLY_DIR = "reply"
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        os.makedirs(REPLY_DIR, exist_ok=True)
        tts.instance.tts_to_file(text=clean_for_tts(state["final_answer"]),file_path=os.path.join(REPLY_DIR,"reply.wav"))
        print("Success, create text to file")