from fastapi import APIRouter
from starlette import status
from text_to_speech.repository import tts
from text_to_speech import schemas

router = APIRouter()


@router.post("/convert",status_code=status.HTTP_201_CREATED)
def upload_data(request: schemas.TextData):
    return tts.upload_data(dialogue=request.dialogue, language=request.language)


@router.get("/retrive", status_code=status.HTTP_100_CONTINUE)
def retrive_audio():
    return tts.retrive_audio()
