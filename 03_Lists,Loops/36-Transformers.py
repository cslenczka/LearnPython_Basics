# Declare a new function called data_transformer() that receives a list as parameter.
# The function should return a list of strings containing the full name of each user using the map() method.

incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

def data_transformer(data):
    return list(map(lambda x: f'{x["name"]} {x["last_name"]}', data))

print(data_transformer(incoming_ajax_data))