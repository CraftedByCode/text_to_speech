import os
from pathlib import Path
from gtts import gTTS as t2t
from fastapi.exceptions import HTTPException
from fastapi import File, UploadFile
import shutil
from fastapi.responses import FileResponse
from starlette import status
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource
    )

DEEPGRAM_API_KEY = "3d86741a4e4fb7846e6eaf073eef52c9f4c560a3"



def upload_text(dialogue, language):
    return text_to_speech(dialogue=dialogue, language=language)

def upload_speech(audio: UploadFile = File(...)):
    return speech_to_text(audio=audio)

def speech_to_text(audio: UploadFile):
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        
        audio_path = Path("speech_technology/audio/output.wav")
        
        with audio_path.open("wb") as buffer:
            shutil.copyfileobj(audio.file,buffer)
        
        with open(audio_path, "rb") as file:
            buffer_data = file.read()
            
        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            language="en",
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        return {
            "transcript": transcript
        }
    
    except Exception as e:
        print(f"Exception: {e}")

def text_to_speech(dialogue: str, language: str = "en"):
    try:
        text = t2t(dialogue, lang=language)
        output_path = "/tmp"
        if os.path.exists(output_path):
            text.save(f"{output_path}/output.mp3")
        else:
            os.makedirs(output_path, exist_ok=True)
            text.save(f"{output_path}/output.mp3")

        return {"Audio file 🎼 Generated!"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"issue": str(e)}
        )


def retrive_audio():
    output_file = "/tmp/output.mp3"
    if os.path.isfile(output_file):
        return FileResponse(output_file, media_type="audio/mpeg")
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
