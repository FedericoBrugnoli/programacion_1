from random import randint
from functools import reduce

from sklearn.utils import shuffle

lista_palabras = [
    "Goku", "Vegeta", "Frieza", "Cell", "Beerus", 'Krillin'
]

# Refactoprizar la funcion clasica usando lambda
def sup_triangulo(base: int, altura: int) -> float:
    return (base*altura)/2


#l = [12,43]
sup = lambda x,y:x*y/2
print("0-",sup)

# Refactorizar la funcion clasica usando lambda y map
def aplicar_mayusculas(lista_palabras: list) -> list:
    for i in range(len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].upper()
    return lista_palabras

mayus = list(map(lambda str:str.upper(),lista_palabras))
print("1-",mayus)


# Refactorizar la funcion usando lambda y reduce
def obtener_mas_letras(lista: list) -> str:
    seleccionado = ''
    for palabra in lista:
        if len(palabra) > len(seleccionado):
            seleccionado = palabra
    return seleccionado

mas_let = reduce(lambda x,y: y if len(y)>len(x) else x , lista_palabras)
print("2-",mas_let)

# refactorizar la funcion usando lambda y filter
def obtener_nombres_cantidad_letras(lista: list, cantidad: int) -> list:
    return list(filter(lambda el : el if len(el) == cantidad else '', lista))

#cantnomb = list(filter(lambda x,y: list(x) if len(x) == int(y) else list(y) ,lista_palabras ))
cant = int(input("3- ingrese un num"))
print("3-",obtener_nombres_cantidad_letras(lista_palabras,cant))


# refactorizar usando shuffle
def ordenar_random_lista(lista: list) -> list:
    maximo = len(lista)
    desordenada = list()
    while len(desordenada) < len(lista):
        indice = randint(0, maximo)
        for elemento in lista:
            desordenada.insert(indice, elemento)
    return desordenada

shflrndm = shuffle(lista_palabras) 
print("4-",shflrndm)

# Refactorizar usando sort y lamda
def ordenar_burbujeo(lista: list) -> list:
    lista_copia = lista.copy()
    for i in range(len(lista_copia)-1):
        for j in range(i+1, len(lista_copia)):
            if lista_copia[i] > lista_copia[j]:
                lista_copia[i], lista_copia[j] = lista_copia[j], lista_copia[i]
    return lista_copia

#sortbbl = lista_palabras.sort(lambda key:key=len,lista_palabras)




heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]

# Refactorizar usando zip
for ind_h in range(len(heroes)):
    for ind_a in range(ind_h, len(ataques)):
        for ind_v in range(ind_h, len(villanos)):
            mensaje =\
                f"""
                {heroes[ind_h].capitalize()}
                Lanza un {ataques[ind_a].capitalize()}
                a {villanos[ind_v].capitalize()}
                """
            print(mensaje)
            break
        break
