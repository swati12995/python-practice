myis = [1, 2, 3]
myis.append(5)
myis.append(1)
print(myis)
myis.pop(4)
print(myis)
myis.sort()
print(myis)
print(help(myis.insert))
myis.insert(3, 0)
print(myis)
# def keyword
'''
Creating a function requires a very specific 
syntax,including the def kyword,correct indenttion and proper structure.
'''


def name_of_function():
    '''
        docstring explains function.
    '''
    print("hola")


name_of_function()


def name_of_function(name):
    print("Hello "+name)


name_of_function("Jose")

'''
Typically we use the return keyword to send back
the result of the function,instead of just printing it out
return allows us to assign the output of the function to a new variable.

'''


def add_function(num1, num2):
    return num1+num2


print(add_function(1, 2))


def say_hello():
    print("Hello")


say_hello()


def say_hello(name="Default name Nishu"):
    print(f"Hello {name}")


say_hello("Swati")
say_hello()
