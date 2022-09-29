from func import export_csv
from func import buscar_inteligencia
from func import filtrar_promedio
from func import calcular_promedio
from func import menu_heroes
#from func import search_min_max
from func import heroes_sort
from func import mostrar_heroe_altura
from func import mostrar_heroe_fuerza
from func import mostrar_heroe
from func import cargar_json
'''
1- Listar los primeros N héroes. El valor de N será ingresado por el usuario 
(Validar que no supere max. de lista)

2- Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente
(‘asc’) o descendente (‘desc’)

3- Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente
(‘asc’) o descendente (‘desc’)

4- Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o
no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’)
se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

5- Buscar y Listar héroes por inteligencia [good, average, high] y listar en consola los que cumplan
dicha búsqueda.

6- Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por 
consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original
'''


lista_heroes = cargar_json("C:/Users/R5/Desktop/UTN/Programacion_I/Clase_10/data_stark.json")

#mostrar_heroe(lista_heroes)

menu_heroes()


data = lista_heroes.copy()


while True:
    respuesta = int(input("Seleccione una opción: "))
    if type(respuesta) != int:
        respuesta = int(input("Error, seleccione una opción correcta: "))
    if respuesta == 1: #Listar los primeros N héroes.
        n = int(input("Seleccione la cantidad de heroes a mostrar: "))
        if n > len(lista_heroes):
            print("Error, usted quiere ver mas heroes de los que contiene la lista.")
        else:
            data = mostrar_heroe(lista_heroes[:n])
    elif respuesta == 2: #Ordenar y Listar héroes por altura.
        orden = input("Seleccione si quiere ver la lista de forma ascendente o descendente ('up' para descendente, 'down' para ascendente)")
        if orden == "up" or orden == "down":
            data = mostrar_heroe_altura(heroes_sort(lista_heroes,"altura", orden))
        else:
            print("Error, reingrese una opcion correcta.")
    elif respuesta == 3: #Ordenar y Listar héroes por fuerza.
        orden = input("Seleccione si quiere ver la lista de forma ascendente o descendente ('up' para descendente, 'down' para ascendente)")
        if orden == "up" or orden == "down":
            data = mostrar_heroe_fuerza(heroes_sort(lista_heroes,"fuerza", orden))
        else:
            print("Error, reingrese una opcion correcta.")
    elif respuesta == 4: #4- Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio
        clave = input("Elija una clave numérica: (Altura, peso o fuerza)").lower()
        if clave != "altura" and clave != "peso" and clave != "fuerza":
            print("Error, ingresó un dato no válido.")
            clave = input("Elija una clave numérica: (Altura, peso o fuerza)").lower()
        orden = input("Seleccione si quiere ver quienes estan por encima del promedio ('mayor'),"
                      " o quienes estan por debajo del promedio ('menor')").lower()
        if orden != "mayor" and orden != "menor":
            print("Error, ingresó un dato no válido.")
            orden = input("Seleccione si quiere ver quienes estan por encima del promedio ('mayor'),"
                          " o quienes estan por debajo del promedio ('menor')").lower()
        lista_rta = filtrar_promedio(lista_heroes,clave,orden)
        print("El promedio de" ,clave, " es de:" , calcular_promedio(lista_heroes,clave) ,
              "\nQuienes cumplen con la condición", orden , "son:" ,lista_rta)
        data = lista_rta
    elif respuesta == 5:
        seguir = "si"
        while seguir == "si":
            clave = input("Seleccione el nivel de inteligencia que desea ver: (good, average, high)").lower()
            if clave != "good" and clave != "average" and clave != "high":
                print("Error, ingresó un dato no válido.")
            buscar_inteligencia(lista_heroes,clave)
            seguir = input("¿Desea seguir viendo datos? Si/No\n>").lower()
            if seguir != "si" and seguir == "no":
                print("Usted ingresó 'No' o una respuesta inválida, se lo devolverá al menú.")
        data = buscar_inteligencia(lista_heroes,clave)
        
    elif respuesta == 6:
        export_csv(data,"Clase_10/data_stark.csv")
    elif respuesta == 7:
        break

