my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

print('The list is: ' + str(my_list))
# with this function we can find the average value of a list of numbers using the sum() and len() functions
def find_average(numbers):
    return sum(numbers)/len(numbers)

print('The average value of the list is: ' + str(find_average(my_list)))
print('**************************************')
# with the following function we can find the average value of a list of numbers using a for loop
def find_average_for(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

print('The average value of the list is: ' + str(find_average_for(my_list)))
print('**************************************')
# with the next function we can find the average value of a list of numbers using a while loop
def find_average_while(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total/len(numbers)

print('The average value of the list is: ' + str(find_average_while(my_list)))