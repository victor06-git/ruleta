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

roulette_numbers_angle = {
    0: 0,      # Verde
    32: 9.73,  # Rojo
    15: 19.46, # Negro
    19: 29.19, # Rojo
    4: 38.92,  # Negro
    21: 48.65, # Rojo
    2: 58.38,  # Negro
    25: 68.11, # Rojo
    17: 77.84, # Negro
    34: 87.57, # Rojo
    6: 97.30,  # Negro
    27: 107.03,# Rojo
    13: 116.76,# Negro
    36: 126.49,# Rojo
    11: 136.22,# Negro
    30: 145.95,# Rojo
    8: 155.68, # Negro
    23: 165.41,# Rojo
    10: 175.14,# Negro
    5: 184.87, # Rojo
    24: 194.60,# Negro
    16: 204.33,# Rojo
    33: 214.06,# Negro
    1: 223.79, # Rojo
    20: 233.52,# Negro
    14: 243.25,# Rojo
    31: 252.98,# Negro
    9: 262.71, # Rojo
    22: 272.44,# Negro
    18: 282.17,# Rojo
    29: 291.90,# Negro
    7: 301.63, # Rojo
    28: 311.36,# Negro
    12: 321.09,# Rojo
    35: 330.82,# Negro
    3: 340.55, # Rojo
    26: 350.28 # Negro
}

pygame.init()
clock = pygame.time.Clock()


# Definir la finestra
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ruleta')

angle = 0
spinning = False
spin_speed = 0
decelaration = 0.98
initial_speed = 20
min_speed = 0.1

clicked = False
mouse_x, mouse_y = -1, -1
selected_arrow_number = None
target_reached = False

#Contador
total_spins = 0
ocurrences = [0] * 37

percentage_dict = {
    0: 2, 1: 5, 2: 15, 3: 20, 4: 10, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5, 10: 5,
    11: 5, 12: 5, 13: 5, 14: 5, 15: 5, 16: 5, 17: 5, 18: 5, 19: 5, 20: 5, 21: 5, 22: 5,
    23: 5, 24: 5, 25: 5, 26: 5, 27: 5, 28: 5, 29: 5, 30: 5, 31: 5, 32: 5, 33: 5, 34: 5,
    35: 5, 36: 5
    }

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
    global clicked, spinning, selected_arrow_number, spin_speed, target_reached

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
                target_reached = False
                selected_arrow_number = select_number(percentage_dict)
                spin_speed = initial_speed
    
    return True

# Fer càlculs
def app_run():
    global spinning, angle, spin_speed, total_spins, ocurrences, selected_arrow_number, target_reached
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if spinning:
        
        current_angle = angle % 360
        target_angle = calculate_target_angle(selected_arrow_number)

        angle_diff = (target_angle - current_angle) % 360
        if angle_diff > 180:
            angle_diff -= 360

        angle += spin_speed

        spin_speed *= decelaration

        if spin_speed < min_speed and abs(angle_diff) < 1:
            if abs(angle_diff) < 1:
                spinning = False
                angle = angle - (current_angle - target_angle)
                ocurrences[selected_arrow_number] += 1
                total_spins += 1
                target_reached = True
        
# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(GREY)

    
    draw_roulette()
    #Flecha azul
    draw_arrow()
    # Actualitzar el dibuix a la finestra
    pygame.display.update()


#Dibuja la ruleta
def draw_arrow():
    pygame.draw.polygon(screen, BLUE, [(screen_width // 2 - 10, screen_height // 2 - 250),
                                       (screen_width // 2 + 10, screen_height // 2 - 250),
                                       (screen_width // 2 , screen_height // 2 - 200 )])
    if selected_arrow_number is not None:

            font = pygame.font.SysFont(None, 50)

            text_number = font.render(f"Número: {selected_arrow_number}", True, BLUE)
            text_rect = text_number.get_rect(center=(screen_width // 2, 50))
            screen.blit(text_number, text_rect)
#Roulette
def draw_roulette():
    global angle_rad, angle
    for i in numbers:

        current_angle = math.radians(angle + i * (360 / 37))
        next_angle = math.radians(angle + ( i + 1 ) * (360 / 37))


       
        x = screen_width // 2 + 250 * 0.9 * math.cos(current_angle)
        y = screen_height // 2 + 250 * 0.9 * math.sin(current_angle)
        x2 = screen_width // 2 + 250 * 0.9 * math.cos(next_angle)
        y2 = screen_height // 2 + 250 * 0.9 * math.sin(next_angle)
       
              
        #Color ruleta / números
        if i == 0:
            color = GREEN
        elif i % 2 == 0:
            color = RED
        else:
            color = BLACK
        #Coordenadas ruleta
        polygon_points = [
            (screen_width // 2 , screen_height // 2 ),
            (x, y),
            (x2 , y2)
        ]
        
        roulette_order = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        current_number = roulette_order[i]
       
        radius = 250 * 0.7
        text_angle = math.radians(angle + (i + 0.5) * (360 / 37))
        text_x = screen_width // 2 + radius * math.cos(text_angle)
        text_y = screen_height // 2 + radius * math.sin(text_angle)
        

        #Ruleta y contorno amarillo/oro
        pygame.draw.polygon(screen, color, polygon_points)
        pygame.draw.polygon(screen, YELLOW, polygon_points, 1)

        font = pygame.font.SysFont(None, 25)
        text  = font.render(str(current_number), True, WHITE)
        text_rect = text.get_rect(center=(int(text_x), int(text_y)))
        #rotated_text = pygame.transform.rotate(text, -rotate_angle)
        #rotated_text_rect = rotated_text.get_rect(center=(int((x + x2) / 2 + 20), int((y + y2) / 2 - 10)))
        
        #Circulo interior blanco
        pygame.draw.circle(screen, WHITE, (screen_width // 2, screen_height // 2), 20)
        
        screen.blit(text, text_rect)

def calculate_target_angle(selected_number):
   return (270 - roulette_numbers_angle[selected_number]) % 360

#Funció que selecciona el número per el seu percentatge de sortida
def select_number(percentage_dict):
    total = sum(percentage_dict.values())
    rand = random.randint(1, total)
    cumulative = 0


    for number, percentage in percentage_dict.items():
        cumulative += percentage
        if rand <= cumulative:
            return number
if __name__ == "__main__":
    main()
