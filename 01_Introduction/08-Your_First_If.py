"""
If the user has more than $100, we answer: "Give me your money!".

If the user has more than $50, we answer: "Buy me some coffee you cheap!".

If the user has less or equal than $50, we answer: "You are a poor guy, go away!".
"""
total = int(input('How much money do you have in your pocket?\n'))

if total > 100:
    print("Give me your money!")
elif total > 50:
    print("Buy me some coffee you cheap!")
else:
    print("You are a poor guy, go away!")