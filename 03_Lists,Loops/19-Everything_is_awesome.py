"""
Compare the item if it is 1 push the number to the list new_list.
Compare the item if it is 0 push Yahoo to the list new_list (instead of the number).
"""
my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def everything_awesome(sample_list):
    new_list = []
    for i in range(len(sample_list)):
        if sample_list[i] == 0:
            new_list.append('Yahoo')
        else:
            new_list.append(sample_list[i])
    
    return new_list

print(everything_awesome(my_list))

print('********')

def awesome(sample_list):
    second_list = []
    for i in sample_list:
        if i == 0:
            second_list.append('Yahoo')
        else:
            second_list.append(i)
    return second_list

print(awesome(my_list))
