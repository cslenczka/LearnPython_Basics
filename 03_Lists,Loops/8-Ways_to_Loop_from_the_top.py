#Lets try looping from the end to the beginning.
# List of string
wordList = ['hi', 'hello', 'this', 'that', 'is', 'of']
print(wordList) 

#iterate over the wordList in reverse using while loop
# 1- Point i to the last element of the list 
i = len(wordList) - 1
# 2- Iterate til 1st element and keep on decrementing i
while i >= 0:
    print(wordList[i])
    i-=1
print('**********')
#iterate using for loop and range()
# 1- Suppose if wordList had n elements then  range( len(wordList) - 1, -1, -1) Will return list of numbers from n to 1
#For example, wordList had 5 elements then above specified range() function will return 4, 3, 2 , 1, 0
# 2- Now use that range() function in for loop and use random access operator [] to access elements in reverse i.e.
for i in range(len(wordList) -1, -1, -1):
    print(wordList[i])
print('**********')
#Iterate over the list using for loop and reversed()
#reversed() function returns an iterator to accesses the given list in the reverse order.
for i in reversed(wordList):
    print(i)
print('**********')
#Iterate over the list using List Comprehension and [::-1]
# 1- It will create a temporary revesed list
print(wordList[::-1])
[print (i) for i in wordList[::-1]]
print('**********')
#Iterate over the list using List Comprehension and reversed()
[print (i) for i in reversed(wordList)]