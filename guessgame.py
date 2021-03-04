# This is a guess the number game.
import random

name = input ('Hello. What is your name?: ')

print ('Well, ', name, ', I am thinking of a number between 1 and 20')
secretNumber = random.randint (1, 20)

for guessesTaken in range (1, 7):
    print ('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print ('Your guess is to low.')
    elif guess > secretNumber:
        print ('Your guess is to high.')
    else:
        break

if guess == secretNumber:
    print ('Good job, ', name, '! You guessed my number in ', guessesTaken, ' guesses!')
else:
    print ('The number i was thinking of was ', secretNumber)
