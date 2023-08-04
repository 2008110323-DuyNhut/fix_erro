from fastapi import APIRouter, HTTPException, Body
from typing import List
from controllers.users.users_model import User
from controllers.users.users_dto import UserCreate, UserUpdate
from services.json_service import load_users_data, save_users_data

users_controller = APIRouter()

@users_controller.get("/")
def read_root():
    return {"Hello anh Huy đẹp trai"} 

@users_controller.get("/users/", response_model=List[User])
async def get_users():
    users_data = load_users_data()  
    return users_data

@users_controller.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    users_data = load_users_data()
    for user in users_data:
        if user.id == user_id: 
            return user
    raise HTTPException(status_code=404, detail="User not found")

@users_controller.post("/users/", response_model=User)
async def add_user(user: UserCreate = Body(...)):
    users_data = load_users_data()  
    new_user = User(id=len(users_data) + 1, **user.dict())
    users_data.append(new_user)
    save_users_data(users_data)
    return new_user

@users_controller.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate = Body(...)):
    users_data = load_users_data() 
    for existing_user in users_data:
        if existing_user.id == user_id: 
            for field, value in user.dict(exclude_unset=True).items():
                if value is not None:
                    setattr(existing_user, field, value)  
            save_users_data(users_data)
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")

@users_controller.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    users_data = load_users_data()  
    for index, existing_user in enumerate(users_data):
        if existing_user.id == user_id: 
            deleted_user = users_data.pop(index)
            save_users_data(users_data)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")