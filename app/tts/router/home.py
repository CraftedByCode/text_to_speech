from fastapi import APIRouter
from tts.repository import common

router = APIRouter()

@router.get('/')
def home():
    return common.hello()

