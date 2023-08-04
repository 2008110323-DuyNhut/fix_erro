from pydantic import BaseModel

class RoomCreate(BaseModel):
    name_class: str
    number_class: int

class RoomUpdate(BaseModel):
    name_class: str
    number_class: int