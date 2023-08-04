import json
from controllers.users.users_model import User
from controllers.rooms.rooms_model import Room

def load_users_data():
    valid_users_data = []

    try:
        with open("assets/users.json", "r", encoding="utf-8") as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = []

    for user in users_data:
        try:
            valid_user = User(
                id=user["id"],
                name=user["name"],
                age=user["age"],
                gender=user["gender"],
                phone=user["phone"],
                address=user["address"]
            )
            valid_users_data.append(valid_user)
        except:
            pass

    return valid_users_data

def save_users_data(data):
    users_data = []
    for user in data:
        users_data.append({
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "gender": user.gender,
            "phone": user.phone,
            "address": user.address
        })

    with open("assets/users.json", "w", encoding="utf-8") as file:
        json.dump(users_data, file, indent=4)


def load_rooms_data():
    valid_rooms_data = []

    try:
        with open("assets/rooms.json", "r", encoding="utf-8") as file:
            rooms_data = json.load(file)
    except FileNotFoundError:
        rooms_data = []

    for room in rooms_data:
        try:
            valid_room = Room(
                id=room["id"],
                name_class=room["name_class"],
                number_class=room["number_class"]
            )
            valid_rooms_data.append(valid_room)
        except:
            pass

    return valid_rooms_data


def save_rooms_data(data):
    rooms_data = []
    for room in data:
        rooms_data.append({
            "id": room.id,
            "name_class": room.name_class,
            "number_class": room.number_class
        })

    with open("assets/rooms.json", "w", encoding="utf-8") as file:
        json.dump(rooms_data, file, indent=4)