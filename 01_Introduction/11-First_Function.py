"""
Please, write all of your code inside the my_main_code function.

The function is_odd is defined at the beginning of the code, please call that function inside my_main_code passing it the number 45345 and print the result on the console.
"""
def is_odd(my_number):
    return (my_number % 2 != 0)

def my_main_code():
    return is_odd

print(is_odd(45345))