#ml = [1, 2, 3, 4, 5, 6]
for num in range(10):  # generators
    print(num)
for num in range(0, 10, 2):
    print(num)

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

print(list(range(0, 11, 2)))


index_count = 0
word = 'abcdefg'
for letter in word:
    print(word[index_count])
    index_count += 1

# using enum
word = "qwertyuiop"
for i in enumerate(word):
    print(i)
# comments added
