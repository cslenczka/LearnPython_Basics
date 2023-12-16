"""
create a function that takes a list of numbers and returns only the numbers that are 3 digits long.
"""
# The abs() function returns the absolute value of the specified number.

my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]
def get_three_digit_numbers(numbers):
    return [num for num in numbers if 100 <= abs(num) < 1000]

print(get_three_digit_numbers(my_list))