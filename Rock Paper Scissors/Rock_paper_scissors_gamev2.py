import random

# Function that compare bot choice if user chooses rock
def rockCompare ():
    if (bot_play == "paper"):
        print (" Paper covers rock. You lose ! ")
        score[1] += 1
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")
    elif (bot_play == "scissors"):
        print (" Rock breaks scissors. You win ! ")
        score[0] += 1
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")


# Function that compare bot choice if user chooses paper
def paperCompare ():
    if (bot_play == "rock"):
        print (" Paper covers rock. You win ! ")
        score[0] += 1
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")
    elif (bot_play == "scissors"):
        print (" Scissors cut paper. You lose ! ")
        score[1] += 1
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")


# Function that compare bot choice if user chooses scissors
def scissorsCompare ():
    if (bot_play == "rock"):
        print (" Rock breaks scissors. You lose ! ")
        score[1] += 1
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")
    elif (bot_play == "paper"):
        print (" Scissors cut paper. You win ! ")
        score[0] += 1
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")


# Function that compare the bot and the player choice
def comparePlays ():
    if (user_play == bot_play):
        print (" It's a tie ! ")
        print(f" Your score : {score[0]} , Bot score : {score[1]} ")
    if (user_play == "rock"):
        rockCompare()
    elif (user_play == "paper"):
        paperCompare()
    elif (user_play == "scissors"):
        scissorsCompare()


# Function that give the final score of the game
def finalScore ():
    if (score[0] > score[1]):
        print(" You win ! ")
    else:
        print(" You lose ! ")


# Loop of play the game
play = "y"
play_possible = ["rock", "paper", "scissors"]
score = [0, 0]      # [player score, bot score]

while play == "y":
    user_play = input("\n Rock Paper or Scissors ? \n").lower()
    while (user_play not in play_possible):
        user_play = input(" Please choose rock, paper or scissors ! \n").lower()

    bot_play = random.choice(play_possible)
    print(f" The bot plays {bot_play} ")

    comparePlays()

    play = input("\n Do you want to play another time ? (y or n) ").lower()


print(f"\n Your final was score : {score[0]} , Bot final was score : {score[1]} ")
finalScore()

print ("\n Thanks for playing ! ")
