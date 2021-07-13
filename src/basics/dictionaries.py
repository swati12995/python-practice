'''
Dictionaries are unordered mappings for storing objects.
dictionaries use a key-value pair.
The key-value pair allows users to quickly grab objects withit needing to know an index location
It uses curly braces and colons to signify the keys and their associated values.
{'key1':'value','key2':'value2'}
Dictionaries will be useful when we want to quickly pick a value without needing to know the exact index location
it can't be sorted
Dictionary is a built-in Python Data Structure that is mutable
'''
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])
dictio = {'1': 'First', '2': 'Second'}
print(dictio['1'])
dictio['3'] = 'Third'
print(dictio)
d = {'k1': [1, 2, 3]}
print(d['k1'][1])
'''
1. Do dictionaries keep an order? How do I print the values of the dictionary in order?
Dictionaries are mappings and do not retain order! If we do want the capabilities of a dictionary but we would like 
ordering as well, we can use the ordereddict object
'''
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key': 'hello'}
# Grab 'hello'
print(d['simple_key'])

dd = {'k1': {'k2': 'hello'}}
# Grab 'hello'
print(dd['k1']['k2'])

dst = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
# Grab hello
print(dst['k1'][0]['nest_key'][1][0])

ddd = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
# Grab hello
print(ddd['k1'][2]['k2'][1]['tough'][2][0])
