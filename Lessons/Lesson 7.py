# Making Choices

## Conditionals
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')

# No else

num = 53
print('before conditional')
if num > 100:
    print(num,' is greater than 100')
print('...after conditional')

#Multiple branches with elif

num = -3
if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is negative')

# AND OR
if (1 > 0) and (-1 >= 0):
    print('both parts are true')
else:
    print('at least one part is false')

if (1 > 0) or (-1 >= 0):
    print('at least one part is true')
else:
    print('at least one part is false')

# Checking Data

import numpy
