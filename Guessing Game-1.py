# This Project is called GUESSING GAME
# Coded by James Dumitru

import random
import time 

guessesTaken = 0 #starts at 0.
#Enter Name and welcome.
print('Hello! Welcome to the Guessing Game. Please Enter Your Name!')
myName = input()
#Random number between 1 and 20.
number=random.randint(1,20)
print('Hi '+ myName +'! I am thinking of a number between 0 and 20. Guess my number!')
#Character Error Part 1
while True:
    try:
        #10 guesses max, any more and you lose.
        while guessesTaken <10:
            print('Take a guess.') 
            guess=input()
            guess=int(guess)
        #For each guess taken add one
            guessesTaken=guessesTaken + 1
        #If too low, you get this message.
            if guess < number:
                print('Your guess is too low, try again.')
        #If too high, you get this message.
            if guess > number:
                print('Your guess is too high, try again.') 
        #If you guess the correct number you get good job and how many tries.
            if guess == number:
                guessesTaken = str(guessesTaken)
                print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
        #If you run out of guesses you get this message, with the correct number.
        if guess != number:
            number = str(number)
            print('Nope. The number I was thinking of was ' + number)
#Character Error Part 2           
        break        
    except ValueError:
         print("Sorry!  That was not a valid number.  Please try again...")
##### timer attempt #####

