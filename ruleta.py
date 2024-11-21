#!/usr/bin/env python3
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random
from funciones import *
from variables import *

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 
DARK_GREEN = (0, 180, 0)
GREY = (120,120,120)
YELLOW = (243,228,67)


#Para saber como va a girar la ruleta y definir el angulo que lleva cada número para mostrarlo

pygame.init()
clock = pygame.time.Clock()


# Definir la finestra
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ruleta')



clicked = False
mouse_x, mouse_y = -1, -1


# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global clicked, spinning
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spinning = True
                
    
    return True

# Fer càlculs
def app_run():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pass
    
        
# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(GREY)

    
    draw_roulette()
    
    pygame.display.update()



#Roulette
def draw_roulette():
    
    rad_first = ((360 / 37) * (math.pi / 180)) #First angle
    rad_second = ((360 / 37) * (math.pi / 180) + (rad_first)) #Second angle

    rad_1 = rad_second
    rad_2 = ((360 / 37) * (math.pi / 180) + (rad_1))

    rad_num = ((360 / 37) * (math.pi / 180) * 5) / 2
    rad_num1 = ((360 / 37) * (math.pi / 180) * 3) / 2
    pygame.draw.polygon(screen, GREEN, [(screen_width // 2, screen_height // 2),
                        (screen_width // 2 + (250 * math.cos(rad_first)), screen_height // 2 + (250 * math.sin(rad_first))),
                        (screen_width // 2 + (250 * math.cos(rad_second)), screen_height // 2 + (250 * math.sin(rad_second)))])
if __name__ == "__main__":
    main()
