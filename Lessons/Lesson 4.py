# Repeating Actions with loops
# Basic loop

word = 'lead'
for char in word:
    print(char)

length = 0
for vowel in 'aeiou':
    length = length + 1
print('There are', length, 'vowels')

# Loop vars are only used ot record progress in a loop
letter = 'z'
for letter in 'abc':
    print(letter)
print('after the loop, letter is', letter)

# Length function
print(len('aeiou'))

# Exercises
for number in range(1,4):
    print(number)

outcome = 1
for number in range(0, 3):
    outcome  = outcome * 5
print(outcome)

newstring = ''
oldstring = 'Newton'
for char in oldstring:
    newstring = char + newstring
print(newstring)

y = 0
for idx, coef in enumerate(coefs):
    y = y + coef * x ** idx