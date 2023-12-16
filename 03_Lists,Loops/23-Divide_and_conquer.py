"""
Create a function called merge_two_list that expects an list of numbers (integers).
Loop through the list and separate the odd and the even numbers in different lists.
If the number is odd number push it to a placeholder list named odd.
If the number is even number push it to a placeholder list named even.
Then concatenate the odd list to the even list to combine them. Remember, the odd list comes first and you have to append the even mergeTwoList.

Create empty (placeholder) variables when you need to store data.
Expected result:
mergeTwoList([1,2,33,10,20,4])
[[1,33,2], [10,20,4]]
"""
# 24-Create a function called merge_two_list that expects an list of numbers (integers).
list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

def merge_two_list(sample_list):
    odd = []
    even = []
    for i in sample_list:
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)

    return odd, even

print(merge_two_list(list_of_numbers))


