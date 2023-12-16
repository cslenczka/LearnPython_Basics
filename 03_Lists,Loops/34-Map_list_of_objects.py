"""
At this time the function is printing the names only. Please update the mapping function so it creates a list where each item contains the following:
You have to get the age of each people based on their birthDate.
Search in Google "How to get the age of given birth date in python"
Inside your simplifier function you have to return a concatenation.
"""
import datetime

people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]

def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda x: 'Hello, my name is ' + x['name'] + ' and I am ' + str(calculateAge(x['birthDate'])) + ' years old', people))
print(name_list)