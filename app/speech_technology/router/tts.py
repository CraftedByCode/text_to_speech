from fastapi import APIRouter, File, UploadFile
from starlette import status
from speech_technology.repository import tts
from speech_technology import schemas

router = APIRouter(
    tags=["Speech Processing"]
)

@router.post("/text",status_code=status.HTTP_201_CREATED)
def upload_text(request: schemas.TextData):
    return tts.upload_text(dialogue=request.dialogue, language=request.language)

@router.post('/speech')
def upload_speech(audio: UploadFile = File(...)):
    return tts.upload_speech(audio=audio)

@router.get("/retrive", status_code=status.HTTP_100_CONTINUE)
def retrive_audio():
    return tts.retrive_audio()
