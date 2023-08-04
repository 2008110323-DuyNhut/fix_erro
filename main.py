from fastapi import FastAPI
from controllers.users.users_controller import users_controller 

app = FastAPI()

app.include_router(users_controller)
