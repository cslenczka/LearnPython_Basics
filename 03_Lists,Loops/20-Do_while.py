"""
Print every iteration number on the console from 20 to 1, but concatenate an exclamation point to the output if the number is a multiple of 5.
At the end print() LIFTOFF.
"""

i = 21
while i > 1:
    i -= 1
    if i % 5 == 0:
        print(f'{i}!')
    else:
        print(i)

print('LIFTOFF')