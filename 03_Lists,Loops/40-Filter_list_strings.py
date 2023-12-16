# Given a list of names called names please create a function that filters the list with only the names that contain the given string.
# The given string is 'am'
# The search should NOT be Case Sensitive.
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']

def filterNames(name):
    return 'am' in name.lower()

filteredNames = list(filter(filterNames, names))
print(filteredNames)

# same as above but with lambda and startswith()
filteredNames = list(filter(lambda name: 'am' in name.lower(), names))
print(filteredNames)

# same as above but with list comprehension
filteredNames = [name for name in names if 'am' in name.lower()]
print(filteredNames)

