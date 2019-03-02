# This Project is called GUESSING GAME
import random

guesses Taken=0

print('Hello! Welcome to the Guessing Game. Guess my number!')

number=random.randint(1,20)
print('I am thinking of a number between 0 and 20.')

while guessesTaken <5:
    print('Take a guess.') 
    guess=input()
    guess=int(guess)

    guessesTaken=guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
         print('Your guess is too high.')

    if guess == number:
         break  

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)