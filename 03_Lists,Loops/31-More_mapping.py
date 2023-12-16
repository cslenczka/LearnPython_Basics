"""
Create a function named increment_by_one that will multiply each number by 3.
Use the list map() function to run the increment_by_one function through each value in the list.
Store the new list in a variable named new_list and print() the new values.
"""
# def increment_by_one(x):
#     return x * 3
myNumbers = [23,234,345,4356234,243,43,56,2]

def increment_by_one(x):
    return x * 3

new_list = list(map(increment_by_one, myNumbers))
print(new_list)