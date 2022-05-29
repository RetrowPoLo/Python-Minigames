#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 3

import random


# Function that compare bot choice if user chooses rock
def rockCompare ():
    if (bot_play == "paper"):
        print (" Paper covers rock. You lose ! ")
    elif (bot_play == "scissors"):
        print (" Rock breaks scissors. You win ! ")


# Function that compare bot choice if user chooses paper
def paperCompare ():
    if (bot_play == "rock"):
        print (" Paper covers rock. You win ! ")
    elif (bot_play == "scissors"):
        print (" Scissors cut paper. You lose ! ")


# Function that compare bot choice if user chooses scissors
def scissorsCompare ():
    if (bot_play == "rock"):
        print (" Rock breaks scissors. You lose ! ")
    elif (bot_play == "paper"):
        print (" Scissors cut paper. You win ! ")


# Function that compare the bot and the player choice
def comparePlays ():
    if (user_play == bot_play):
        print (" It's a tie ! ")
    if (user_play == "rock"):
        rockCompare()
    elif (user_play == "paper"):
        paperCompare()
    elif (user_play == "scissors"):
        scissorsCompare()


# Loop to play the game
play = "y"
play_possible = ["rock", "paper", "scissors"]

while play == "y":

    user_play = input(" Rock Paper or Scissors ? \n").lower()
    bot_play = random.choice(play_possible)
    print(f" The bot plays {bot_play} ")
    comparePlays()

    play = input("\n Do you want to play another time ? (y or n) ")

print ("\n Thanks for playing ! ")

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

import random


# Function that compare bot choice if user chooses rock
def rockCompare ():
    if (bot_play == "paper"):
        print (" Paper covers rock. You lose ! ")
    elif (bot_play == "scissors"):
        print (" Rock breaks scissors. You win ! ")


# Function that compare bot choice if user chooses paper
def paperCompare ():
    if (bot_play == "rock"):
        print (" Paper covers rock. You win ! ")
    elif (bot_play == "scissors"):
        print (" Scissors cut paper. You lose ! ")


# Function that compare bot choice if user chooses scissors
def scissorsCompare ():
    if (bot_play == "rock"):
        print (" Rock breaks scissors. You lose ! ")
    elif (bot_play == "paper"):
        print (" Scissors cut paper. You win ! ")


# Function that compare the bot and the player choice
def comparePlays ():
    if (user_play == bot_play):
        print (" It's a tie ! ")
    if (user_play == "rock"):
        rockCompare()
    elif (user_play == "paper"):
        paperCompare()
    elif (user_play == "scissors"):
        scissorsCompare()


play_possible = ["rock", "paper", "scissors"]
user_play = input(" Rock Paper or Scissors ? \n").lower()
bot_play = random.choice(play_possible)
print(f" The bot plays {bot_play} ")
comparePlays()

print ("\n Thanks for playing ! ")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
