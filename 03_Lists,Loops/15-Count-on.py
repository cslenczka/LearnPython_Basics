"""
As you saw in the last exercise your list can be a mix types of data we are going to divide and conquer.
Would you be so kind to add all the items with data-type dict and list of the list named my_list into a new list named new_list?
    Loop the given list.
    Push the data-types dict and list found to a new list called new_list.
    Print the variable new_list.
"""
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
print('The list my_list is: ' + str(my_list))
print('**********')
new_list = []

for i in range(len(my_list)):
    if type(my_list[i]) == dict:
        new_list.append(my_list[i])
    elif type(my_list[i]) == list:
        new_list.append(my_list[i])
    

print('The new_list is: ' + str(new_list))
