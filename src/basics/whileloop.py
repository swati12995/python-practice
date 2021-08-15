'''
while loops will continue to execute a block of code while some condition remains true.
e.g. while my jug is not full,keep filling my jug with water.
or while my pet are still hungry,keep feeding them.
syntax:
while some_boolean_conditon:
    # do something
we can combine with an else statement
syntax:
while some_boolean_condition:
    # do something
else:
    # do something different

 break, continue,pass
 we can use break, continue and pass statements in oour loops to add additional funcionality for various cases.
 break: Breaks out of the current closest enclosing loop
 continue: Goes to the top of the closest enclosing loop
 pass:Does nothing at all
'''
a = 0
while a < 6:
    print("The value of a is", a)
    a = a+1
else:
    print("X is not less than 5")

x = [1, 2, 3]
for item in x:
    # comment
    pass
print("End of script")

mystring = 'Swati'
for l in mystring:
    if l == 'a':
        continue
    print(l)

for l in mystring:
    if l == 'a':
        break
    print(l)

n = 0
while n < 5:
    if n == 2:
        break
    print(n)
    n += 1
