#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
#Exercise 8 (and Solution)

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock

a = ['rock', 'paper', 'scissors']

while True:
    start = input('Play a game? (input anything to start type n to stop): ')
    if start == 'n':
        print ('Game over')
        break
    else:
        num1 = str(input('Player 1 choose rock paper scissors:'))
        num2 = str(input('Player 2 choose rock paper scissors:'))
        
#Tried to make code below to work as extra to check if the inputs are spelt correctly. but something is wrong.
#    if num1 != 'rock' or num1 != 'paper' or num1 != 'scissors' or num2 != 'rock' or num2 != 'paper' or num2 != 'scissors':
#        print('type it properly silly')
#    else:

        if num1 == 'rock' and num2 == 'scissors' or num1 == 'paper' and num2 == 'rock' or num1 == 'scissors' and num2 == 'paper':
            print('Player 1 has won with', num1)
        elif num1 == num2:
            print('A draw')
        else:
            print('Player 2 has won with', num2)


