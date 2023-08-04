from fastapi import FastAPI
from controllers.users.users_controller import users_controller 
from controllers.rooms.rooms_controller import rooms_controller 

app = FastAPI()

app.include_router(users_controller)
app.include_router(rooms_controller)
