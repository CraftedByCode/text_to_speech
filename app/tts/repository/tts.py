import os
from gtts import gTTS as t2t
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from starlette import status

 
def text_to_speech(dialogue:str,language:str = 'en'):
    try:
        text = t2t(dialogue,lang=language)
        output_path = 'tts/output'
        if os.path.exists:
            text.save(f"{output_path}/output.mp3")
        else:
            os.mkdir(output_path)
            text.save(f"{output_path}/output.mp3")
        
        return {
            "Audio file 🎼 is generated!"    
        }
    except Exception as e:
        return {"issue":str(e)}
    
def retrive_audio():
    output_file = 'tts/output/output.mp3'
    if os.path.isfile(output_file):
        return FileResponse(output_file, media_type="audio/mpeg")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    