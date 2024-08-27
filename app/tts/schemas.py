from pydantic import BaseModel

class TextData(BaseModel):
    dialogue:str
    language:str
  
    