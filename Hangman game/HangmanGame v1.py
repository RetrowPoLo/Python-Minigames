#Find the mystery word !

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 1
attemp = 7
word = "chair"
display = ""
letter_found = ""

for l in word:
    display = display + "_ "

while attemp > 0:
    print(f" Word to find : {display} with {attemp} attemps ! ")
    proposal = input(" Submit a letter : ")
                                        # |___ [0:1].lower()
    if proposal in word:
        letter_found = letter_found + proposal
        print(" You find a letter ! \n")
    else:
        attemp = attemp - 1
        print(f" Letter not in the word ! \n")
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

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
