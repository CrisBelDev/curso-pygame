# clase 05: creacion de animaciones parte 2 (Animacion lluvia)
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

# moleculas de agua (cantidad)
coord_list = []
for i in range(60):
    x = random.randint(0, ancho)
    y = random.randint(0, alto)
    coord_list.append([x, y])
# ------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #color de pantalla
    screen.fill(white)

    for coord in coord_list:
        pygame.draw.circle(screen, red, coord, 2)
        coord[1]+=1
        coord[0] -=1
        if coord[0] < 0:
            coord[0] = ancho
        if (coord[1] > alto):
            coord[1] = 0

    #actualizamos pantalla
    pygame.display.flip()
    clock.tick(60)