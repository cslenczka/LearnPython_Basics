#Update the map function to make it create a new list that contains the data types of each corresponding item from the original list.
# Use the type() function to get the data type.
# The new list should look like this:
# [<class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'str'>, <class 'int'>, <class 'int'>]
list_Strings = ['1','5','45','34','343','34',6556,323]
def prepender(x):
    return type(x)

new_list = list(map(prepender, list_Strings))
print(new_list)
