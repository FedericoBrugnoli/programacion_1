import json
import re

def cargar_json(path:str) ->list:
    '''
    Abre el archivo json 'pokedex.json' en modo lectura.
    
    Guarda dicho archivo en un diccionario.

    Retorna el diccionario en la clave "pokemones".
    '''
    with open(path, "r") as file:
        buffer_dict = json.load(file)

    return buffer_dict["pokemones"]

def print_menu_poke():
    '''
    Imprime las opciones del menú.
    '''
    print("\n1- Listar los últimos N pokemones."
          "\n2- Ordenar y Listar pokemones por poder."
          "\n3- Ordenar y Listar pokemones por ID"
          "\n4- Calcular la cantidad promedio de las key tipo lista."
          "\n5- Buscar pokemones por tipo."
          "\n6- Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]."
          "\n7- Salir."
          "\n")

def validar_respuesta_input()-> int:
    '''
    Pide un dato al usuario.

    Valida que dicho número se encuentre dentro de las opciones dadas a elegir.

    En caso de no matchear, pide nuevamente un dato al usuario.

    En caso de sí, convierte dicho dato a entero y lo retorna.
    '''
    respuesta = input("Seleccione una opción: ")
    match = re.search('[1-7]',respuesta)
    if not match:
        respuesta = input("Error, seleccione una opción válida: ")
    else:
        rta = (int(respuesta))

    return rta

def mostrar_pk(lista:list,key:str):
    '''
    Recibe por parámetro una lista.


    Verifica que la lista recibida no esté vacía, en ese caso imprime un mensaje de error.

    En caso que no esté vacía, imprime los elementos formateados a Pokemón - "key", este último será un dato hardcodeado.
    '''
    if len(lista) < 0:
        print("Error, la lista está vacía")
    else:
        for elem in lista:
            if key == "id":
                print("Pokemón: {0} - ID: {1}".format(elem["nombre"],elem[key]))
            elif key == "poder":
                print("Pokemón: {0} - Poder: {1}".format(elem["nombre"],elem[key]))
            

    

def buscar_min_max(lista:list,key:str,orden:str) -> int:
    '''
    Recibe una lista, una key y un orden por parámetro.

    Por defecto retorna "-1"

    Valida que la lista sea mayor a 0, en caso que no imprime un mensaje de error.

    En caso que no esté vacía, asigna el primer indice a una variable.

    Recorre los indices según la longitud de la lista y compara el orden, en caso de ser descendiente compara
    el indice actual en tanto sea menor al indice asignado en la variable. Y en caso de ser ascendiente compara
    el indice actual en tanto sea mayor al indice asignado en la variable.

    Asigna a la variable el indice, y lo retorna.
    '''
    mensaje = -1
    if len(lista) > 0:
        i_min_max = 0
        for i in range(len(lista)):
            if orden == "asc" and lista[i][key] < lista[i_min_max][key] or orden == "desc" and lista[i][key] > lista[i_min_max][key]:
                i_min_max = i
    else:
        print("Error, la lista está vacía")
    mensaje = i_min_max
    return mensaje

def pk_sort(lista:list,key:str,orden:str) -> list:
    '''
    Recibe por parámetro una lista, una key y un orden.
    
    Crea una copia de la lista recibida.

    Recorre los indices según la longitud de la lista.

    Asigna a una variable el mínimo o máximo (definido por el parámetro "orden"), utilizando la función buscar_min_max,
    y le suma el indice.

    Asigna a la copia de la lista el indice, y también el indice min_max y lo iguala al indice min_max y al indice respectivamente.

    Retorna la copia de la lista, ordenada.
    '''
    lista_a_sortear = lista.copy()
    for i in range(len(lista_a_sortear)):
        i_min_max = buscar_min_max(lista_a_sortear[i:],key,orden) + i
        lista_a_sortear[i],lista_a_sortear[i_min_max] = lista_a_sortear[i_min_max],lista_a_sortear[i]
    
    return lista_a_sortear

def calcular_promedio(lista:list[dict],key):
    ac_keys = 0
    sum_key = 0
    if len(lista) > 0:
        for elem in lista:
            for elemen in elem.values():
                print(elemen)
                

        
        #print(ac_keys,sum_key)
        #promedio = sum_key/ac_keys
    
    #print(int(promedio))

def buscar_tipo(lista:list,key:str):
    for elem in lista:
        for elemen in elem:
            match = re.search(key,elemen["tipo"],re.IGNORECASE)
            if match:
                tipo = elem["tipo"]
                palabra = "\033[0;31m" + match.group(0) + "\033[0;m"
                tipo = tipo.replace(match.group(0),palabra)
                print("{0} - {1}".format(elem["nombre"], tipo))

def export_csv(lista:list,path:str):
    with open (path,"w") as file:
        for elem in lista:
            file.write(lista)