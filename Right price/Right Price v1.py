# Guess the right number !

import random

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 1 


try_counter = 5
random_number = random.randint(0, 50)
user_number = int(input())
game_status = True

while game_status != False:
    if try_counter != 0:
        if user_number == random_number:
            print(" You won ! ")
            game_status = False
        if user_number != random_number:
            try_counter = try_counter - 1
            print(f" Not this time ! {try_counter} more try ! ")
            user_number = int(input())
    else:
        print(" You loose ! Try again ")
        game_status = False

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
