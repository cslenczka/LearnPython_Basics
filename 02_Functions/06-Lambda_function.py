"""
A lambda function is a function with just one line of code and no name.
Lambda fuctions have to be always very small.
Lambda function can only have one line.
Lambda function doesn't need a return statement (it is assumed that it will return whatever is on that one line).
Lambda functions can be stored in variables or passed as parameters to another function

Create a variable called is_odd.
Assign a lambda function to it that returns True or False if a given number is odd.
"""
is_odd = lambda n : True if n % 2 != 0 else False
print(is_odd(10))
