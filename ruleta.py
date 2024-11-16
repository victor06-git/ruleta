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

pygame.init()
clock = pygame.time.Clock()


# Definir la finestra
screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Roulette')

angle = 0
spinning = False
spin_angle = 0

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
    global clicked, spinning, spin_angle

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
                spin_angle = random.randint(720, 1440)
    
    return True

# Fer càlculs
def app_run():
    global spinning, angle,spin_angle
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if spinning:
        angle += spin_angle / 60
        spin_angle -= 1
        if spin_angle <= 0:
            spinning = False
            spin_angle = 0
# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Escriure un text de prova
    font = pygame.font.SysFont("Arial", 55)
    
    draw_roulette()
    pygame.draw.polygon(screen, BLACK, [(screen_width // 2 - 10, screen_height // 2 - 250), (screen_width // 2 + 10, screen_height // 2 - 250), (screen_width // 2, screen_height // 2 - 300)])

    # Actualitzar el dibuix a la finestra
    pygame.display.update()
#Roulette
def draw_roulette():
    global angle_rad, angle
    for i in range(37):
        angle_rad = math.radians(angle + i * (360 / 37))
        x  = screen_width // 2 + 200 * math.cos(angle_rad)
        y = screen_height // 2 + 200 * math.sin(angle_rad)
        if i == 0:
            color = GREEN
        elif i % 2 == 0:
            color = RED
        else:
            color = BLACK
        pygame.draw.circle(screen, color, (int(x), int(y)), 30)
        font = pygame.font.SysFont(None, 36)
        text  = font.render(str(numbers[i]), True, WHITE)
        screen.blit(text, (int(x) - 10, int(y) - 10))

if __name__ == "__main__":
    main()
