lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

'''
1. recorro la lista
2. busco un minimo
3. guardo ese minimo
4. comparo ese minimo con los demas'''


def buscar_minimo(lista:list):
    minimo = lista[0]
    for i in range(len(lista)):
        if(lista[i] < minimo):
            minimo = lista[i]
    return minimo



def ord_list(lista:list):
    lista_ordenar = lista.copy()
    lista_ordenada = [] 
    minimo = buscar_minimo(lista)
    lista_ordenada.append(minimo)
    while(len(lista_ordenada)>1):#no usar for, while 
        minimo = buscar_minimo(lista_ordenar)
        lista_ordenar.pop(minimo)#borrar minimo de ordenar
        lista_ordenada.append(minimo)
        



    print(lista_ordenada)

ord_list(lista) 

