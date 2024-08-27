from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from text_to_speech.router.tts import router as tts
from text_to_speech.router.home import router as home

app = FastAPI()

app.include_router(home)
app.include_router(tts)

app.mount('/audio', StaticFiles(directory="text_to_speech/audio/"), name="audio")

    

