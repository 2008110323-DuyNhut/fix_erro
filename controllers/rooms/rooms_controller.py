from fastapi import  APIRouter, HTTPException, Body
from typing import List
from services.json_service import load_rooms_data, save_rooms_data
from controllers.rooms.rooms_model import Room
from controllers.rooms.rooms_dto import RoomUpdate, RoomCreate
rooms_controller = APIRouter()


@rooms_controller.get("/")
def read_root():
    return {" Chúc bạn một ngày vui"}

# Get information of all rooms
@rooms_controller.get("/rooms/", response_model=List[Room])
async def get_rooms():
    rooms_data = load_rooms_data()
    return rooms_data

# Get information about a room by id
@rooms_controller.get("/rooms/{room_id}", response_model=Room)
async def get_room(room_id: int):
    rooms_data = load_rooms_data()
    for room in rooms_data:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=404, detail="Room not found")

# Post information about a room by id
@rooms_controller.post("/rooms/", response_model=Room)
async def add_room(room: RoomCreate = Body(...)):
    rooms_data = load_rooms_data()
    new_room = {"id": len(rooms_data) + 1, **room}
    rooms_data.append(new_room)
    save_rooms_data(rooms_data)
    return new_room

# Put information about a room by id
@rooms_controller.put("/rooms/{room_id}", response_model=Room)
async def update_room(room_id: int, room: RoomUpdate = Body(...)):
    rooms_data = load_rooms_data()
    for existing_room in rooms_data:
        if existing_room["id"] == room_id:
            existing_room.update(room)
            save_rooms_data(rooms_data)
            return existing_room
    raise HTTPException(status_code=404, detail="Room not found")

# Delete information about a room by id
@rooms_controller.delete("/rooms/{room_id}", response_model=Room)
async def delete_room(room_id: int):
    rooms_data = load_rooms_data()
    for index, existing_room in enumerate(rooms_data):
        if existing_room["id"] == room_id:
            deleted_room = rooms_data.pop(index)
            save_rooms_data(rooms_data)
            return deleted_room
    raise HTTPException(status_code=404, detail="Room not found")
