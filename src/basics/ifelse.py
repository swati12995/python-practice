'''
To control the flow of logic we use some keywords:
if
elif
else
* syntax of an if statement
if some_condition:
    #execute some code

* syntax of an if/else statement
if some_condition:
    #execute some code
else:
    #do something else
 *syntax f an if/else statement
if some_condition:
     #execute some code
elif some_other_conditon:
    # do something different
else:
    #do something else
'''
if True:
    print('Its true')
if 3 > 2:
    print("3 is greater")
hungry = False
if hungry:
    print("Feed me")
else:
    print('Not Hungry')
loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "showroom":
    print("Welcome to the store")
else:
    print("I do not know much")
name = "Samy"
if name == "Franki":
    print("Hello Franki")
elif name == "Samy":
    print("Hello Samy")
else:
    print("what is your name")
