#Change the value of those variables to make the loop print only the last half of the list.
#Change nothing but the value of those 3 variables!
my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

initialValue = 7
stopValue = len(my_list) - 1
increaseValue = 1

len_my_list = len(my_list)

print('my_list = ' +str(my_list))
print('The length of my_list is: ' + str(len_my_list))
print('**********')
for i in range(initialValue,stopValue):
    if i == my_list[i]:
        i += increaseValue
    print(my_list[i])