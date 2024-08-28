from sqlalchemy import Column, Integer
from text_to_speech.database import Base

class Abbreivation(Base):
    __tablename__ = "abbreivation"
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    
    