players = {
    "player_purple":{
        "color": "purple",
        "money": 100,
        "your_turn":False,
        "chips":{
            "fitxa_100":0,
            "fitxa_50":0,
            "fitxa_20":0,
            "fitxa_10":0,
            "fitxa_5":0
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
        }
    },
    "player_orange":{
        "color": "orange",
        "money": 100,
        "your_turn":False,
        "chips":{
            "fitxa_100":0,
            "fitxa_50":0,
            "fitxa_20":0,
            "fitxa_10":0,
            "fitxa_5":0
        }
    }
}

chips = [[1,4,7,10,13,16,19,22,25,28,31,34],
         [2,5,8,11,14,17,20,23,26,29,32,35],
         [3,6,9,12,15,18,21,24,27,30,33,36]]

chip_0 = 0

#def lost_money(player) --> maneja la logica de la perdida de diner0
#def gain_money(player) --> maneja la logica de la ganancia de dinero
#def manage_money(player) --> en función de si gana o pierde, se añade a player["dinero"]
#def banca_rota(player)--> maneja la logica de cuando te quedas en banca rota
mou