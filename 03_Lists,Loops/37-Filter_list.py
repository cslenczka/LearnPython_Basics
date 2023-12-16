# Another looping function that is available on python is the filter() function
# Please update the filtering function so it filters all the numbers bigger than 10.
allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]

def filterNumbers(number):
    return number > 10

filteredNumbers = list(filter(filterNumbers, allNumbers))
print(filteredNumbers)