import pygame
import sys

pygame.init()

#creando una ventana
import pygame
import sys

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        #print(event) # vemos todos los eventos que ocurren
        if event.type == pygame.QUIT:
            pygame.quit() #salimos de la ventana
            sys.exit()

