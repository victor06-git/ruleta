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
BROWN = (98,52,18)




#Para saber como va a girar la ruleta y definir el angulo que lleva cada número para mostrarlo

pygame.init()
clock = pygame.time.Clock()


# Definir la finestra
screen_width = 1500
screen_height = 950
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
# Gestionar events
def app_events():
    global clicked, spinning

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botón cerrar ventana
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = False
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
    table()
    
    pygame.display.update()

#Roulette
def draw_roulette():

    rad_first = ((360 / 37) * (math.pi / 180)) #First angle
    rad_second = ((360 / 37) * (math.pi / 180) + (rad_first)) #Second angle

    rad_1 = rad_second
    rad_2 = ((360 / 37) * (math.pi / 180) + (rad_1))

    rad_num = ((360 / 37) * (math.pi / 180) * 5) / 2
    rad_num1 = ((360 / 37) * (math.pi / 180) * 3) / 2
   
    #Ruleta parte verde del 0
    pygame.draw.polygon(screen, GREEN, [((screen_width // 2) / 2, screen_height // 2 - 100),
                        ((screen_width // 2) / 2 + (250 * math.cos(rad_first)), screen_height // 2 + (250 * math.sin(rad_first)) - 100),
                        ((screen_width // 2) / 2 + (250 * math.cos(rad_second)), screen_height // 2 + (250 * math.sin(rad_second)) - 100)])
    pygame.draw.polygon(screen, YELLOW, [((screen_width // 2) / 2, screen_height // 2 - 100), 
                                         ((screen_width // 2) / 2 + (250 * math.cos(rad_first)), screen_height // 2 + (250 * math.sin(rad_first)) - 100),
                                         ((screen_width // 2) / 2 + (250 * math.cos(rad_second)), screen_height // 2 + (250 * math.sin(rad_second)) - 100)], 2)
       
    #RULETA ROJO/NEGRO
    for angle in range(36):    

        if angle % 2 == 0:
            color = RED
        else:
            color = BLACK

        pygame.draw.polygon(screen, color, [(screen_width // 2 / 2 , screen_height // 2 - 100), 
                                            (screen_width // 2 / 2 + (250 * math.cos(rad_1)), screen_height // 2 + (250 * math.sin(rad_1)) - 100),
                                            (screen_width // 2 / 2 + (250 * math.cos(rad_2)), screen_height // 2 + (250 * math.sin(rad_2)) - 100)])
        pygame.draw.polygon(screen, YELLOW, [(screen_width // 2 / 2 , screen_height // 2 - 100), 
                                             (screen_width // 2 / 2 + (250 * math.cos(rad_1)), screen_height // 2 + (250 * math.sin(rad_1)) - 100),
                                             (screen_width // 2 / 2 + (250 * math.cos(rad_2)), screen_height // 2 + (250 * math.sin(rad_2)) - 100)], 2)
        rad_1 += 0.1698
        rad_2 += 0.1698
    #Centro ruleta y borde
    pygame.draw.circle(screen, BROWN, (screen_width // 2 / 2, screen_height // 2 - 100), 260, 20)
    pygame.draw.circle(screen, BROWN, (screen_width // 2 / 2, screen_height // 2 - 100), 150)

    #lista números ruleta
    roulette_numbers = [32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 
                        11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 
                        9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    
    x0 = (screen_width // 2 / 2 ) + (215 * math.cos(rad_num1))
    y0 = screen_height // 2  + (215 * math.sin(rad_num1)) - 100
    font0 = pygame.font.Font(None, 20)
    text0 = font0.render(str(0), True, WHITE)
    text_rect0 = (x0,y0)
    screen.blit(text0, text_rect0)
    
    for number in roulette_numbers:    
        x = (screen_width // 2 / 2) + (215 * math.cos(rad_num))
        y = (screen_height // 2 )+ (215 * math.sin(rad_num)) - 100
        font = pygame.font.Font(None, 20)
        text = font.render(str(number), True, WHITE)
        text_rect = (x,y)
        screen.blit(text, text_rect)
        rad_num += ((360/37) * (math.pi/180)) 

def table():
    points_rect0 = [(screen_width // 2 - 50, screen_height // 2 + 200), (screen_width // 2 + 50, screen_height // 2 - 20), (screen_width // 2 + 50, screen_height // 2 + 400)]
    pygame.draw.polygon(screen, BLACK, points_rect0, 3)

    numeros_caselles = {
        "Primera":{
            "Rojo": [3, 9, 12, 18, 21, 27, 30, 36],
            "Negro": [6, 15, 24, 33]
        },
        "Segunda": {
            "Rojo": [5, 14, 23, 32],
            "Negro": [2, 8, 11, 17, 20, 26, 29, 35]
        },
        "Tercero": {
            "Rojo": [1, 7, 16, 19, 25, 34],
            "Negro": [4, 10, 13, 22, 28, 31]
        }
    }

    for fila, color in numeros_caselles:
        
        
        if color == "Rojo":
            color_casella = RED
        elif color == "Negro":
            color_casella = BLACK
            
        pygame.draw.polygon(screen, color_casella, )

        


if __name__ == "__main__":
    main()
