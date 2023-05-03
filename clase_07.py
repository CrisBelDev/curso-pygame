# clase 07: mover objetos con el teclado
import pygame, sys, random
pygame.init()

# Ventana
ancho = 800
alto = 600
size = (ancho, alto)
screen = pygame.display.set_mode(size)
# reloj fps
clock = pygame.time.Clock()
# definiendo colores
Black   = (0,0,0)
white   = (255,255,255)
green   = (0,255,0)
red     = (255,0 ,0)
blue    = (0,0,255)


# ------------para el cuadrado------------------
coord_x = 10
coord_y = 10
speed_x = 0
speed_y = 0


pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # eventos teclado
        if event.type == pygame.KEYDOWN:    # al presionar tecla
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
        if event.type == pygame.KEYUP:      # dejo de presionar tecla
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0

    #color de pantalla
    screen.fill(white)
    # logica 
    coord_x += speed_x
    
    
    if coord_x  < 0:
        coord_x= 0
    elif coord_x > ancho -50:
            coord_x = ancho - 50

    
    pygame.draw.rect(screen, red, (coord_x,coord_y,50,50))

    #actualizamos pantalla
    pygame.display.flip()
    clock.tick(60)