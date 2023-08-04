from pydantic import BaseModel

class Room(BaseModel):
    id: int
    name_class: str
    number_class: int