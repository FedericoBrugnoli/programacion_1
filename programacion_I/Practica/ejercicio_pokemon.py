from data_pokemon import pokemones


'''# Nivel 1 - [En clase de repaso]
01 - Imprimir nombres de pokemones
02 - Imprimir pokemones que tenga un ID par
03 - Imprimir pokemones que tenga un ID múltiplo de 25
04 - Imprimir nombre de pokemones con su ID de prefijo.
05 - Imprimir los pokemones con más poder y cuánto poder tienen (misma fuerza)
06 - Imprimir los pokemones con menos poder y cuánto poder tienen (misma fuerza)

# Nivel 2 - [En clase de repaso]
07 - Imprimir el promedio de poder de pokemones que entre sus tipos tenga 'psíquico'
08 - Imprimir el promedio de poder de pokemones que entre sus tipos tenga 'fuego'
09 - Imprimir el promedio de poder de pokemones que entre sus tipos tenga 'eléctrico'

# Nivel 3 - [En clase de repaso]
10 - Imprimir pokemones que posean más de un tipo
11 - Imprimir pokemones que posean más de un tipo y su cantidad
12 - Imprimir pokemones que posean más de una evolución
13 - Imprimir pokemones que posean más de una evolución y su cantidad
14 - Imprimir pokemones que posean más de una fortaleza
15 - Imprimir pokemones que posean más de una fortaleza y su cantidad
16 - Imprimir pokemones que posean más de una debilidad
17 - Imprimir pokemones que posean más de una debilidad y su cantidad


        {
            "id": 1,
            "nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
            "poder": 4,
            "fortaleza":["agua"],
            "debilidad":["fuego"]
        }
'''



def imprimir_nombre_pokemones():
    '''
    recorre la lista de pokemones.
    guarda los nombres.
    imprime los nombres de los pokemones.
    '''
    for nombre_pokemon in pokemones:
        print(nombre_pokemon["nombre"])

def imprimir_nombre_pk_par():
    '''
    recorre la lista de pokemones.
    guarda los nombres de los pokemones con id par.
    imprime los nombres.
    '''
    for pokemon_par in pokemones:
        if(pokemon_par["id"]%2==0):
            print(pokemon_par["nombre"])

def imprimir_nombre_pk_multiplo():
    '''
    recorre la lista de pokemones.
    guarda los nombres de los pokemones multiplos de 25.
    imprime los nombres.
    '''
    for pokemon_multiplo in pokemones:
        if(pokemon_multiplo["id"]%25==0):
            print(pokemon_multiplo["nombre"])

def imprimir_pk_id():
    '''
    recorre la lista de pokemones.
    imprime los id y los nombres de los pokemones.
    '''
    for pokemon_id in pokemones:
        print(pokemon_id["id"],pokemon_id["nombre"])

def imprimir_pk_mas_poder():
    pokemon_mas_fuerte = pokemones[0]["poder"]
    nombre_pk_mas_fuerte = pokemones[0]["nombre"]
    '''
    recorre la lista de pokemones.
    guarda los que más poder tengan.
    imprime nombre y poder.
    '''
    for pokemon_fuerte in pokemones:
        if(pokemon_fuerte["poder"] > pokemon_mas_fuerte):
            pokemon_mas_fuerte = pokemones["poder"]
            nombre_pk_mas_fuerte = pokemones["nombre"]

            print(pokemon_mas_fuerte["poder"],nombre_pk_mas_fuerte["nombre"])

imprimir_pk_mas_poder()




