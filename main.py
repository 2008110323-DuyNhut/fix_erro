from fastapi import FastAPI
from controllers.rooms.rooms_controller import rooms_controller 

app = FastAPI()

app.include_router(rooms_controller)

