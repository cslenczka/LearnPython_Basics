"""
Import random function at the beginning of the file.
Create a variable named the_last_one, and assign it the LAST element of my_stupid_list.
Print the_last_one to the console.
"""
import random

def generate_random_list():
    aux_list = []
    randomLength = random.randint(1, 100)

    for i in range(randomLength):
        aux_list.append(i)
        i += i
    return aux_list

my_stupid_list = generate_random_list()
print(my_stupid_list)
print(len(my_stupid_list))
the_last_one = my_stupid_list[-1]
print(the_last_one)