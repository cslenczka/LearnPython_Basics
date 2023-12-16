"""
Create a new variables named square_area1, square_area2, square_area3 and call the function calculate_area three times one for each square in the picture, for example:
Call the calculate_area function three times, one per each square, passing the length and edge of each square.
"""
def calculate_area(length,edge):
    return length * edge

square_area = calculate_area(5,10)

print(square_area)
print(calculate_area(5,10))