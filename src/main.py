from application.modules.cor.BlackListHandler import BlackListHandler
from application.modules.cor.InferenceHandler import InferenceHandler
from application.modules.cor.PageNavigatorHandler import PageNavigatorHandler
from application.modules.cor.AudioFileDispatcherHandler import AudioFileDispatcherHandler
from fastapi.responses import FileResponse
from fastapi import FastAPI,File, UploadFile
import whisper
from infrastructure.LlmClient import LlmClient
import asyncio
import os
import datetime
from infrastructure.TtsClient import TtsClient
from infrastructure.SocketIoClient import SocketIoClient

app = FastAPI()
model = os.getenv("LLM_MODEL", "gemma2:2b")
model_whisper = None
temperature = int(os.getenv("LLM_TEMPERATURE", 0))
base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/")
llm = LlmClient(model, temperature, base_url).instance

@app.on_event("startup")
async def startup_event():
    sio = SocketIoClient() #singleton initialization
    tts= TtsClient() #singleton initialization
    global model_whisper
    loop = asyncio.get_event_loop()
    model_whisper = await loop.run_in_executor(None, whisper.load_model, "small")
    print("✅ Whisper model loaded successfully!")
    llm.invoke("Lets Warm Up")
    print("✅ Warm-up finished!")
@app.post("/transcribe")
async def upload(file: UploadFile = File(...)):
    global model_whisper
    REPLY_DIR = "reply"
    UPLOAD_DIR = "uploads"
    start_time = datetime.datetime.now()  # 
    print(f"🚀 Start transcribing at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    global updated_file
    if not file.filename.lower().endswith(".wav"):
        return {"error": "Only .wav files are allowed"}
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    print(f"File '{file.filename}' uploaded successfully!")
    print("🧠 Transcribing with Whisper...")
    result = model_whisper.transcribe(file_path, language="english")
    print(result["text"])
    print("Transcribed with Whisper")

    blacklist = BlackListHandler()
    inference = InferenceHandler()
    pageNavigator = PageNavigatorHandler()
    audioFileDispatcher = AudioFileDispatcherHandler()
    blacklist.set_next(inference).set_next(pageNavigator).set_next(audioFileDispatcher)

    blacklist.handle(result["text"])
    end_time = datetime.datetime.now() 
    duration = (end_time - start_time).total_seconds()
    print(f"🏁 Finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')} (Duration: {duration:.2f} seconds)")
    return FileResponse(
        os.path.join(REPLY_DIR, "reply.wav"),
        media_type="audio/wav",
        filename="processed.wav"
    )