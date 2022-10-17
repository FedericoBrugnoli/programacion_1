
import func_pk as f
'''
1- Listar los últimos N pokemones. El valor de N será ingresado por el usuario  (Validar que no supere max. de
lista)


2- Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o
descendente (‘desc’)


3- Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o
descendente (‘desc’)


4- Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo), Preguntar qué
promedio quiere calcular este esas posibles keys y filtrar los que cumplan con la condición de superar o no
el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que
cumplan con tener mayores o menores cantidades en la lista de dicha key según corresponda.


5- Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer, muchos de ellos poseen
más de un tipo, con lo cual habrá que darle a elegir al usuario entre todos los tipos que existen en el json)
una vez seleccionado listar en consola los que posean dicho tipo. (Usando RegEx para la búsqueda).
Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, deberá
listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).


6- Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]



Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola
con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original
'''

lista_poke = f.cargar_json("C:/Users/R5/Desktop/UTN/Programacion_I/Practica_02/pokedex.json")

pokes = lista_poke.copy()
print(pokes)
f.print_menu_poke()
while True:
    lista_for_csv = []
    respuesta = f.validar_respuesta_input()
    if respuesta == 1:
        n = int(input("Seleccione desde qué pokemon quiere ver: "))
        if n > len(pokes):
            print("Error, quiere ver más pokemones de los que contiene la lista.")
        else:
            info_for_csv = f.mostrar_pk(pokes[n:],"id")
            lista_for_csv.append(info_for_csv)
    elif respuesta == 2:
        orden = input("Seleccione si quiere ordenar la lista de manera ascendente('asc') o descendente('desc'):").lower()
        if orden == "asc" or orden == "desc":
            f.buscar_min_max(pokes,"poder",orden)
            lista_ord = f.pk_sort(pokes,"poder",orden)
            f.mostrar_pk(lista_ord,"poder")
            info_for_csv = lista_ord
            lista_for_csv.append(info_for_csv)
        else:
            print("Error, reingrese una opción válida.")
    elif respuesta == 3:
        orden = input("Seleccione si quiere ordenar la lista de manera ascendente('asc') o descendente('desc'):").lower()
        if orden == "asc" or orden == "desc":
            #f.buscar_min_max(pokes,"id",orden)
            lista_ord = f.pk_sort(pokes,"id",orden)
            f.mostrar_pk(lista_ord,"id")
            info_for_csv = lista_ord
            lista_for_csv.append(info_for_csv)
        else:
            print("Error, reingrese una opción válida.")
    elif respuesta == 4:
        clave = input("Seleccione la clave a promediar: (evoluciones, fortaleza, debilidad, tipo)").lower()
        if clave == "evoluciones" or clave == "fortaleza" or clave == "debilidad" or clave == "tipo":
            f.calcular_promedio(pokes,clave)
        else:
            print("Error, ingresó un dato incorrecto.")
    elif respuesta == 5:
        seguir = "si"
        while seguir == "si":
            clave = input("\nSeleccione el tipo de pokemón que desea buscar:"
                          "[planta, fuego, volador, agua, electrico, fantasma, veneno,"
                          " hielo, psiquico, lucha o acero.]\n").lower()
            if clave != "planta" or clave != "fuego" or clave != "volador" or clave != "agua" or clave != "electrico" or clave != "fantasma" or clave != "veneno" or clave != "hielo" or clave != "psiquico" or clave != "lucha" or clave != "acero":
                print("\nError, ingresó un tipo no válido.\n")
            f.buscar_tipo(pokes,clave)
            seguir = input("\n¿Desea seguir buscando? 'si/no'\n").lower()
            if seguir != "si":
                print("\nIngresó 'no' o un dato incorrecto, por lo que se le devolverá al menu.\n")
                break
    elif respuesta == 6:
        f.export_csv(lista_for_csv,"Practica_02/pokedex.csv")
    elif respuesta == 7:
        break