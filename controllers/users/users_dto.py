from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str

class UserUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    phone: Optional[str]
    address: Optional[str]
