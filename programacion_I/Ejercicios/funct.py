import json

def down_json(path:str)->list:
    with open(path, "r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["paulina"]


