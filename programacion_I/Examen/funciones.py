import json
import re

def cargar_json(path:str):
    with open(path,"r") as file:
        file = json.load(file)
    return file

