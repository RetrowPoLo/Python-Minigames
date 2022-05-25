import random

play_possible = ["rock", "paper", "scissor"]
bot_play = random.choice(play_possible)

user_play = input("Rock Paper or Scissors ? \n").lower()

if (user_play != bot_play):
    print("You loose ! ")
else:
    print("You won ! ")
