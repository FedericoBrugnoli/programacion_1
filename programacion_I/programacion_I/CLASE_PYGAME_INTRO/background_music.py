import pygame

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
background_music = pygame.mixer.Sound("CLASE_PYGAME_INTRO/y2mate.com - The Simpsons Hit  Run Soundtrack  Main Theme.mp3")
background_music.play(-1)