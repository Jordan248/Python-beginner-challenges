#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# Fibonacci
#Exercise 13 (and Solution)

#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def get():
    userinput = int(input("Give us number to generate fibonacci: "))

#makes sure that input 0 and 1 creates an empty or the first part of fib   
    i = 1
    if userinput == 0:
        fib = []
        
    elif userinput == 1:
        fib = [1]

#using a while loop I can print out all the fib numbers. In the loop we add the last and second to last in the list to create fib numbers.
    elif userinput >= 2:
        fib = [1,1]
        while i < userinput - 1:
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
            
print (get())
                    
   # return userinput
