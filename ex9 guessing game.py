#https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
#Guessing Game One

#Exercise 9 (and Solution)
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#(Hint: remember to use the user input lessons from the very first exercise)

#Extras:
#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
random = random.randint(1,9)
count = 0
guess = 0


while input != 'exit' and int(guess) != random:
    count += 1
    guess = input('Guess a number between 1-9 (type exit if you want to leave):')
    if guess == 'exit':
        print('Game is now exiting')
        break
    
   
    if int(guess) > random:
        print('You guessed higher')
        continue
    elif int(guess) < random:
        print('You guessed lower')
        continue
    elif int(guess) == random:
        print('Nice you guessed correctly :)')
        print ('The number was', random, 'it took you',count, 'tries')
        break
    

#print(random)
