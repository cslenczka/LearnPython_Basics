# Create a function called lyrics_generator that receives a list. The list passed to the function will be something like this:
# [0,0,1,1,0,0,0]
# For each Zero you will add to the string Boom.
# For each One you will add to the string Drop the base.
# If you find the number 1 three times in a row, you should ALSO ADD to the string !!!Break the base!!!
# At the end you return the string.
# Example:
# lyrics_generator([0,0,1,1,0,0,0]) will return the string Boom Boom Drop the base Boom Boom Boom !!!Break the base!!!
# lyrics_generator([0,0,1,1,1,0,0,0]) will return the string Boom Boom Drop the base !!!Break the base!!!

def lyrics_generator(list):
    string = ""
    for num in list:
        if num == 0:
            string += "Boom "
        elif num == 1:
            string += "Drop the base "
    if "Drop the base Drop the base Drop the base" in string:
        string = string.replace("Drop the base Drop the base Drop the base", "!!!Break the base!!!")
    return string

print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))








