#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 3
import random

# 20 words in English
word_choice_en = ["apple", "bee", "cacao", "daily", "eagle", "labyrinth", "zoo", "object", "package", "rabbit", "bed", "lizard", "mayor", "turkey", "wall", "maggot", "glasses", "truck", "unknown", "armchair"]

# 20 words in French
word_choice_fr = ["pomme", "abeille", "cacao", "quotidien", "aigle", "labyrinthe", "zoo", "objet", "emballer", "lapin", "lit", "lezard", "maire", "dinde", "mur", "asticot", "lunettes", "camion", "inconnue", "fauteuil"]

# Function to play in English
def playEnglishMode(word_choice_en):

    user_play = input(" Do you want to play the hangman game ? (y or n) ")
    if user_play == "n":
        while user_play == "n":
            user_play = input(" Do you want to play the hangman game ? (y or n) ")
        user_play = "y"
    if user_play == "y":
        game_status = True
        play_again = "y"

        
    while play_again == "y":
        attemp = 7
        display = ""
        letter_found = ""
        letter_not_found = []
        word = random.choice(word_choice_en)
        
        for l in word:
            display = display + "_ "
        
        while attemp > 0:

            if attemp == 1:
                print(f" Word to find : {display} with {attemp} attemp ! ")

            else:
                print(f" Word to find : {display} with {attemp} attemps ! ")

            proposal = input(" Submit a letter : ")[0:1].lower()
            
            if proposal in word:
                letter_found = letter_found + proposal
                print(" You find a letter ! \n")
                
            else:
                letter_not_found.append(proposal)
                attemp = attemp - 1
                print(f" Letter not in the word ! ")
                print(f" Letters not in the word : {letter_not_found} \n")
                
                if attemp == 0:
                    print(" ==========Y= ")
                    
                if attemp <= 1:
                    print(" ||/       |  ")
                    
                if attemp <= 2:
                    print(" ||        0  ")
                    
                if attemp <= 3:
                    print(" ||       /|\ ")
                    
                if attemp <= 4:
                    print(" ||       /|  ")
                    
                if attemp <= 5:                    
                    print("/||           ")
                    
                if attemp <= 6:
                    print("==============\n")
                    
                if attemp == 0:
                    print(f" The word to find was '{word}' ")
            
            display = ""
            for x in word:
                if x in letter_found:
                    display += x + " "
                else:
                    display += "_ "
            
            if "_" not in display:
                print(f" You won ! The word was '{word}' ")
                break
                
        play_again = input(" Do you want to play another time ? (y or n) ")

    print("\n Have a nice day ! ")


# Function to play in French
def playFrenchMode(word_choice_fr):
    user_play = input(" Voulez-vous jouer au jeu du pendu ? (o ou n) ")
    if user_play == "n":
        while user_play == "n":
            user_play = input(" Voulez-vous jouer au jeu du pendu ? (o ou n) ")
        user_play = "o"
    if user_play == "o":
        game_status = True
        play_again = "o"

        
    while play_again == "o":
        attemp = 7
        display = ""
        letter_found = ""
        letter_not_found = []
        word = random.choice(word_choice_fr)
        
        for l in word:
            display = display + "_ "
        
        while attemp > 0:

            if attemp == 1:
                print(f" Mot à trouver : {display} avec {attemp} seule tentative restante ! ")

            else:
                print(f" Mot à trouver : {display} avec {attemp} tentatives restantes ! ")

            proposal = input(" Donner une lettre : ")[0:1].lower()
            
            if proposal in word:
                letter_found = letter_found + proposal
                print(" Vous avez trouver une lettre ! \n")
                
            else:
                letter_not_found.append(proposal)
                attemp = attemp - 1
                print(f" La lettre n'est pas dans le mot ! ")
                print(f" Lettres pas dans le mot : {letter_not_found} \n")
                
                if attemp == 0:
                    print(" ==========Y= ")
                    
                if attemp <= 1:
                    print(" ||/       |  ")
                    
                if attemp <= 2:
                    print(" ||        0  ")
                    
                if attemp <= 3:
                    print(" ||       /|\ ")
                    
                if attemp <= 4:
                    print(" ||       /|  ")
                    
                if attemp <= 5:                    
                    print("/||           ")
                    
                if attemp <= 6:
                    print("==============\n")
                    
                if attemp == 0:
                    print(f" Le mot à trouver était '{word}' ")
            
            display = ""
            for x in word:
                if x in letter_found:
                    display += x + " "
                else:
                    display += "_ "
            
            if "_" not in display:
                print(f" Vous avez gagné ! Le mot était '{word}' ")
                break
                
        play_again = input(" Voulez-vous jouer une autre fois ? (o ou n) ")

    print("\n Bonne journée ! ")

language_choice = ""
while language_choice != "en" or language_choice != "fr":
    language_choice = input(" In which language do you want to play ? (en/fr) ")
    if language_choice == "en":
        playEnglishMode(word_choice_en)
        break
    if language_choice == "fr":
        playFrenchMode(word_choice_fr)
        break

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
