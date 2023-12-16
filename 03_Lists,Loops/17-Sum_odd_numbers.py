"""
Create a function called sum_odds that sums all the odd numbers in the arr variable.
Returns and print the result.
    You will need to declare an auxiliar variable outside the loop to keep adding the values.
    Create a function.
    You have to loop the list.
    On each loop, you have to ask if the value of the list in that index position is an odd number.
    If its odd then add the value to the auxiliar variable.
    An auxiliar variable is a regular variable, the only difference is a logical difference; an auxiliar variable is like a chosen one, 
    it'll be useful until it completes its purpose (add all the values, make a copy of a value, etc).
"""
arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]
print('The arr is: ' + str(arr))

def get_odds(sample_arr):
    odd_numbers = []
    for i in range(len(sample_arr)):
        if sample_arr[i] % 2 != 0:
            odd_numbers.append(sample_arr[i])
    
    return odd_numbers

print('The odds in arr are: ')
print(get_odds(arr))
odd_numbers = get_odds(arr)
print('**********')

def sum_odds(numbers):
    total = 0
    for i in numbers:
        total += i
    
    return total

print('The sum of all odds is: ')
print(sum_odds(odd_numbers))


