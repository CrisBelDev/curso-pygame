# dibujar figuras geometricas
import pygame
import sys

pygame.init()
# definir colores
Black   = (0,0,0)
white   = (255,255,255)
green   = (0,255,0)
red     = (255,0 ,0)
blue     = (0,0,255)
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
    screen.fill(red) # color de fondo
    # zona para dibujo ---------------
    pygame.draw.line(screen,green, [0,100], [200,300],5)
    pygame.draw.rect(screen,Black,(100,100,80,80))
    pygame.draw.circle(screen,Black, (300,200),50)
    # zona para dibujo ---------------
    pygame.display.flip() # actualizamos pantalla