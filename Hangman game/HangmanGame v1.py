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

    if proposal in word:
        letter_found = letter_found + proposal
        print(" You find a letter ! \n")
    else:
        attemp = attemp - 1
        print(f" Letter not in the word ! {attemp} more attemps \n")
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
