# function to return a list of numbers ending with 3

my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

def numbers_ending_with_3(numbers):
    return [num for num in numbers if num % 10 == 3]

print(numbers_ending_with_3(my_list))



