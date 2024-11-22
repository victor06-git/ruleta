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
GRAY = (128,128,128)




#Para saber como va a girar la ruleta y definir el angulo que lleva cada número para mostrarlo

pygame.init()
clock = pygame.time.Clock()


# Definir la finestra
screen_width = 1400
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ruleta')



clicked = False
mouse_x, mouse_y = -1, -1

rad_first = ((360 / 37) * (math.pi / 180)) #First angle
rad_second = ((360 / 37) * (math.pi / 180) + (rad_first)) #Second angle

rad_1 = rad_second
rad_2 = ((360 / 37) * (math.pi / 180) + (rad_1))

rad_num = ((360 / 37) * (math.pi / 180) * 5) / 2
rad_num1 = ((360 / 37) * (math.pi / 180) * 3) / 2

velocity = 0.1







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
    global clicked

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
    global rad_1, rad_2, rad_first, rad_second, velocity
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pass
    
        
# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(GREY)

    draw_grid()
    
    draw_roulette()
    table()
    
    pygame.display.update()

#Roulette
def draw_roulette():
    global rad_1,rad_2,rad_first,rad_second,rad_num,rad_num1
    
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
        rad_1 += ((360 / 37) * (math.pi / 180))
        rad_2 += ((360 / 37) * (math.pi / 180))
    
    #Centro ruleta y borde
    pygame.draw.circle(screen, BROWN, (screen_width // 2 / 2, screen_height // 2 - 100), 260, 20)
    pygame.draw.circle(screen, BROWN, (screen_width // 2 / 2, screen_height // 2 - 100), 150)
    pygame.draw.circle(screen, GRAY, (screen_width // 2 / 2, screen_height // 2 - 100), 190, 10)
    
    #Lineas interiors ruleta
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2, screen_height // 2 + 50), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2, screen_height // 2 - 250), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 + 148, screen_height // 2 - 100), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 - 148, screen_height // 2 - 100), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 + (148 * math.cos(math.pi / 4)), screen_height // 2 - 100 + (148 * math.sin(math.pi / 4))), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 - (148 * math.cos(math.pi / 4)), screen_height // 2 - 100 + (148 * math.sin(math.pi / 4))), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 + (148 * math.cos(1.25 * math.pi)), screen_height // 2 - 100 + (148 * math.sin(1.25 * math.pi))), 3)
    pygame.draw.line(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 - (148 * math.cos(1.25 * math.pi)), screen_height // 2 - 100 + (148 * math.sin(1.25 * math.pi))), 3)
    
    #Part interior
    pygame.draw.circle(screen, BLACK, (screen_width // 2 / 2, screen_height // 2 - 100), 30)
    pygame.draw.circle(screen, YELLOW, (screen_width // 2 / 2, screen_height // 2 - 100), 18)
    pygame.draw.line(screen, YELLOW, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2, screen_height // 2 - 30), 5)
    pygame.draw.circle(screen, YELLOW, (screen_width // 2 /2, screen_height // 2 - 30), 10)
    
    pygame.draw.line(screen, YELLOW, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2, screen_height // 2 - 170), 5)
    pygame.draw.circle(screen, YELLOW, (screen_width // 2 /2, screen_height // 2 - 170), 10)
   
    pygame.draw.line(screen, YELLOW, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 + 70, screen_height // 2 - 100), 5)
    pygame.draw.circle(screen, YELLOW, (screen_width // 2 / 2 + 70, screen_height // 2 - 100), 10)

    pygame.draw.line(screen, YELLOW, (screen_width // 2 / 2, screen_height // 2 - 100), (screen_width // 2 / 2 - 70, screen_height // 2 - 100), 5)
    pygame.draw.circle(screen, YELLOW, (screen_width // 2 / 2 - 70, screen_height // 2 - 100), 10)
    
    #lista números ruleta
    roulette_numbers = [32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    
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

#Tabla de apuestas
def table():
    #Parte del 0
    points_rect0 = [(1100, 50), (950, 100), (1250, 100), (1100, 50)]
    pygame.draw.polygon(screen, BLACK, points_rect0, 3)
    pygame.draw.polygon(screen, DARK_GREEN, points_rect0)
    

    font = pygame.font.SysFont(None, 30)
    text = font.render(str(0), True, WHITE)
    text_rect = (((950 + 1250) / 2 - 4) , 70) #Posicion de texto 0 centrado
    screen.blit(text, text_rect)
    
    height_casella = (600 / 13)
    width_casella = (300 / 3)

    #Casillas apuesta columna
    pygame.draw.rect(screen, BLACK, (950 + (width_casella), 100 + (600 / 13) * 12, width_casella, height_casella), 3)
    pygame.draw.rect(screen, BLACK, (950 , 100 + (600 / 13) * 12, width_casella, height_casella), 3)
    pygame.draw.rect(screen, BLACK, (950 + (2 * width_casella), 100 + (600 / 13) * 12, width_casella, height_casella), 3)

    #Pares/ Impares/ Rojo/ Negro
    pygame.draw.rect(screen, DARK_GREEN, (850, 100 ,100, 100))
    pygame.draw.rect(screen, DARK_GREEN, (850 , 200, 100, 180))
    pygame.draw.rect(screen, DARK_GREEN, (850 , 380, 100, 180))
    pygame.draw.rect(screen, DARK_GREEN, (850 ,555, 100, 100))
    pygame.draw.rect(screen, BLACK, (850, 100 ,100, 100), 3)
    pygame.draw.rect(screen, BLACK, (850 , 200, 100, 180), 3)
    pygame.draw.rect(screen, BLACK, (850 , 380, 100, 180), 3)
    pygame.draw.rect(screen, BLACK, (850 ,555, 100, 100), 3)

    #Rombos rojo y negro
    pygame.draw.polygon(screen, RED, [(900, (200 + ((180 / 2) / 4))),
                                      (850 + (100 / 4), (200 + (180 / 2))), 
                                      (900, (200 + 3 * (180 / 4) + 25)),
                                      (950 - ((100 / 4)), (200 + (180 / 2)))])
    
    pygame.draw.polygon(screen, BLACK, [(900, (380 + ((180 / 2) / 4))),
                                      (850 + (100 / 4), (380 + (180 / 2))), 
                                      (900, (380 + 3 * (180 / 4) + 25)),
                                      (950 - ((100 / 4)), (380 + (180 / 2)))])
    



    for  columna in range(3):
        for fila in range(12):
            
            if columna == 0 or columna == 2:
                if fila % 2 == 0:
                    color = RED
                else: 
                    color = BLACK
            if columna == 1:
                if fila % 2 == 0:
                    color = BLACK
                else:
                    color = RED

            if columna == 0:
                column_number = 0
            elif columna == 1:
                column_number = 1
            else:
                column_number = 2
            

            
            pygame.draw.rect(screen, BLACK, (950 + (columna * width_casella), 100 + (fila * height_casella), width_casella, height_casella), 3) #Contorno casilla
            pygame.draw.rect(screen, color, (950 + (columna * width_casella), 100 + (fila * height_casella), width_casella, height_casella)) #Relleno de color la casilla
            
            #Números casillas
            numbers = chips[column_number][fila]
            font = pygame.font.SysFont(None, 25)
            text = font.render(str(numbers), True, WHITE)
            text_rect = (950 + (columna * width_casella) + 50, 100 + ( fila * height_casella) + 15) #Posicion de texto
            screen.blit(text, text_rect)
            
#graellas
def draw_grid():
    
    # Color de la cuadrícula
    GRID_COLOR = (50, 50, 50)
    
    # Tamaño de las celdas
    cell_size = 50
    
    # Dibujar líneas verticales
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, screen_height))
        
        # Añadir texto de coordenadas X
        font = pygame.font.Font(None, 20)
        text = font.render(str(x), True, (200, 200, 200))
        screen.blit(text, (x+2, 2))
    
    # Dibujar líneas horizontales
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (screen_width, y))
        
        # Añadir texto de coordenadas Y
        font = pygame.font.Font(None, 20)
        text = font.render(str(y), True, (200, 200, 200))
        screen.blit(text, (2, y+2))

if __name__ == "__main__":
    main()
