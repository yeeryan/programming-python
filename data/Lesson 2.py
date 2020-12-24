import numpy as np

data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print(data)

# class
print(type(data))
# data type
print(data.dtype)
# array shape
print(data.shape)

# Extract first entry
print('first value in data: ', data[0, 0])

# Extract middle value
print(data[30, 20])

# Slicing (First 10 columns, 4 rows)
print(data[0:4, 0:10])

# Excluding a starting value begins at 0

print(data[:3, 36:])

## Analyzing

print(np.mean(data))

# Setting functions
maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
print(maxval)
print(minval)
print(stdval)

# Creating new arrays from slices
patient_0 = data[0, :]
print(np.max(patient_0))

print(np.max(data[2, :]))

print(np.mean(data, axis=0))

#Other functions
import time
print(time.ctime())

# Stacking arrays
A = np.array([[1,2,3], [4,5,6], [7, 8, 9]])
print('A:')
print(A)

B = np.hstack([A, A])
print('B:')
print(B)

C = np.vstack([A, A])
print('C:')
print(C)

#Exercise
D = np.hstack((A[:, :1], A[:, -1:]))
print('D = ')
print(D)