# schemas.py - Pydantic models for validation


# Pydantic BaseModel will take care of the constructor

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
    married: bool


class User(BaseModel):  
    id: int
    name: str
    age: int
    married: bool