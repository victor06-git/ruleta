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

pygame.init()
clock = pygame.time.Clock()


# Definir la finestra
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ruleta')

angle = 0
spinning = False
spin_angle = 0
target_angle = 0

clicked = False
mouse_x, mouse_y = -1, -1
selected_arrow_number = None

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
    global clicked, spinning, spin_angle, selected_arrow_number, spin_angle, target_angle

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
                selected_arrow_number = select_number(percentage_dict)
                target_angle = calculate_target(selected_arrow_number)
                spin_angle = random.randint(720, 1800) + target_angle
    
    return True

# Fer càlculs
def app_run():
    global spinning, angle,spin_angle, total_spins, ocurrences
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if spinning:
        angle += spin_angle / 60
        spin_angle -= 1
        if spin_angle <= 0:
            spinning = False
            spin_angle = 0

            final_angle = angle % 360
            selected_arrow_number = int(final_angle / (360 / 37))

            ocurrences[selected_arrow_number] += 1
            total_spins += 1
            
        
        
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
    if not spinning and selected_arrow_number != None:
            font = pygame.font.SysFont(None, 50)
            text_number = font.render(f"Número: {selected_arrow_number}", True, BLUE)
            screen.blit(text_number, (screen_width // 2 - 100, 50))
#Roulette
def draw_roulette():
    global angle_rad, angle
    for i in numbers:
        angle_rad = math.radians(angle + i * (360 / 37))
        x  = screen_width // 2 + 250 * 0.9 * math.cos(angle_rad)
        y = screen_height // 2 + 250 * 0.9 * math.sin(angle_rad)
        x2 = screen_width // 2 + 250 * 0.9 * math.cos(math.radians(angle + (i + 1)* (360 / 37)))   
        y2 = screen_height // 2 + 250 * 0.9 * math.sin(math.radians(angle + (i + 1)* (360 / 37)))
       
        
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
        
       
        radius = 250 * 0.7
        text_x = screen_width // 2 + radius * math.cos(math.radians(angle + (i + 0.5) * (360 / 37)))
        text_y = screen_height // 2 + radius * math.sin(math.radians(angle + (i + 0.5) * (360 / 37)))
        

        #Ruleta y contorno amarillo/oro
        pygame.draw.polygon(screen, color, polygon_points)
        pygame.draw.polygon(screen, YELLOW, polygon_points, 1)

        font = pygame.font.SysFont(None, 25)
        text  = font.render(str(numbers[i]), True, WHITE)
        text_rect = text.get_rect(center=(int(text_x), int(text_y)))
        #rotated_text = pygame.transform.rotate(text, -rotate_angle)
        #rotated_text_rect = rotated_text.get_rect(center=(int((x + x2) / 2 + 20), int((y + y2) / 2 - 10)))
        
        #Circulo interior blanco
        pygame.draw.circle(screen, WHITE, (screen_width // 2, screen_height // 2), 20)
        
        screen.blit(text, text_rect)

def calculate_target(selected_number):
    #Cada número té un angle determinat
    angle_number = 360 / 37
    return selected_number * angle_number

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
