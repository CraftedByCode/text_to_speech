from fastapi import APIRouter
from speech_technology.repository import common

router = APIRouter()

@router.get('/')
def home():
    return common.hello()

