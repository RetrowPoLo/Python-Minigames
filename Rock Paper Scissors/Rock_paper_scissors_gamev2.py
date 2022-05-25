import random

def botPlay ():
    play_possible = ["rock", "paper", "scissor"]
    bot_play = random.choice(play_possible)
    return bot_play

def userPlay ():
    user_play = input(" Rock Paper or Scissors ? \n").lower()
    return user_play

def comparePlay ():
    if (userPlay() != botPlay()):
        print(" You loose ! Better luck next time ")
    else:
        print(" You won ! ")

comparePlay()
