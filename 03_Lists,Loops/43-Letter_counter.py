# Create a function that takes a string and returns a dictionary with the count of each letter that is in the string.
# Capitalization should not affect the count
# Spaces should be ignored!

par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

def letter_counter(paragraph):
    letter_count = {}
    for letter in paragraph:
        if letter == " ":
            continue
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

print(letter_counter(par))

# Same as above but including spaces

def letter_counter(paragraph):
    letter_count = {}
    for letter in paragraph:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

print(letter_counter(par))