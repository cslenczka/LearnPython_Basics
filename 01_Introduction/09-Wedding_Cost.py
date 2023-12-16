"""
Complete the algorithm that prompts the user for the number of people attending their wedding and prints the corresponding price in the console.
Extend the given code on the left to cover all possible ranges of guests.
Make sure that your code correctly calculates and prints the price in the console based on the user's input.
# of guests	price
Up to 50 people	$4,000
Up to 100 people	$10,000
Up to 200 people	$15,000
More than 200 people	$20,000
"""
user_input = int(input('How many people are coming to your weddding?\n'))

if user_input <= 50:
    price = 4000
elif user_input <= 100:
    price = 10000
elif user_input <= 200:
    price = 15000
else:
    price = 20000


print('Your wedding will cost $' +str(price)+' dollars')