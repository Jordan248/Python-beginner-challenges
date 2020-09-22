#https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# List Ends
#Exercise 12 (and Solution)

#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
#For practice, write this code inside a function.

import random

randomlist = random.sample(range(30),30)
newlist = []

print (randomlist)

def firstlast(x):
    newlist = [x[0],x[-x]]
    return newlist

x = firstlast(randomlist)
print (x)

#new = [l[0],l[-1]]
 #   return new
