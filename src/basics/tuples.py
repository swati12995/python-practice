'''
Tuples are very similar to list,te key difference is the - immutability
once an element is inside a tuple, it can not be reassigned.
Tuples use parenthesis:(1,2,3)
Python has two built-in methods that you can use on tuples.
count()
index()
'''
t = (1, 2, 3)
mylist = [1, 2, 3]
print(type(t))
print(type(mylist))
t = ('one', 2)
print(t)
print(t[-1])
t = ('a', 'a', 'b', 'b', 'b')
print(t.count('a'))
print(t.count('c'))
mylist[0] = 'New'
print(mylist)
# t[0] = 'New'   #  this assignnent will throw an  as TypeError: 'tuple' object does not support item assignment
print(t)
