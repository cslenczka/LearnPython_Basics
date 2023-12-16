"""
Create a function named maxInteger
This function should take a list as an input parameter and return the maximum number found in the list.
You should use a 'for' loop to iterate through the list.
Use the print() function to print what the function returns when it is called.
"""
my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

def maxInteger(sample_list):
    max = 0
    for i in sample_list:
        if i > max:
            max = i
    return max

print(maxInteger(my_list))