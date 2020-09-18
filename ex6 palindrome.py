#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#Exercise 6 (and Solution)
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = str(input('Give me a word: '))

if string == string[::-1]:
    print('Ya it is a palindrome')
else:
    print('Nope not palindrome')
    
