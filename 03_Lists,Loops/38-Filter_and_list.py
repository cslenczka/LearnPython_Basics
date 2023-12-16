# Complete the code to make it fill the resulting_names list with only the names that start with letter R.
# Use the filter() function.

all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

def filter_names(name):
    return name[0] == "R"

resulting_names = list(filter(filter_names, all_names))
print(resulting_names)

# same as above but with lambda and startswith()
resulting_names = list(filter(lambda name: name.startswith("R"), all_names))
print(resulting_names)