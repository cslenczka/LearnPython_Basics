"""
Create a variable new_list.
Using a loop, invert the arr list.
Append the result loop into the new_list variable.
With the print() function output in the console the result that you have.
"""
arr = [45, 67, 87, 23, 5,  32, 60]

print('initial list: ' + str(arr))

new_list = []

for i in range(len(arr) -1, -1, -1):
    new_list.append(arr[i])
    
print('final list: ' + str(new_list))