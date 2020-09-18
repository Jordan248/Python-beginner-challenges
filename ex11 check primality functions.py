#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#Check Primality Functions

#Exercise 11 (and Solution)

#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
#You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def prime():
    return int(input('Type a number and see if it is a prime number: '))

a = prime()
if a %% 2 == 0:
    print ('It is a prime number')
