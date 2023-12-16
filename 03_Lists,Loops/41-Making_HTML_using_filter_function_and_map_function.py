# Create generate_li and filter_colors function to make the exercise print the following HTML with only the sexy colors:
# Maybe you have to use filter() and map() function
all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

def generate_li(color):
    return f"<li>{color['label']}</li>"

def filter_colors(color):
    return color["sexy"] == True

sexy_colors = list(filter(filter_colors, all_colors))
print(sexy_colors)
sexy_colors = list(map(generate_li, sexy_colors))
print(sexy_colors)

# same as above but with lambda
sexy_colors = list(filter(lambda color: color["sexy"] == True, all_colors))
sexy_colors = list(map(lambda color: f"<li>{color['label']}</li>", sexy_colors))
print(sexy_colors)