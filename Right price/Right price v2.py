import random

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Version 2

try_counter = 5
random_number = random.randint(0, 50)
print(f" You have {try_counter} try to find the right number ! (between 0 and 50) ")
user_number = int(input(" Choose a number : "))
game_status = True

while game_status != False:
    if try_counter != 1:
        if user_number == random_number:
            print(" You won ! You found the right number ! ")
            game_status = False
        if user_number != random_number:
            try_counter = try_counter - 1
            if user_number > random_number:
                if try_counter > 1:
                    print(f" Your number is too high ! {try_counter} more tries ! ")
                else:
                    print(f" Your number is too high ! {try_counter} more try ! ")
            if user_number < random_number:
                if try_counter > 1:
                    print(f" Your number is too low ! {try_counter} more tries ! ")
                else:
                    print(f" Your number is too low ! {try_counter} more try ! ")
            user_number = int(input(" Choose a new number : "))
    else:
        print(" You loose ! Try again ")
        game_status = False

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
