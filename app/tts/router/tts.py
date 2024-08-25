from fastapi import APIRouter
from starlette import status
from tts.repository import tts
from tts import schemas

router = APIRouter()

@router.post('/convert',status_code=status.HTTP_201_CREATED,description=' Language-opt : ta, en, fr , pt, es')
def text_to_speech(request: schemas.TextData,):
    return tts.text_to_speech(request.dialogue,language=request.language)

@router.get('/retrive',status_code=status.HTTP_100_CONTINUE)
def retrive_audio():
    return tts.retrive_audio()