#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
#Exercise 3 (and Solution)

#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#ex3 + extra 1+2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    i += 1
    if i < 5:
        b.append(i)

print (b)

#extra 3
c = []
num = int(input('Give me a number: '))

for x in a:
    x += 1
    if x < num:
        c.append(x)

print ('New list with user input', c)
