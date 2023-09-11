import random
import math

MIN_GUESS = 1
MAX_GUESS = 50

def get_user_guess():
    while True:
        user_guess = input('enter a number between 1 and 50: ')
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess > 0:
                break
            else:
                print('Number must be greater than 0.')
        else:
            print('quit playin mane, a real number')
    return user_guess

def compare_nums():
    computer_guess = random.randint(MAX_GUESS)
    
    while user_guess != computer_guess:
        if user_guess > computer_guess:
            print('Lmao higher than Wiz Khalifa in April')
            get_user_guess()
        elif user_guess < computer_guess:
            print('Lmao lower than my gpa')
            get_user_guess()
        elif MIN_GUESS > user_guess > MAX_GUESS:
            print('come on mane you read the prompt be fr...')
            get_user_guess()
        else:
            print('You Win')
            print('You get nothing now go away!')
            break

def play_game():
    get_user_guess()
    compare_nums()