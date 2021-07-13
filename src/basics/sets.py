'''
Sets are unordered collections of unique elements.
meaning there can only be one representative of the same object.
A set is an unordered collection of items. 
Every set element is unique (no duplicates) and must be immutable (cannot be changed). 
However, a set itself is mutable. We can add or remove items from it
'''
myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, ]
set(mylist)
print(set(mylist))
strg = 'Mississippi'
set(strg)  # remove the repeated characters of string and convert it to a set
print(set(strg))
print(set([1, 1, 2, 3]))
# Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
list5 = set(list5)
print(list5)
