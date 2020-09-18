#https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
#Exercise 5 (and Solution)

#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []


for x in a:
    if x in b:
        if x not in c:
            c.append(x)

print ('Here is the the new list (no duplicates)', c)


#I don't know how to do extras. randint?
