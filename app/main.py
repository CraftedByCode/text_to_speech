from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tts.router.tts import router as tts
from tts.router.home import router as home

app = FastAPI()

app.include_router(home)
app.include_router(tts)

app.mount('/audio', StaticFiles(directory="tts/audio/"), name="audio")

    

