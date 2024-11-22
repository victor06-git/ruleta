import math
import random
from variables import *
from ruleta import table

def bet_columns (player):

    select_column = int(input("A que columna quieres apostar ? [0 // 1 // 2] "))#--> Esto se haria automaticamente al dejar la ficha en la casilla
    cantidad_column = int(input("Que numero de fichas quieres apostar ?: ")) #--> Esto pasaria despues de dejar la ficha en la columna correspondiente

    columna_seleccionada = chips[select_column]
    succesful_row = random.choice(chips)

    #El tipo de ficha tiene que registrarse automáticamente
    if columna_seleccionada == succesful_row:
        #players[player]["chips"]["Tipo de ficha"] += (1*cantidad_column)
        print("Has ganado la apuesta")
    else:
        #players[player]["chips"]["Tipo de ficha"] -= (1*cantidad_column)
        print("Has perdido la apuesta")

def odd_even (player):
    
    select_odd_even = input("Quieres apostar par o impar ?. [1.Par // 2.Impar] ")#--> Actualizar esto en base a donde coloquemos la ficha
    cantidad_odd_even = int(input("Que numero de fichas quieres apostar ?: ")) #--> Esto pasaria despues de dejar la ficha en la columna correspondiente

    numero_ruleta = random.choice(roulette_numbers)

    if select_odd_even == "1": #Esto luego se tiene que actulizar dependiendo de la posicion de la ficha
    
        if numero_ruleta % 2 == 0:
            #players[player]["chips"]["Tipo de ficha"] += (1*cantidad_column)
            print(f"Felicidades has ganado. El numero {numero_ruleta}, es 'par'")
    
        elif numero_ruleta % 2 != 0:
            print(f"Has perdido el numero {numero_ruleta} es 'impar'")
    
        elif numero_ruleta == 0:
            print(f"Has perdido. Ha salido el numero {numero_ruleta}")

    elif select_odd_even == "2":
    
        if numero_ruleta % 2 == 0:
            #players[player]["chips"]["Tipo de ficha"] += (1*cantidad_column)
            print(f"Felicidades has perdido. El numero {numero_ruleta}, es 'par'")
    
        elif numero_ruleta % 2 != 0:
            print(f"Has ganado el numero {numero_ruleta} es 'impar'")
    
        elif numero_ruleta == 0:
            print(f"Has perdido. Ha salido el numero {numero_ruleta}")
        
    return numero_ruleta

def bet_number(player):
    
    select_number = input("Selecciona un numero: ")#--> Actualizar esto en base donde coloquemos la ficha
    cantidad_number = int(input("Que cantidad de fihcas deseas apostar ? "))
    
    random_number = random.choice(roulette_numbers)

    if select_number == random_number:
        #players[player]["chips"]["Tipo de ficha"] += (5*cantidad_column) #--> La ficha se actualiza automáticamente dependiendo de que ficha coloquemos en el numero
        print(f"Felicidades has ganado. Has obtenido el mismo numero que la ruleta: {random_number}")
    else:
        #players[player]["chips"]["Tipo de ficha"] -= (5*cantidad_column)
        print(f"Has perdido. El numero de la ruleta ha sido el: {random_number}")

def color_number(player):
    orange = 1

