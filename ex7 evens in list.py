#https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
#List Comprehensions
#Exercise 7 (and Solution)

#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

print ('Only evens in this list:', a)

for i in a:
    if i % 2 == 0:
        b.append(i)

print (b)

