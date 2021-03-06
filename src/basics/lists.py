'''
Lists are ordered sequences that can hold a variety of object type.
They use [] brackets and commas to separate objects in the list.
Lists support indexing nad slicing.
Lists can be nested
'''
my_list = [1, 2, 3]
my_list = ['STRING', 100, 23.33]
print(len(my_list))
mylist = ["ONE", "TWO", "TREE"]
print(mylist[0])
print(mylist[1:])
print(my_list + mylist)
print(my_list + my_list)
my_list[0] = "VALUE CHANGED"
print(my_list)
mylist.append("Appened")
print(mylist)
mylist.append("four")
print(mylist)
mylist.append("five")
print(mylist)
mylist.append("six")
mylist.append("seven")
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(4)
print(mylist)
new_list = ["two", "three", "four", "five"]
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
print(type(new_list))
my_sorted_list = new_list.sort()
print(my_sorted_list)
new_list.reverse()
print(new_list)
new_list.append("Appended")
# Build this list 0,0,0 two separate ways.
# Method 1:
l = [0, 0, 0]
print(l)
# Method 2:
ll = [0]*3
print(ll)
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)
# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)
