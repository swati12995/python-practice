'''
Booleans are operators that allow to convey True
or False
theseare important when we deal with control flow and logic

'''
print(1 > 2)
print(1 == 1)
print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(4**0.5 != 2)
print(3 == 3.0)

# What is the boolean output of the cell block below?
# two nested lists
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
# True or False?
print(l_one[2][0])
print(l_two[2]['k1'])
print(l_one[2][0] >= l_two[2]['k1'])
