"""
The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
The syntax of map() is: map(function, iterable, ...)
map() Parameter:
    function: passes each item of the iterable to this function.
    iterable: iterable which is to be mapped. You can pass more than one iterable to the map() function.
"""
# The formula is: F = 1.8 * C + 32 (where C is the Celsius value) and the list is: celsius = [0, 10, 15, 32, -5, 27, 3]
# Expected output: [32.0, 50.0, 59.0, 89.6, 23.0, 80.6, 37.4].
print('Using the map() function: ')
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = list(map(lambda c: 1.8 * c + 32, celsius))
print(fahrenheit)
print('-----------------------------')
# Using the same logic, add the needed code to convert a list of Celsius values into Fahrenheit inside the map() function after having defined the function fahrenheit() that converts a single Celsius value into Fahrenheit.
celsius_values = [-2,34,56,-10]
def fahrenheit(c):
    return 1.8 * c + 32

fahrenheit_values = list(map(fahrenheit, celsius_values))
print(fahrenheit_values)