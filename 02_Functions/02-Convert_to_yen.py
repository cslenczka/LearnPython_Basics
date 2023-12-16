"""
For example, in this particular case we have two functions available:

dollar_to_euro: that calculates the value in euros of a given value in dollars.
euro_to_yen: calculates the value in yen of a given value in euros.

📝 Instructions:
Using the two functions available, print on the console the value of 137 dollars in yen.
Our expected value is in yen.
Our available function euro_to_yen will provide that.
To get to euro we will use the available function dollar_to_euro.
"""
def dollar_to_euro(dollar_value):
    return dollar_value * 0.89

def euro_to_yen(euro_value):
    return euro_value * 124.15

total = dollar_to_euro(137)
print(euro_to_yen(total))