import random


# Function that compare bot choice if user chooses rock
def rockCompare ():
    if (language == "fr"):
        if (bot_play == "papier"):
            print (" Le papier couvre la pierre. Vous perdez ! ")
            score[1] += 1
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
        elif (bot_play == "ciseaux"):
            print (" La pierre casse les ciseaux. Vous gagnez ! ")
            score[0] += 1
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
    else:
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
    if (language == "fr"):
        if (bot_play == "pierre"):
            print (" Le papier couvre la pierre. Vous gagnez ! ")
            score[0] += 1
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
        elif (bot_play == "ciseaux"):
            print (" Les ciseaux coupent le papier. Vous perdez ! ")
            score[1] += 1
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
    else:
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
    if (language == "fr"):
        if (bot_play == "pierre"):
            print (" La pierre casse les ciseaux. Vous perdez ! ")
            score[1] += 1
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
        elif (bot_play == "papier"):
            print (" Les ciseaux coupent le papier. Vous gagnez ! ")
            score[0] += 1
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
    else:
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
    if (language == "fr"):
        if (user_play == bot_play):
            print (" Egalité ! ")
            print(f" Votre score : {score[0]} , Score du bot : {score[1]} ")
        if (user_play == "pierre"):
            rockCompare()
        elif (user_play == "papier"):
            paperCompare()
        elif (user_play == "ciseaux"):
            scissorsCompare()
    else:
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
    if (language == "fr"):
        if (score[0] == score[1]):
            print (" Egalité ! ")
        if (score[0] > score[1]):
            print(" Vous avez gagné ! ")
        elif (score[0] < score[1]):
            print(" Vous avez perdu ! ")
    else:
        if (score[0] == score[1]):
            print (" It's a tie ! ")
        if (score[0] > score[1]):
            print(" You win ! ")
        elif (score[0] < score[1]):
            print(" You lose ! ")


# Play the game in french mode
def playFrenchMode():
    play = "o"
    print(" =============================== ")
    print (" Bienvenue dans le jeu de pierre papier ciseaux ! ")

    while (play == "o"):
        user_play = input("\n Pierre papier ou ciseaux ? \n").lower()
        while (user_play not in play_possible_fr):
            user_play = input(" Veuillez choisir pierre, papier ou ciseaux ! \n").lower()

        bot_play = random.choice(play_possible_fr)
        print(f" Le bot joue {bot_play} ")

        comparePlays()

        play = input("\n Voulez vous jouer une autre partie ? (o ou n) ").lower()

    print(f"\n Votre score final est {score[0]} , Le score final du bot est {score[1]} ")
    finalScore()
    print ("\n Merci d'avoir jouer ! ")


# Play the game in english mode
def playEnglishMode():
    play = "y"
    print(" =============================== ")
    print(" Welcome to the rock, paper, scissors game ! ")

    while (play == "y"):
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


play = ""
language = ""

play_possible = ["rock", "paper", "scissors"]
play_possible_fr = ["pierre", "papier", "ciseaux"]

score = [0, 0]      # [player score, bot score]

user_play = ""
bot_play = ""

# Choose the language of the game
while (language != "en" or language != "fr"):
    language = input(" In which language do you want to play ? (en/fr) ")

    if language == "fr":
        playFrenchMode()
        break

    if language == "en":
        playEnglishMode()
        break
