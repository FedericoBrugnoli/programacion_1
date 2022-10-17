import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 400), 0, 32)
#pygame.display.set_caption("Vamos hacer un juego!")
#pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
imagen_f = pygame.image.load("C:/Users/R5/Desktop/UTN/Programacion_I/Pygame/dbz_fondo.jpg")

while(running):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))# Se pinta el fondo de la ventana
   # Se dibuja un círculo azul en el centro
    #pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
    window.blit(imagen_f,(0,0))

    pygame.display.flip()


