# Create a matrix 1's based on a parameter.
# Create a function called matrixBuilder, which will expect 1 parameter (an integer):
#  This number represents the amount of rows and columns for the matrix.
#  Example: 5 means that the matrix should be 5x5.
# This function should return a list of lists that represents the matrix.
# All of the values should be 1.
# Example: matrixBuilder(3) should return:
# [ [1,1,1,1,1],
#   [1,1,1,1,1],
#   [1,1,1,1,1], ]


def matrixBuilder(num):
    matrix = []
    for i in range(num):
        matrix.append([1] * num)
    return matrix

print(matrixBuilder(3))

# Another way to do it using a nested loop:
def matrixBuilder(num):
    matrix = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(1)
        matrix.append(row)
    return matrix

print(matrixBuilder(3))

# Another way to do it using list comprehension 1:
def matrixBuilder(num):
    return [[1] * num for i in range(num)]

print(matrixBuilder(3))

# Another way to do it using list comprehension 2:
def matrixBuilder(num):
    return [[1 for i in range(num)] for j in range(num)]

print(matrixBuilder(3))

# Another way to do it using list comprehension 3:
def matrixBuilder(num):
    return [[1] * num] * num

print(matrixBuilder(3))