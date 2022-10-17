
dic_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios'
# en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'
product = str(input("ingrese un producto: (banana, pera, frutilla, mango)"))
if product in dic_precios:
    print("El producto seleccionado es: {0}, su valor es de ${1} y hay en stock hay {2} productos".format(product.capitalize(),dic_precios[product]['precio'],dic_precios[product]['stock']))
else:
    print(dic_precios.get(product,"El articulo no se encuentra en la lista."))

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el
# precio total (precio * cantidad)

cant = int(input("ingrese cant: "))
if cant > dic_precios[product]['stock']:
    print("Error, quiere llevar más productos de los que hay en stock.")
else:
    price = dic_precios[product]['precio'] * cant
print(price)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio,
# unidad de medida y stock. Agregar la nueva fruta a la lista de precios

nueva_fruta = input("Ingrese una nueva fruta: ").lower()
nuevo_precio = float(input("Ingrese el precio: $"))
nueva_udm = input("Ingrese la unidad de medida: (kg o unidad)").lower()
nuevo_stock = int(input("Ingrese la cantidad en stock: "))

dic_precios.update({nueva_fruta:{'precio':nuevo_precio,'unidad_medida':nueva_udm,'stock':nuevo_stock}})

print(dic_precios)
# Punto 4: imprimir el listado de frutas (solo su nombre)

print(list(dic_precios.keys()))

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir
# eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

fruta_pop = str(input("Seleccione la fruta a eliminar:").lower())
fruta_eliminada = dic_precios.pop(fruta_pop,"El articulo no se encuentra en la lista")
print(fruta_eliminada)

