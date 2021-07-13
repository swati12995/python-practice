'''
Reading Writing, Appending Modes
mode='r' is read only
mode='w' is write only(overwrite files or create new)
mode='a' is append only(will add to the end of the file)
mode='r+' isreading and writing
mode='w+' is writing and reading(overwrites existing filles or creates a new file)

'''
myfile = open('myfile.txt')
#myfile = open('wrongfile.txt')
print(myfile.read())
myfile.seek(0)  # this will put the cursor to the beginning of the file

print(myfile.read())
myfile.seek(0)
print(myfile.readlines())  # list- where each element represents a line
print(myfile.close())
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)
with open('myfile.txt', mode='w+') as myfile:
    contents = myfile.read()
file = open('geeky.txt', 'w')
file.write("This is write command. \n")
file.write("Contents have been written to the file.\n ")
file.close()
file = open('geeky.txt', 'a')
file.write("Appended contents. \n")
file = open('geeky.txt', 'r')
print(file.read())
file.close()
with open('my_new_file.txt', 'r') as f:
    print(f.read())
