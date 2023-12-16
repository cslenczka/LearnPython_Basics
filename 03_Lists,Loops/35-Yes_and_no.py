"""
Please use the list map functionality to loop the list of booleans and create a new list that contains the string 'wiki' for every 1 and 'woko' for every 0 that the original list had.
Print that list on the console.
You need to map the entire list.
Inside your mapping function you need to use a conditional to verify if the current value is 0 or 1.
If the current value is 1 you print the string 'wiki'.
If the current value is 0 you print the string 'woko'.
"""
theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
wiki_list = list(map(lambda x: 'wiki' if x == 1 else 'woko', theBools))
print(wiki_list)
