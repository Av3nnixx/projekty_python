import random
values = ["Paper","Rock","Scissors"]
def choose():
    player_choose = input("Paper Rock Scissors: ")
    bot_pick = values[random.randint(0,2)]
    print(f"Bot pick {bot_pick}")
    print(f"Plyer pick {player_choose}")
    match bot_pick,player_choose:
        case "Scissors","Rock":
            return "Player win"
        case "Scissors","Paper":
            return "Bot win"
        case "Paper","Rock":
            return "Bot win"
        case "Paper","Scissors":
            return "Player win"
        case "Rock","Paper":
            return  "Player win"
        case "Rock","Scissors":
            return "Bot win"
        case _ :
            print("Draw")
            return choose()
print(choose())