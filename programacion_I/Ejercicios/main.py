'''
1 - Listar TOP N videos
2 - Ordenar videos por duracion (UP/DOWN)
3 - Ordenar videos por cantidad de views (UP/DOWN)
4 - Buscar videos por título 
5 - Exportar lista de videos a CSV
6 - Salir

        {
            "title": "Papa rosti con salchicha parrillera 🥔#paparosti #salchicha #patatas #papa #recetadepapa #shorts",
            "views": 11432,
            "length": 42,
            "img_url": "https://i.ytimg.com/vi/ZGni3XkUEeU/hqdefault.jpg",
            "url": "https://youtube.com/watch?v=ZGni3XkUEeU",
            "date": "2022-09-20 00:00:00"
        }
'''
import funct

def paulina_app():
    lista_videos = func.cargar_json("./CLASE_repaso_pp/data_paulina.json")
    while(True):
        print("1 - Listar TOP N videos\n2 - Ordenar videos por duracion (UP/DOWN)\n3 - Ordenar videos por cantidad de views (UP/DOWN)\n4 - Buscar videos por título \n5 - Exportar lista de videos a CSV\n6 - Salir")
        respuesta = input()
        if(respuesta=="1"):
            top = int(input("\n¿Cantidad de elementos a mostrar?: "))
            # VALIDAR QUE TOP SEA UN INT
            func.mostrar(lista_videos[:top])
        elif(respuesta=="2"):
            func.mostrar(func.nahuel_sort_improve(lista_videos,"length","down"))
        elif(respuesta=="3"):
            lista_videos = func.nahuel_sort_improve(lista_videos,"views","down")
            lista_videos.reverse()
            func.mostrar(lista_videos)
        elif(respuesta=="4"):
            patron = input("Burcar: ")
            func.buscar(lista_videos,patron)
        elif(respuesta=="5"):
            func.exprotar_csv(lista_videos,"./CLASE_repaso_pp/paulina.csv")
        elif(respuesta=="6"):
            break

respuesta = input("Seleccione una opción: 1 - Listar TOP N videos\n2 - Ordenar videos por duracion (UP/DOWN)\n3 - Ordenar videos por cantidad de views (UP/DOWN)\n4 - Buscar videos por título\n5 - Exportar lista de videos a CSV\n6 - Salir\n>")
while True:
    if respuesta == "1":
        print("1 - Listar TOP N videos")
    elif respuesta == "2":
        print("2 - Ordenar videos por duracion (UP/DOWN)")
    elif respuesta == "3":
        print("3 - Ordenar videos por cantidad de views (UP/DOWN)")
    elif respuesta == "4":
        print("4 - Buscar videos por título")
    elif respuesta == "5":
        print("5 - Exportar lista de videos a CSV")
    elif respuesta == "6":
        print("6 - Salir")
        break
#paulina_app()