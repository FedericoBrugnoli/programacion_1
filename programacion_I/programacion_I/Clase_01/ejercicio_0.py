#La división de higiene está trabajando en un control de stock para productos sanitarios. 
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio,
# de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y 
# el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

flag_barbijo_mas_caro = 0
flag_item_mas_unidades = 0

cantidad_jabon = 0
cantidad_alcohol = 0
cantidad_barbijo = 0

for i in range(5):
    tipo = input("Ingrese el tipo de producto: 'Barbijo, jabón o alcohol'") #El tipo (validar "barbijo", "jabón" o "alcohol")
    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("Error, reingrese un tipo de producto válido: 'Barbijo, jabón o alcohol'")

    precio = input("Ingrese el precio del producto: ") #El precio: (validar entre 100 y 300)
    precio = float(precio)
    while(not precio < 100 and precio > 300):
        precio = input("Error, reingrese un precio del producto válido: ")
        precio = float(precio)

    cantidad = input("Ingrese la cantidad de productos: ")
    cantidad = int(cantidad)
    while(not cantidad > 0 and cantidad < 1000):#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
        cantidad = input("Error, reingrese una cantidad de productos válida: ")
        cantidad = int(cantidad)

    marca = input("Ingrese la marca: ")#La marca y el Fabricante.
    fabricante = input("Ingrese el fabricante: ")


    if (tipo == "barbijo"):#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
        if (flag_barbijo_mas_caro == 0):
            barbijo_mas_caro_cant = cantidad
            barbijo_mas_caro_fab = fabricante
            barbijo_mas_caro_precio = precio
            flag_barbijo_mas_caro = 1
        elif (barbijo_mas_caro_precio < precio):
            barbijo_mas_caro_cant = cantidad
            barbijo_mas_caro_fab = fabricante
            barbijo_mas_caro_precio = precio

    if (tipo == "jabon"):
        cantidad_jabon = cantidad + cantidad_jabon#Cuántas unidades de jabones hay en total.

    if (flag_item_mas_unidades == 0):#Del ítem con más unidades, el fabricante.
        tipo_mas_unidades = tipo
        fabricante_mas_unidades = fabricante
        cantidad_mas_unidades = cantidad
        flag_item_mas_unidades = 1
    elif (cantidad_mas_unidades < cantidad):
        tipo_mas_unidades = tipo
        fabricante_mas_unidades = fabricante
        cantidad_mas_unidades = cantidad

print("El barbijo mas caro es fabricado por " + barbijo_mas_caro_fab + ", que cuesta $" + str(barbijo_mas_caro_precio) + ", y se vendieron " 
+ str(barbijo_mas_caro_cant) + " unidades")
print("/n La cantidad total de unidades de jabon vendidas es " + str(cantidad_jabon))
print("/n El item con mas unidades es " + tipo_mas_unidades + ", con " + str(cantidad_mas_unidades) + " unidades, y su fabricante es "
+ fabricante_mas_unidades)

'''

    elif (tipo == "barbijo"):
        cantidad_barbijo = cantidad + cantidad_barbijo
    else:
        cantidad_alcohol = cantidad + cantidad_alcohol

    if (cantidad_jabon > cantidad_barbijo and cantidad_jabon > cantidad_alcohol):
        print("El item con mas unidades es el jabon, con " + cantidad_jabon + " unidades")
    elif(cantidad_barbijo > cantidad_alcohol):
        print("El item con mas unidades son los barbijos, con " + cantidad_barbijo + " unidades")
    else:
        print("El item con mas unidades es el alcohol, con " + cantidad_alcohol + " unidades")
'''    

