# Figuras con for loops
import pygame
import sys

pygame.init()
# definir colores
Black   = (0,0,0)
white   = (255,255,255)
green   = (0,255,0)
red     = (255,0 ,0)
blue    = (0,0,255)
#creando una ventana
import pygame
import sys

pygame.init() # iniciamos pygame
size = (800,600) # tamaño
screen = pygame.display.set_mode(size) # tamaño ventana
while True:
    for event in pygame.event.get():
        #print(event) # vemos todos los eventos que ocurren
        if event.type == pygame.QUIT:
            pygame.quit() #salimos de la ventana
            sys.exit()
    screen.fill(white) # color de fondo
    # zona para dibujo con for loops---------------
    for x in range(100,700,100):
        pygame.draw.rect(screen,Black,(x,230,50,50))
        pygame.draw.line(screen,green,(x,0),(x,99),5)
    # zona para dibujo ---------------
    pygame.display.flip() # actualizamos pantalla