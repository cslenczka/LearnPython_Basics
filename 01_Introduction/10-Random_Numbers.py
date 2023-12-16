#The code now is returning random decimal numbers, please update the function code to make it return an integer (no decimal) number between 1 and 10.

import random

def get_randomInt():
    random_number = random.randint(1,10)
    return random_number

print(get_randomInt())