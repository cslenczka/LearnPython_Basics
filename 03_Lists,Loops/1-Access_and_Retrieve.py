"""
Every list has the following parts:
    Items: are the actual values inside on each position of the list.
    Length: is the size of the list, the number of items.
    Index: is the position of an element.
To access any particular item within the list you need to know its index (position).
The index is an integer value that represents the position in which the element is located.
🔎 Important:
Every list starts from zero (0)! So to get the first item we'd use my_list[0]
📝 Instructions:
    Using the print() function, print the 3rd item from the list.
    Change the value in the position where Thursday' is located to None.
    Print the particular position of the step two.
"""
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# 1. print the item here
print('The original list is: ' + str(my_list))
print(my_list[2])
# 2. change the position were 'thursday' is to None
my_list[4] = 'None'
print(my_list)
# 3. print that position now here
print(my_list[4])





