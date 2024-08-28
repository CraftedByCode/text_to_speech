from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from speech_technology.router.tts import router as tts
from speech_technology.router.home import router as home

app = FastAPI()

app.include_router(home)
app.include_router(tts)

from fastapi.middleware.cors import CORSMiddleware