"""
It is possible to find a list comprised of other lists (it is called a two-dimension list or matrix or nested list).
In this example, we have a list of coordinates that you can access by doing the following:
"""
coordinatesList = [[33.747252,-112.633853],[-33.867886, -63.987],[41.303921, -81.901693],[-33.350534, -71.653268]]
# funtion enumerate() returns a tuple with the index and the value of each item in the list
# here we return the second item of each list in the coordinatesList (the longitude)
print('The longitudes are:')
for item in coordinatesList:
    for index, value in enumerate(item):
        if index == 1:
            print(value)