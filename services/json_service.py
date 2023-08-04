import json
from controllers.rooms.rooms_model import Room

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