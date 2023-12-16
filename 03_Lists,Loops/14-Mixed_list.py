#Write a function to programmatically print in the console the types of the values that the list contains in each position.
#You can use the for loop.
mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
print('The list is: ' + str(mix))
print('**********')

for i in mix:
    print(type(i))