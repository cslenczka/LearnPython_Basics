"""
Write the code needed to print in the console all the numbers from 1 to 100.
For multiples of 3, instead of the number, print "Fizz".

For multiples of 5, print "Buzz".

For numbers which are multiples of both 3 and 5, print "FizzBuzz".
"""
def fizz_buzz():
    for i in range(0,20):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()