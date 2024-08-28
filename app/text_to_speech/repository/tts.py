import os
from gtts import gTTS as t2t
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from starlette import status

def upload_data(dialogue, language):
    return text_to_speech(dialogue=dialogue, language=language)


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
