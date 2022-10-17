import pygame
import colores
import dona
import personaje
#import background_music
import dona_mala

ANCHO_VENTANA = 600
ALTO_VENTANA = 600

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-200,200,200)
lista_donas = dona.crear_lista_donas(50)
lista_donas_malas = dona_mala.crear_lista_donas_malas(10)

flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas)
                dona_mala.update(lista_donas_malas)

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT] :
        personaje.update(player,-10)
    if lista_teclas[pygame.K_RIGHT] :
        personaje.update(player,10)
    '''
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)
    background_music = pygame.mixer.Sound("CLASE_PYGAME_INTRO/The Simpsons Hit & Run Soundtrack - Main Theme.wav")
    background_music.set_volume(0.1)
    background_music.play(1)
    '''
    background = pygame.image.load("CLASE_PYGAME_INTRO/sillon.png")
    ventana_ppal.blit(background,(0,0))
    personaje.actualizar_pantalla(player,ventana_ppal)
    dona.actualizar_pantalla(lista_donas,player,ventana_ppal)
    dona_mala.actualizar_pantalla(lista_donas_malas,player,ventana_ppal)

    pygame.display.flip()
pygame.quit()