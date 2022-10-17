import pygame
import colores
import random

def crear(x,y,ancho,alto):
    # Leer una imagen
    imagen_dona_mala = pygame.image.load("CLASE_PYGAME_INTRO/dona_rotten.png")
    imagen_dona_mala = pygame.transform.scale(imagen_dona_mala,(ancho,alto))
    rect_dona_mala = imagen_dona_mala.get_rect()
    rect_dona_mala.x = x
    rect_dona_mala.y = y
    dict_dona_mala = {}
    dict_dona_mala["surface"] = imagen_dona_mala
    dict_dona_mala["rect"] = rect_dona_mala
    dict_dona_mala["visible"] = True
    dict_dona_mala["speed"] = random.randrange (10,20,1)
    return dict_dona_mala

def update(lista_donas_malas):
    for dona_mala in lista_donas_malas:
        rect_dona_mala = dona_mala["rect"]
        rect_dona_mala.y = rect_dona_mala.y + dona_mala["speed"]


def actualizar_pantalla(lista_donas_malas,personaje,ventana_ppal):
    for dona_mala in lista_donas_malas:
        if(personaje["rect"].colliderect(dona_mala["rect"])):
            personaje["score"] = personaje["score"] - 500
            restar_dona_mala(dona_mala)
        
        if(dona_mala["rect"].y > 680):
            restar_dona_mala(dona_mala)
        ventana_ppal.blit(dona_mala["surface"],dona_mala["rect"])
    '''
    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]), True, colores.NEGRO)
    ventana_ppal.blit(text,(0,0))
    '''
def crear_lista_donas_malas(cantidad):
    lista_donas_malas = []
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,540,60)
        lista_donas_malas.append(crear(x,y,60,60))
    return lista_donas_malas

def restar_dona_mala(dona_mala):
    dona_mala["rect"].x = random.randrange (0,540,60)
    dona_mala["rect"].y = random.randrange (-1000,0,60)
