# Clase 04 : Creacion de Animaciones

import pygame
import sys

pygame.init() # iniciamos pygame
# definir colores
Black   = (0,0,0)
white   = (255,255,255)
green   = (0,255,0)
red     = (255,0 ,0)
blue    = (0,0,255)
#creando una ventana
ancho = 800
alto = 500
size = (ancho,alto) # tamaño
#reloj : controlar los FPS 
clock = pygame.time.Clock()
# Coordenadas del cuadrado
cord_x = 0
cord_y = 200
# dimension de cuadrado
dim_x = 50
dim_y = 50
# velocidad que se movera el cuadrado
speed_x = 3
speed_y = 3

screen = pygame.display.set_mode(size) # tamaño ventana
while True:
    for event in pygame.event.get():
        #print(event) # vemos todos los eventos que ocurren
        if event.type == pygame.QUIT:
            pygame.quit() #salimos de la ventana
            sys.exit()
    # --------------- Logica del juego ----------------
    if cord_x > ancho - dim_x or cord_x < 0:
        speed_x *= -1
    if cord_y > alto - dim_y or cord_y < 0:
        speed_y *= -1    
    
    cord_x += speed_x
    cord_y += speed_y
    # --------------- Logica del juego ----------------

    screen.fill(white) # color de fondo
    # zona para dibujo con for loops---------------
    pygame.draw.rect(screen,Black,(cord_x,cord_y,dim_x,dim_y))
    # zona para dibujo ---------------
    pygame.display.flip() # actualizamos pantalla
    clock.tick(60)