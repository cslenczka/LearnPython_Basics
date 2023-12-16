"""
Please now create a function called generate_random that returns a random number between 0 and 9 every time it is called.

Print the result that the function call returns.
"""
import random

def generate_random():
    num1 = random.randint(0,9)
    return 'Random numbers between 0 and 9 is ' +str(num1)

print(generate_random())

"""
Change whatever you need to change to make the algorithm print random integers between 1 and 12.

This time use randrange()function.
"""
def generate_more_random():
    num2 = random.randrange(1,12)
    return 'Now generate random numbers between 1 and 12 using randrange(): ' +str(num2)

print(generate_more_random())