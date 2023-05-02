# clase 06: mover objetos con el mouse
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


# ------------------------------
pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #color de pantalla
    screen.fill(white)

    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]
    
    if x  > ancho- 50:
        x= ancho - 50
    if y > alto -50:
        y = alto-50
    

    pygame.draw.rect(screen, red, (x,y,50,50))

    #actualizamos pantalla
    pygame.display.flip()
    clock.tick(60)