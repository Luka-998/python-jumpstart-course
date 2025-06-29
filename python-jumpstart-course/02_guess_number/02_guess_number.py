
print("-"*60)
print(f'{'Guess The Number APP':^60}')
print("-"*60)

import os
import numpy as np
random_number =np.random.randint(low=1,high=100)
guess = 0

print('What is your name? ')
name = str(input())
print(f'Okay {name}, please guess a number from 1-100 :)')
guess=int(input())

while guess != random_number:
    print(f'Wrong! Correct number was {random_number}, please try again!')
    random_number =np.random.randint(low=1,high=100)
    guess = int(input())
    if guess > random_number:
        diff = guess - random_number
        print(f"You guessed bigger number! Difference is {diff}  Correct number was {random_number}, please try again! ")
        random_number =np.random.randint(low=1,high=100)
        guess=int(input())
    elif guess < random_number:
        print('You guessed lower num! Please try again.')
        random_number =np.random.randint(low=1,high=100)
        guess=int(input())
    else:
        print('Correct number!')

