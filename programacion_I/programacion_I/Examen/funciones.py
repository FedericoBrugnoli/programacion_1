import json
import re

def cargar_json(path:str):
    with open(path,"r") as file:
        file = json.load(file)
    return file["results"]

def mostrar(lista:list,key:str)->list:
    lista_mostrar = []
    if len(lista) > 0:
        for elem in lista:
            lista_mostrar.append(lista)
            mensaje = ()
    return mensaje

lambda a,b : a+b