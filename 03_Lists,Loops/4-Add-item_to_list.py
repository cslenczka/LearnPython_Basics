"""Add 10 random integers to the arr list.
We can use the above randint() method along with a for loop to generate a list of numbers. 
We first create an empty list and then append the random numbers generated to the empty list one by one.
"""
import random

my_list = [4,5,734,43,45]

def generate_random_numbers():
    for i in range(10): #can be 0,10
        new_numbers = random.randint(1,100)
        my_list.append(new_numbers)
        
    return my_list

print(generate_random_numbers())
print()
"""
We can also use the sample() method available in random module to directly generate a list of random numbers.
Here we specify a range and give how many random numbers we need to generate.
"""
my_list2 = [4,5,734,43,45]

def generate_with_sample():
    new_numbers = random.sample(range(0,100), 10)
    my_list2.append(new_numbers)
    return my_list2

print(generate_with_sample())


