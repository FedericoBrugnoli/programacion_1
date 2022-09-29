from multiprocessing import Value
from os import lseek
from data_stark import lista_heroes
def definir_lista_femenino():
    '''
    recorre la lista de heroes
    
    compara los géneros, coincidiendo con los femeninos
    
    guarda los diccionarios de los femeninos en una nueva lista
    '''
    lista_heroes_f = []
    for heroe_f in lista_heroes:
        if(heroe_f["genero"] == "F"):
            lista_heroes_f.append(heroe_f)

    return lista_heroes_f
        
def definir_lista_masculinos():
    '''
    recorre la lista de heroes
    
    compara los géneros, coincidiendo con los masculinos
    
    guarda los diccionarios de los masculinos en una nueva lista
    '''
    lista_heroes_m = []
    for heroe_m in lista_heroes:
        if(heroe_m["genero"] == "M"):
            lista_heroes_m.append(heroe_m)

    return lista_heroes_m
        
lista_heroes_masc = definir_lista_masculinos()
lista_heroes_feme = definir_lista_femenino()

def imprimir_nombres(lista_nombres):
    for heroe in lista_nombres:
        print(heroe["nombre"])

def calcula_imprime_mas_alto(lista_de_heroes):
    '''
    recorre la lista de heroes
    
    compara las alturas hasta encontrar el maximo

    guarda el más alto, junto con el nombre y los imprime
    '''
#-------------------Max altura --------------
    heroe_mas_alto = lista_de_heroes[0]["altura"]
    nombre_mas_alto = lista_de_heroes[0]["nombre"]

    for heroe in lista_de_heroes:
        heroe_mas_alto_float = float(heroe_mas_alto)
        altura_float = float(heroe["altura"])
        if(altura_float > heroe_mas_alto_float):
            heroe_mas_alto = heroe["altura"]
            nombre_mas_alto = heroe["nombre"]

    print(nombre_mas_alto, heroe_mas_alto)



def calcula_imprime_mas_bajo(lista_de_heroes):
    '''
    recorre la lista de heroes
    
    compara las alturas hasta encontrar el minimo

    guarda el más bajo, junto con el nombre y los imprime
    '''
    #----------------Min altura--------------------
    heroe_mas_bajo = lista_de_heroes[0]["altura"]
    nombre_mas_bajo = lista_de_heroes[0]["nombre"]

    for heroe in lista_de_heroes:
        heroe_mas_bajo_float = float(heroe_mas_bajo)
        altura_float = float(heroe["altura"])
        if(altura_float < heroe_mas_bajo_float):
            heroe_mas_bajo = heroe["altura"]
            nombre_mas_bajo = heroe["nombre"]

    print(nombre_mas_bajo, heroe_mas_bajo)
'''
def calcula_imprime_mas_bajo(lista_de_heroes):
#----------------Min altura--------------------
    heroe_mas_bajo = lista_de_heroes[0]["altura"]
    nombre_mas_bajo = lista_de_heroes[0]["nombre"]

    for heroe in lista_de_heroes:
        heroe_mas_bajo_float = float(heroe_mas_bajo)
        altura_float = float(heroe["altura"])
        if(altura_float < heroe_mas_bajo_float):
            heroe_mas_bajo = heroe["altura"]
            nombre_mas_bajo = heroe["nombre"]

    print(nombre_mas_bajo, heroe_mas_bajo)
'''

def calcular_promedio_altura(lista_de_heroes):
    '''
    recorre la lista de heroes
    
    accede al valor de la key altura, pasándolo a un float para poder sumarlos
    
    acumula las alturas y las divide por la longitud de la lista, calculando así el promedio de altura
    '''
    acumulador_altura = 0
    
#----------------Promedio-------------------
    for heroe in lista_de_heroes:
        altura_float = float(heroe["altura"])
        acumulador_altura = acumulador_altura + altura_float
        
    print("Promedio: ", acumulador_altura/len(lista_de_heroes))

#J-Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def determinar_cant_ojos():
    '''
    declara una lista vacía, recorre la lista de heroes y guarda en esa lista vacía los colores de ojos
    
    los guarda en un set para no tenerlos repetidos
    
    declara una segunda lista vacía, recorre el set y crea un diccionario donde guarda el color y la cantidad de veces
    que aparece
    
    recorre la lista de heroes, aumentando la cantidad de veces por color de ojos, incrementando la cantidad en el 
    diccionario
    
    agrega el diccionario en la segunda lista y la retorna'''
    lista_color_ojos = []
    for heroe in lista_heroes:
        lista_color_ojos.append(heroe["color_ojos"])

    set_ojos = set(lista_color_ojos)
    #print(set_ojos)

    lista_de_ojos = []
    for color_ojos in set_ojos:
        dic_color_ojos = {"Color":color_ojos, "Cantidad": 0}
        for heroe in lista_heroes:
            if(heroe["color_ojos"] == color_ojos):
                dic_color_ojos["Cantidad"]+=1

        lista_de_ojos.append(dic_color_ojos)

    return lista_de_ojos

#K- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def determinar_cant_pelos():
    '''
    declara una lista vacía, recorre la lista de heroes y guarda en esa lista vacía los colores de pelos
    
    los guarda en un set para no tenerlos repetidos
    
    declara una segunda lista vacía, recorre el set y crea un diccionario donde guarda el color y la cantidad de veces
    que aparece
    
    recorre la lista de heroes, aumentando la cantidad de veces por color de pelos, incrementando la cantidad en el 
    diccionario
    
    agrega el diccionario en la segunda lista y la retorna'''
    lista_color_pelo = []
    for heroe in lista_heroes:
        lista_color_pelo.append(heroe["color_pelo"])

    set_pelo = set(lista_color_pelo)
    #print(set_pelo)

    lista_de_pelos = []
    for color_pelo in set_pelo:
        dic_color_pelo = {"Color":color_pelo, "Cantidad": 0}
        for heroe in lista_heroes:
            if(heroe["color_pelo"] == color_pelo):
                dic_color_pelo["Cantidad"]+=1

        lista_de_pelos.append(dic_color_pelo)

    return lista_de_pelos

#L- Determinar cuántos superhéroes tienen cada tipo de inteligencia
#(En caso de no tener, Inicializarlo con ‘No Tiene’). 
def determinar_cant_inteligencias():
    '''
    declara una lista vacía, recorre la lista de heroes y guarda en esa lista vacía la inteligencia
    
    los guarda en un set para no tenerlos repetidos
    
    declara una segunda lista vacía, recorre el set y crea un diccionario donde guarda la inteligencia y 
    la cantidad de veces que aparece
    
    recorre la lista de heroes, aumentando la cantidad de veces por nivel de inteligencia,
    incrementando la cantidad en el diccionario
    
    agrega el diccionario en la segunda lista
    
    en caso de que el heroe no posea un nivel de inteligencia, se le asignará un "No tiene"
    
    retorna la segunda lista y el "No tiene" en caso de ser así'''
    lista_inteligencia = []
    for heroe in lista_heroes:
        lista_inteligencia.append(heroe["inteligencia"])

    set_inteligencia = set(lista_inteligencia)
    #print(set_pelo)

    lista_de_inteligencias = []
    for nivel_inteligencia in set_inteligencia:
        dic_inteligencias = {"Nivel":nivel_inteligencia, "Cantidad": 0}
        for heroe in lista_heroes:
            if(heroe["inteligencia"] == nivel_inteligencia):
                dic_inteligencias["Cantidad"]+=1
                

        lista_de_inteligencias.append(dic_inteligencias)

    for smart in lista_de_inteligencias:
        if(smart["Nivel"] == ""):
            smart["Nivel"] = "No tiene"


    return lista_de_inteligencias, smart

'''
lista_colores_ojos = determinar_cant_ojos()
lista_colores_pelos = determinar_cant_pelos()
lista_smarts = determinar_cant_inteligencias()
'''

#M- Listar todos los superhéroes agrupados por color de ojos.
def imprimir_y_agrupar_colores_ojos():   
    '''
    crea una lista vacía

    recorre la lista de heroes y guarda los colores de ojos en esa lista vacía

    los guarda en un set para no repetirlos

    declara una segunda lista vacía, recorre el set y dentro del mismo declara una tercer lista y un diccionario donde
    guardara los colores de ojos y los nombres con esta ultima lista

    recorre la lista de heroes y compara el color de ojos, si ya aparece en el diccionario, agrega los nombres a la 
    lista dentro del mismo

    agrega el diccionario en la segunda lista y la imprime
    '''
    lista_colores = []
    for heroe in lista_heroes:
        lista_colores.append(heroe["color_ojos"])# busco colores ojos y los guardo 
    
    set_colores_ojos = set(lista_colores)
    #print(set_colores_ojos)

    lista_nombres_colores = []
    for colores_ojos in set_colores_ojos:
        lista_nombres = []
        
        dic_colores_nombres = {"color ojo": colores_ojos, "nombres": lista_nombres}
        for heroe in lista_heroes:
            if(heroe["color_ojos"] == colores_ojos):#los comparo en un if ,
                lista_nombres.append(heroe["nombre"])#y si tienen el mismo color de ojos, guardo los nombres en una lista

        lista_nombres_colores.append(dic_colores_nombres)

    print(lista_nombres_colores)

#N- Listar todos los superhéroes agrupados por color de pelo.
def imprimir_y_agrupar_colores_pelo():   
    '''
    crea una lista vacía

    recorre la lista de heroes y guarda los colores de pelo en esa lista vacía

    los guarda en un set para no repetirlos

    declara una segunda lista vacía, recorre el set y dentro del mismo declara una tercer lista y un diccionario donde
    guardara los colores de pelo y los nombres con esta ultima lista

    recorre la lista de heroes y compara el color de pelo, si ya aparece en el diccionario, agrega los nombres a la 
    lista dentro del mismo

    agrega el diccionario en la segunda lista y la imprime
    '''
    lista_colores = []
    for heroe in lista_heroes:
        lista_colores.append(heroe["color_pelo"])
    
    set_colores_pelo = set(lista_colores)
    #print(set_colores_pelo)

    lista_nombres_colores = []
    for colores_pelo in set_colores_pelo:
        lista_nombres = []
        
        dic_colores_nombres = {"color pelo": colores_pelo, "nombres": lista_nombres}
        for heroe in lista_heroes:
            
            if(heroe["color_pelo"] == colores_pelo):
                lista_nombres.append(heroe["nombre"])

        lista_nombres_colores.append(dic_colores_nombres)

    print(lista_nombres_colores)

#O- Listar todos los superhéroes agrupados por tipo de inteligencia
def imprimir_y_agrupar_inteligencias():
    '''
    crea una lista vacía

    recorre la lista de heroes y guarda la inteligencia en esa lista vacía

    las guarda en un set para no repetirlas

    declara una segunda lista vacía, recorre el set y dentro del mismo declara una tercer lista y un diccionario donde
    guardara la inteligencia y los nombres con esta ultima lista

    recorre la lista de heroes y compara la inteligencia, si ya aparece en el diccionario, agrega los nombres a la 
    lista dentro del mismo

    agrega el diccionario en la segunda lista y la imprime
    '''
    lista_inteligencias = []
    for heroe in lista_heroes:
        lista_inteligencias.append(heroe["inteligencia"])
    
    set_inteligencias = set(lista_inteligencias)
    #print(set_inteligencias)

    lista_nombres_inteligencias = []
    for inteligencias in set_inteligencias:
        lista_nombres = []
        dic_inteligencias_nombres = {"inteligencia": inteligencias, "nombres": lista_nombres}
        for heroe in lista_heroes:
            if(heroe["inteligencia"] == inteligencias):
                lista_nombres.append(heroe["nombre"])
                

        lista_nombres_inteligencias.append(dic_inteligencias_nombres)

    print(lista_nombres_inteligencias)

def stark_normalizar_datos(lista:list):
    contador = 0
    if(len(lista_heroes)>0):
        for heroe in lista:
            if(type(heroe["altura"]) != type(float())):
                heroe["altura"] = float(heroe["altura"])
                contador+=1
            if(type(heroe["peso"]) != type(float())): 
                heroe["peso"] = float(heroe["peso"])
                contador+=1
            if(type(heroe["fuerza"]) != type(int())): 
                heroe["fuerza"] = int(heroe["fuerza"])
                contador+=1
            if(contador>0):
                print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía")
    
def obtener_nombre(heroe:dict) -> str:
    '''
    recorre la lista de heroes
    
    retorna nombre formateado a "Nombre:" nombre_del_heroe'''
    lista_nombres = []
    for heroe in lista_heroes:
        lista_nombres.append(heroe["nombre"])
        for nombre in lista_nombres:
            nombre = lista_nombres
            
    #return "Nombre:", nombre



def imprimir_dato(key:str):
    lista_data = []
    for heroes in lista_heroes:
        lista_data.append(heroes[key])
    return lista_data
    
'''1.3 Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá
imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía
para realizar sus acciones, caso contrario no hará nada y retornara -1.
Con este se resuelve el Ej 1 del desafío #00'''
def stark_imprimir_nombres_heroes(lista_heroes):
    nombre = obtener_nombre(lista_heroes)
    print(nombre)

def obtener_nombre_y_dato(heroe:dict, key:str) -> str:
    dato = imprimir_dato(key)
    for heroe in lista_heroes:
        nombre = heroe["nombre"]
    return "Nombre:", nombre, "|", key+":", dato

def stark_imprimir_nombres_alturas(lista:list):
    nombre = obtener_nombre(lista_heroes)
    alturas = imprimir_dato("altura")
    for heroe in lista_heroes:
        if(len(lista_heroes)>0):
            print(nombre, alturas)
        else:
            return "-1"

'''
while True:#Menu
    respuesta = input("Seleccione la opción: ")
    if(respuesta == "1"):
        stark_imprimir_nombres_heroes(lista_heroes)

'''   


