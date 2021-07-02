''' 
ordered sequence of characters, using either single quotes or double quotes:
'hello'
"hello"
we can use indexing and slicing to grab subsection
indexing notation: []
'''
print('hello')
print("hello")
print('This is also \n a string')
# print('' i'm going to run')
print("String \t Practice")
print(len("hello world"))
mystring = "Python Programming"
print(mystring[0])
print(mystring[8])
print(len(mystring))
print(mystring[-1])
print(mystring[-2])
print(mystring[-18])
print(mystring[1:])
print(mystring[-18:])
print(mystring[:6])
print(mystring[1:9])
print(mystring[::2])
print(mystring[::3])
print(mystring[2:18:2])
print(mystring[::-1])
name = "Nishu"
#name[0] = "P"
name = name[1:]
print(name)
#name = 'P' + name
print('P' + name)
x = "Hello World"
x = x + ' it is beautiful outside!'
print(x)
x = x + x
print(x)
letter = 'z'
#letter = letter * 10
letter *= 10
print(letter)
x = "Hello World"
x = x.upper()
print(x)
x = x.lower()
print(x)
x = x.split()
print(x)
x = "It it is a string practice program"
#x = x.split()
# print(x)
x = x.split('i')
print(x)
# Formatting with the .format() method
print("This is a string {}".format("INSERTED"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {0} {0} {0}".format("fox", "quick", "brown"))
print("The {f} {b} {q}".format(f="fox", b="brown", q="quick"))
# Float formatting follows "{value:width.precision f}"
result = 100/777
print(result)
print("The result {}".format(result))
print("The result was {r}".format(r=result))
print("The result is {r:10.3f}".format(r=result))
# print("The resut is ", result: 1: 3)
name = "Swati"
print("Hello, Her name is", {name})
print("Python rules!")
print('%s' % 'Python')
print('%s %s' % ('Python', 'rules!'))
