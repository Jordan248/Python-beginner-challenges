#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

#Exercise 4 (and Solution)

#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input('Give us a number to divise: '))

for i in range(1,num):
    if num % i == 0:
        print (num, 'is divisble by', i)
i += 1    
