#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 3

import random

play = "y"
user_score = 0
bot_score = 0

while play == "y":
    def botPlay ():
        play_possible = ["rock", "paper", "scissor"]
        bot_play = random.choice(play_possible)
        return bot_play

    def userPlay ():
        user_play = input(" Rock Paper or Scissors ? \n").lower()
        return user_play

    def comparePlay (bot_score, user_score):
        if (userPlay() != botPlay()):
            bot_score = bot_score + 1
            print(" You loose ! Better luck next time ")
            print(bot_score)
        else:
            user_score = user_score + 1
            print(" You won ! ")
            print(user_score)

    comparePlay(bot_score, user_score)
    play = input(" Do you want to play another time ? (y or n) ")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 2

# import random

# def botPlay ():
#     play_possible = ["rock", "paper", "scissor"]
#     bot_play = random.choice(play_possible)
#     return bot_play

# def userPlay ():
#     user_play = input(" Rock Paper or Scissors ? \n").lower()
#     return user_play

# def comparePlay ():
#     if (userPlay() != botPlay()):
#         print(" You loose ! Better luck next time ")
#     else:
#         print(" You won ! ")

# comparePlay()


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 1

# import random

# play_possible = ["rock", "paper", "scissor"]
# bot_play = random.choice(play_possible)

# user_play = input("Rock Paper or Scissors ? \n").lower()

# if (user_play != bot_play):
#     print("You loose ! ")
# else:
#     print("You won ! ")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
