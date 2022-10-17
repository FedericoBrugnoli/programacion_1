import json
import re

from soupsieve import match

def cargar_json(path:str)->list:
    '''
    abre un archivo json en modo lectura

    guarda los datos dentro de un diccionario

    retorna el diccionario

    '''
    with open(path,"r") as file:
        buffer_dict = json.load(file)

    return buffer_dict["heroes"]

#print(cargar_json("C:/Users/R5/Desktop/UTN/Programacion_I/Clase_10/data_stark.json"))

def menu_heroes():
    '''funcion que imprime las opciones a elegir en el menu'''
    print("\n1- Listar los primeros N héroes."
          "\n2- Ordenar y Listar héroes por altura."
          "\n3- Ordenar y Listar héroes por fuerza."
          "\n4- Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio."
          "\n5- Buscar y Listar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda."
          "\n6- Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]"
          "\n7 - Salir")
'''
def validar_rta()-> int:
    respuesta = int(input("\nSeleccione una opción: "))
    if type(respuesta) != int:
        respuesta = int(input("Error, seleccione una opción correcta: "))

    return respuesta
'''
def mostrar_heroe(lista:list):
    '''
    valida que la lista no esté vacía, en ese caso imprime un mensaje de error.

    en caso de que no, la recorre e imprime por consola el heroe y su identidad.

    '''
    lista_rta=[]
    if len(lista) < 0:
        print("Error, la lista está vacía")
    else:
        for element in lista:
            lista_rta.append(lista)
            #print("Heroe: {0} - Nombre: {1}".format(element["nombre"], element["identidad"]))

    return lista_rta
    


def mostrar_heroe_altura(lista:list):
    '''
    valida que la lista no esté vacía, en ese caso imprime un mensaje de error.

    en caso de que no, la recorre e imprime por consola el heroe, su altura.

    '''
    
    if len(lista) < 0:
        print("Error, la lista está vacía")
    else:
        for element in lista:
            print("Heroe: {0} - Altura: {1}".format(element["nombre"], element["altura"]))
   


def mostrar_heroe_fuerza(lista:list):
    '''
    valida que la lista no esté vacía, en ese caso imprime un mensaje de error.

    en caso de que no, la recorre e imprime por consola el heroe, su fuerza.

    '''
   
    if len(lista) < 0:
        print("Error, la lista está vacía")
    else:
        for element in lista:
            print("Heroe: {0} - Fuerza: {1}".format(element["nombre"], element["fuerza"]))

    

def search_min_max(lista:list, key:str, orden:str)->int:
    '''
    por defecto retorna -1.

    valida que la lista no este vacia.

    asigna el maximo y minimo de la lista a la primer posicion.

    recorre los indices de la lista.

    compara un elemento dentro de la lista siguiendo su indice y su key, en caso de que el orden este seleccionado descendente.

    compara que el actual sea menor, y si selecciona ascendente, compara el actual que sea mayor que el siguiente.
    '''
    mensaje = -1
    if len(lista) > 0:
        i_min_max = 0
        for i in range(len(lista)):
            if orden == "down" and lista[i][key] < lista[i_min_max][key] or orden == "up" and lista[i][key] > lista[i_min_max][key]:
                i_min_max = i
    mensaje = i_min_max
    return mensaje

def heroes_sort(lista:list, key:str, orden:str) -> list:
    '''
    creamos una nueva lista en la cual copiamos la lista a trabajar.

    recorremos los indices dentro de la longitud de la lista.

    con la funcion de searc_min_max, mas 1 indice, asignamos una etiqueta de indice minimo maximo.

    con esa lista copiada en el indice, y con esa lista en el indice minimo maximo, les reasignamos los valores.

    retornamos la lista ordenada.

    '''
    lista_sorted = lista.copy()
    for i in range(len(lista_sorted)):
        ind_min_max = search_min_max(lista_sorted[i:],key,orden) + i
        lista_sorted[i],lista_sorted[ind_min_max] = lista_sorted[ind_min_max],lista_sorted[i]
    return lista_sorted

def calcular_promedio(lista:list,key:str):
    '''
    defino un acumulador en 0 para agregar los valores de las keys a elegir
    
    valido que la lista sea mayor a 0, en caso que no, imprimo una alerta por consola
    
    recorro la lista
    
    valido que el contenido de la key sea de tipo numérico, en caso que sí, lo sumo al acumulador

    calculo el promedio diviendo el total del acumulador por la longitud de la lista y lo retorno
    '''
    acumulador_keys = 0
    if len(lista) > 0:
        for elemento in lista:
            if type(elemento[key]) == float or type(elemento[key]) == int:
                acumulador_keys = acumulador_keys + elemento[key]
            else:
                print("Error, ingresó un valor no numérico")
    else:
        print("Error, la lista está vacía")
    promedio = acumulador_keys/len(lista)
    return promedio
        
def filtrar_promedio(lista:list,key:str,orden:str) -> list:
    '''
    calculo el promedio
    
    designo dos lista vacías, una para los que sobrepasen el promedio, y otras para quienes estén por debajo del mismo
    
    defino el retorno en 0
    
    recorro la lista y comparo si el la clave del elemento es mayor a '''
    promedio = calcular_promedio(lista,key)
    lista_mayores = []
    lista_menores = []
    retorno = 0
    for elem in lista:
        if orden == "mayor" and elem[key] > promedio:
            lista_mayores.append(elem)
            retorno = lista_mayores
            #for elem in lista_mayores:
                #"Nombre: {0} -Atributo: {1}".format(elem["nombre"], elem[key])
        elif orden == "menor" and elem[key] < promedio:
            lista_menores.append(elem)
            retorno = lista_menores
            #for elem in lista_menores:
                #"Nombre: {0} -Atributo: {1}".format(elem["nombre"], elem[key])
    

    return retorno
    
def print_nombre_key(lista:list,key:str):
    for elem in lista:
        print('Nombre: {0} - {1}: {2}'.format(elem["nombre"],key,elem[key]))
    
def buscar_inteligencia(lista:list,clave:str):
    
    for elem in lista:
        match = re.search(clave,elem["inteligencia"],re.IGNORECASE)
        if match:
            inteligencia = elem["inteligencia"]
            palabra = "\033[0;31m" + match.group(0) + "\033[0;m"
            inteligencia = inteligencia.replace(match.group(0),palabra)
            print("{0} - {1}".format(elem["nombre"], inteligencia))

    
def export_csv(lista:list,path:str):
    #data = str(lista)
    with open (path,"w") as file:
        for elem in lista:
            file.write(f'{elem["nombre"]},{elem["identidad"]},{elem["altura"]},{elem["peso"]},{elem["fuerza"]},{elem["inteligencia"]}')

