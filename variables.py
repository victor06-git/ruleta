players = {
    "player_purple":{
        "color": "purple",
        "money": 100,
        "your_turn":False,
        "chips":{
            "fitxa_100":90,
            "fitxa_50":0,
            "fitxa_20":0,
            "fitxa_10":0,
            "fitxa_5":0
        },
        "bet":{
            "odd_even":"",
            "column":"",
            "number":"",
            "color":"",
        }
    },
    "player_blue":{
        "color": "blue",
        "money": 100,
        "your_turn":False,
        "chips":{
            "fitxa_100":0,
            "fitxa_50":0,
            "fitxa_20":0,
            "fitxa_10":0,
            "fitxa_5":0
        },
        "bet":{
            "odd_even":"",
            "column":"",
            "number":"",
            "color":"",
        }
    },
    "player_orange":{
        "color": "orange",
        "money": 100,
        "your_turn":False,
        "chips":{
            "fitxa_100":90,
            "fitxa_50":0,
            "fitxa_20":0,
            "fitxa_10":0,
            "fitxa_5":0
        },
        "bet":{
            "odd_even":"",
            "column":"",
            "number":"",
            "color":"",
        }

    }
}

chips = [[1,4,7,10,13,16,19,22,25,28,31,34],
         [2,5,8,11,14,17,20,23,26,29,32,35],
         [3,6,9,12,15,18,21,24,27,30,33,36]]
numbers = list(range(37))
chip_0 = 0

#def lost_money(player) --> maneja la logica de la perdida de diner0
#def gain_money(player) --> maneja la logica de la ganancia de dinero
#def manage_money(player) --> en función de si gana o pierde, se añade a player["dinero"]
#def banca_rota(player)--> maneja la logica de cuando te quedas en banca rota
#def comprar fichas (player) --> Esta funcion permite comprar fichas

def buy_chips(player):

    ask_to_buy = input("Deseas comprar mas fitxas? [y/n] ").lower()

    if ask_to_buy == "yes":
        how_many = input("Select the chips to buy: [1. for 100 // 2. for 50 // 3: for 20 // 4. for 10 // 5. for 5] ")

        cuantity = int(input("How many do you want to buy ? "))

        while True:
            if how_many == "1":

                if players[player]["money"] >= (cuantity*100):

                    players[player]["money"] -= (cuantity*100)
                    players[player]["chips"]["fitxa_100"] += cuantity
                    print(f"Has adquirido {cuantity} fitxas de 100")

                else:
                    print("You do not have enough money")

            elif how_many == "2":

                if players[player]["money"] >= (cuantity*50):

                    players[player]["money"] -= (cuantity*50)
                    players[player]["chips"]["fitxa_50"] += cuantity
                    print(f"Has adquirido {cuantity} fitxas de 50")

                else:
                    print("You do not have enough money")

            elif how_many == "3":

                if players[player]["money"] >= (cuantity*20):

                    players[player]["money"] -= (cuantity*20)
                    players[player]["chips"]["fitxa_20"] += cuantity
                    print(f"Has adquirido {cuantity} fitxas de 20")

                else:
                    print("You do not have enough money")
            
            elif how_many == "4":

                if players[player]["money"] >= (cuantity*10):

                    players[player]["money"] -= (cuantity*10)
                    players[player]["chips"]["fitxa_10"] += cuantity
                    print(f"Has adquirido {cuantity} fitxas de 10")

                else:
                    print("You do not have enough money")
            
            elif how_many == "5":

                if players[player]["money"] >= (cuantity*5):

                    players[player]["money"] -= (cuantity*5)
                    players[player]["chips"]["fitxa_5"] += cuantity
                    print(f"Has adquirido {cuantity} fitxas de 5")
                else:
                    print("You do not have enough money")

            continue_to_purchase = input("Desas seguir comprando ? [y/no] ").lower()

            if continue_to_purchase == "no":
                break


def manage_bet(player):
    ask_bet = input("A que deseas apostar ? [1. Pares o Impares // 2. Columnas // 3. Numeros // 4. Color] ")

    if ask_bet == "1":

        while True:
            ask_chips = input("Cuantas fichas deseas apostar ? [1. Fitxas 100 // 2. Fitxas 50 // 3. Fitxas 20 // 4. Fitxas 10 // 5. Fitxas 5] ")

            if ask_chips == "1":
                ask_chips_100 = int(input("Cuantas fitxas de 100 quieres apostar ? \n"))

                if players[player]["chips"]["fitxa_100"] < ask_chips_100:
                    print("Error: no dispones de tantas fitxas")
                    buy_chips(player)

                elif players[player]["chips"]["fitxa_100"] >= ask_chips_100:

                    players[player]["bet"]["odd_even"] = True
                    players[player]["chips"]["fitxa_100"] -= ask_chips_100

                    print(f"Has apostado {ask_chips_100} de 100 a 'Pares o Impares'")
                    """AQUI SE PODRIA LLAMAR A UNA FUNCIÓN QUE DIGA BET_SUCCESFULL = TRUE OR FALSE, SI ES TRUE SE GANA EL DINERO SI ES FALSE SE PIERDE EL DINERO"""

            if ask_chips == "2":
                ask_chips_100 = int(input("Cuantas fitxas de 50 quieres apostar ?\n "))

                if players[player]["chips"]["fitxa_50"] < ask_chips_100:
                    print("Error: no dispones de tantas fitxas")
                    buy_chips(player)

                elif player[player]["chips"]["fitxa_50"] >= ask_chips_100:

                    players[player]["bet"]["odd_even"] = True
                    player[player]["chips"]["fitxa_50"] -= ask_chips_100

                    print(f"Has apostado {ask_chips_100} de 50 a 'Pares o Impares'")
            
            if ask_chips == "3":
                ask_chips_100 = int(input("Cuantas fitxas de 20 quieres apostar ?\n "))

                if players[player]["chips"]["fitxa_20"] < ask_chips_100:
                    print("Error: no dispones de tantas fitxas")
                    buy_chips(player)

                elif player[player]["chips"]["fitxa_20"] >= ask_chips_100:

                    players[player]["bet"]["odd_even"] = True
                    players[player]["chips"]["fitxa_20"] -= ask_chips_100

                    print(f"Has apostado {ask_chips_100} de 20 a 'Pares o Impares'")
            
            if ask_chips == "4":
                ask_chips_100 = int(input("Cuantas fitxas de 10 quieres apostar ?\n "))

                if players[player]["chips"]["fitxa_10"] < ask_chips_100:
                    print("Error: no dispones de tantas fitxas")
                    buy_chips(player)

                elif player[player]["chips"]["fitxa_10"] >= ask_chips_100:

                    players[player]["bet"]["odd_even"] = True
                    players[player]["chips"]["fitxa_10"] -= ask_chips_100

                    print(f"Has apostado {ask_chips_100} de 10 a 'Pares o Impares'")
            
            if ask_chips == "5":
                ask_chips_100 = int(input("Cuantas fitxas de 5 quieres apostar ?\n "))

                if players[player]["chips"]["fitxa_5"] < ask_chips_100:
                    print("Error: no dispones de tantas fitxas")
                    buy_chips(player)

                elif player[player]["chips"]["fitxa_5"] >= ask_chips_100:

                    players[player]["bet"]["odd_even"] = True
                    players[player]["chips"]["fitxa_5"] -= ask_chips_100

                    print(f"Has apostado {ask_chips_100} de 5 a 'Pares o Impares'")

            ask_for_betting = input("Deseas seguir apostando ? [y/n] ")
            if ask_for_betting == "no":
                break
                
        
    #for player in player:

#print(manage_bet("player_purple"))
