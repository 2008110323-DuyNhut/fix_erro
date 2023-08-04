import json
from controllers.users.users_model import User

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
