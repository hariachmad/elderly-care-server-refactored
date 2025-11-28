from application.modules.cor.BlackListHandler import BlackListHandler
from application.modules.cor.InferenceHandler import InferenceHandler
from application.modules.cor.PageNavigatorHandler import PageNavigatorHandler
from application.modules.cor.AudioFileDispatcherHandler import AudioFileDispatcherHandler
from fastapi.responses import FileResponse
from fastapi import FastAPI,File, UploadFile
from infrastructure.LlmClient import LlmClient
import os
import datetime

model = os.getenv("LLM_MODEL", "gemma2:2b")
model_whisper = None
temperature = int(os.getenv("LLM_TEMPERATURE", 0))
base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/")
llm = LlmClient(model, temperature, base_url).instance

question = "i need help"
blacklist = BlackListHandler()
inference = InferenceHandler()
pageNavigator = PageNavigatorHandler()
audioFileDispatcher = AudioFileDispatcherHandler()
blacklist.set_next(inference).set_next(pageNavigator).set_next(audioFileDispatcher)
blacklist.handle(question)
