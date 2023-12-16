"""
Write a function that merges two list and returns a single new list (merge_list) merging all the values of both lists.

Declare an empty list.
Loop the two list.
Concatenate the result in an empty lists.
Print the variable with two list.
"""
chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']

def merge_list(list1,list2):
    new_list = []
    for i in (list1,list2):
        for j in i:
            new_list.append(j)
    
    return new_list

print(merge_list(chunk_one,chunk_two))