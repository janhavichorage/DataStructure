# Number Guessing Game

import random
number = random.randint(1, 20)
guess = int(input("Guess a number (1-20): "))
if guess == number:
    print("Correct! You won!")
else:
    print("Wrong guess!")
    print("The number was:", number)
print("Game over!")