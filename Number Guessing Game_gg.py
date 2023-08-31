import random
import math

computer_Guess = random.randint(1,50)
user_Guess = int(input('enter a number between 1 and 50: '))

while user_Guess!=computer_Guess:
    if user_Guess > computer_Guess:
        print('Lmao higher than Wiz Khalifa in April')
        user_Guess = int(input('enter a number between 1 and 50: '))
    elif user_Guess < computer_Guess:
        print('Lmao lower than my gpa')
        user_Guess = int(input('enter a number between 1 and 50: '))
    elif user_Guess > 50 or user_Guess < 1:
        print('come on mane you read the prompt be fr...')
        user_Guess = int(input('enter a number between 1 and 50: '))

if user_Guess==computer_Guess:
    print('You Win')
    print('You get nothing now go away!')
