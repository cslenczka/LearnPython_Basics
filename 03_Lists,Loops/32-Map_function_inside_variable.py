"""
The function stored in the variable prepender returns whatever is passed to it but prepended with the string: 'My name is:'.
Please map the names list using the prepender function to create a new list that looks like this:
"""
names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']
def prepender(x):
    return 'My name is: ' + x

new_list = list(map(prepender, names))
print(new_list)