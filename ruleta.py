#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

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
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Window Title')

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
    global clicked

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
    return True

# Fer càlculs
def app_run():
    mouse_x, mouse_y = pygame.mouse.get_pos()

# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Escriure un text de prova
    font = pygame.font.SysFont("Arial", 55)
    text = font.render('Hello World!', True, BLACK)
    screen.blit(text, (50, 50))
    "pygame.draw.circle(screen, RED, (250,250), 150)"
    color = RED
    x = 200
    y = 50
    for _ in range(5):
        pygame.draw.arc(screen, color, (x, 250, 200, 200), 0 , -1, 10)
        x += 50
        if color == BLACK:    
            color = RED
        elif color == RED:
            color = GREEN
        elif color == GREEN:
            color = BLACK

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
