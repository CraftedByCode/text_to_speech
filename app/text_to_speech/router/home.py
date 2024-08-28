from fastapi import APIRouter
from app.text_to_speech.repository import common

router = APIRouter()

@router.get('/')
def home():
    return common.hello()

