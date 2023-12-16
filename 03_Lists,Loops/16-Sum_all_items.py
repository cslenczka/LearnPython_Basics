"""
Complete the code of the function sum so that it returns the sum of all the items in my_sample_list.
You have to loop the entire list and add the value of each item into the "total" variable.
"""
my_sample_list = [3423,5,4,47889,654,8,867543,23,48,5345,234,6,78,54,23,67,3,6,432,55,23,25,12]
print('my_sample_list is: ' + str(my_sample_list))

def sum_all_values(sample_list):
    total = 0
    for i in sample_list:
        total += i
    return total

print('The sum of all values in my_sample_list is: ' + str(sum_all_values(my_sample_list)))
