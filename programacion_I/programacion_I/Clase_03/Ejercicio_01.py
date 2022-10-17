from data_stark import lista_heroes

'''
{
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },

Analizar detenidamente el set de datos
-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
1-Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
2-Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
3-Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
4-Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
5-Calcular e informar cual es el superhéroe más y menos pesado.
-Ordenar el código implementando una función para cada uno de los valores informados.
Construir un menú que permita elegir qué dato obtener
'''
 
def imprimir_nombre_superheroe():
    for heroe in lista_heroes:
        print(heroe["nombre"])

def imprimir_nombre_altura_superheroe():
    for heroe in lista_heroes:
        print(heroe["nombre"],heroe["altura"])

acumulador_altura = 0

def calcular_mas_alto():
#-------------------Max altura--------------
    heroe_mas_alto = lista_heroes[0]["altura"]
    nombre_mas_alto = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        heroe_mas_alto_float = float(heroe_mas_alto)
        altura_float = float(heroe["altura"])
        if(altura_float > heroe_mas_alto_float):
            heroe_mas_alto = heroe["altura"]
            nombre_mas_alto = heroe["nombre"]

    print(nombre_mas_alto, heroe_mas_alto)

def calcular_mas_bajo():
#----------------Min altura--------------------
    heroe_mas_bajo = lista_heroes[0]["altura"]
    nombre_mas_bajo = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        heroe_mas_bajo_float = float(heroe_mas_bajo)
        altura_float = float(heroe["altura"])
        if(altura_float < heroe_mas_bajo_float):
            heroe_mas_bajo = heroe["altura"]
            nombre_mas_bajo = heroe["nombre"]

    print(nombre_mas_bajo, heroe_mas_bajo)

def calcular_promedio_altura():
#----------------Promedio-------------------
    for heroe in lista_heroes:
        altura_float = float(heroe["altura"])
        acumulador_altura = acumulador_altura + altura_float

    print("Promedio: ", acumulador_altura/len(lista_heroes))

def calcular_mas_pesado():
    #----------------max pesado-------------------
    heroe_mas_peso = lista_heroes[0]["peso"]
    nombre_mas_peso = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        heroe_mas_peso_float = float(heroe_mas_peso)
        peso_float = float(heroe["peso"])
        if(peso_float > heroe_mas_peso_float):
            heroe_mas_peso = heroe["peso"]
            nombre_mas_peso = heroe["nombre"]

    print(nombre_mas_peso, heroe_mas_peso)

def calcular_menos_pesado():
    #----------------min pesado-------------------
    heroe_menos_peso = lista_heroes[0]["peso"]
    nombre_menos_peso = lista_heroes[0]["nombre"]

    for heroe in lista_heroes:
        heroe_menos_peso_float = float(heroe_menos_peso)
        peso_float = float(heroe["peso"])
        if(peso_float < heroe_menos_peso_float):
            heroe_menos_peso = heroe["peso"]
            nombre_menos_peso = heroe["nombre"]

    print(nombre_menos_peso, heroe_menos_peso)

respuesta = int(input("1- Lista de superheroes con nombre y altura. \n 2- Superheroe mas alto \n 3- Superheroe mas bajo \n 4- Promedio altura \n 5- Superheroe mas y menos pesado \n 6- Salir"))

while True:
    if(respuesta == 1):
        imprimir_nombre_altura_superheroe()
    elif(respuesta == 2):
        calcular_mas_alto()
    elif(respuesta == 3):
        calcular_mas_bajo()
    elif(respuesta == 4):
        calcular_promedio_altura()
    elif(respuesta == 5):
        calcular_mas_pesado()
        calcular_menos_pesado()
    else:
        break

