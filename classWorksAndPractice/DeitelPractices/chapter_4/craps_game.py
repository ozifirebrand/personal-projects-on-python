import random


# die one and two are rolled
# the sum of the two faces determines if player wins, loses or continues
# game
# A sum of 7 or 11 means win, 2, 3 or 12 on the first roll (called “craps”), you lose
# if the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your “point.”
# To win, you must continue rolling the dice until you “make your point” (i.e., roll
# that same point value). You lose by rolling a 7 before making your point.

def roll_dice():
    die_one = random.randrange(1, 7)
    die_two = random.randrange(1, 7)
    return die_one, die_two


def you_lose():
    number = (2, 3, 12)
    return number


def you_win():
    number = (7, 11)
    return number


def continue_playing():
    number = (4, 5, 6, 8, 9, 10)
    return number


def determine_win_status():
    # random.seed(32)
    numbers = roll_dice()
    for number in numbers:
        if number in you_win():
            print('You win!')
        elif number in you_lose():
            print('You lose!')
        elif number in continue_playing():
            print('Continue!')
            numbers2 = roll_dice()
            for number2 in numbers:
                if number2 in numbers2:
                    print()



# print(determine_win_status())