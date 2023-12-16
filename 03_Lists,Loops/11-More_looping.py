"""
Change the second item value to Steven.
Set the last position to Pepe.
Set the first element's value to the value of the 3rd element concatenated to the value of the 5th element.
Loop the list in reverse order (from the end to the beginning) and print all the elements.
"""
names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

print('names = ' + str(names))
names[1] = 'Steven'
names[-1] = 'Pepe'
names[0] = names[2] + names[4]
print('**********')
print('Reversed list is: ')

for i in range(len(names) -1, -1, -1):
    print(names[i])

print('**********')
i = len(names) - 1
while i >= 0:
    print(names[i])
    i -= 1

print('**********')
for i in reversed(names):
    print(i)