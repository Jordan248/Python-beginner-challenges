#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Exercise 1 (and Solution)
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = str(input('Name: '))
age = int(input('Age: '))
num = int(input('Print how many copies: '))
newage = 100 - age

for x in range(num):
    x += 1
    print(name, 'will be 100 in', newage)
