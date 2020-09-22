#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#Check Primality Functions

#Exercise 11 (and Solution)

#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
#You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
#functions too hard, had to look at solutions for ideas

num = int(input('Give us a number to check if prime: '))
primecheck = range(2, num)

for x in primecheck:
    if num % x != 0:
        continue
    else:
        print (num, 'is not a prime number')
        exit()

print (num, 'is a prime number')



## tried to use a def prime, but it was too hard
# def prime(): int(input(Number here:)) 

#for x in range(2, (get_num / 2), + 1):
#    if x % prime == 0:
#        print (x)


#if a % 2 == 0:
 #   print ('It is a prime number')

#print (prime(2))
