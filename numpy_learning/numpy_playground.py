import numpy as np

a = np.array([1, 2, 3])

print(a)

# multiply all elements by 2
print(a * 2)

# Generate the squareroot
b = np.array([9, 25, 100])
print(np.sqrt(b))

# Get an array of 6 random values, and then reshape it
c = np.arange(6)
print(c)
print(c.shape)
print(c.reshape(2, 3))
print(c.reshape(2, 3).shape)

print(np.zeros(10))
print(np.ones(5))

# Have to convert into a list if want to use?
zeros = np.zeros(5)
print(type(zeros))
print(zeros)

# Figure out how much memory the array takes up
print(a.dtype)

small = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], dtype='int16')
print(small.dtype)

print("Orig np-array is: ", a.itemsize, a.size * a.itemsize, a.nbytes)
print("Small np-array is: ", small.itemsize, small.size * small.itemsize, small.nbytes)

a1 = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a1)
print(a1.shape)
print(a1[1, 5])  # this is [row, column], so 13
print(a1[1, -2]) # also 13

# Get a specific row
print(a1[0, :])  # ':' is the slice like in a python list

# get 3rd column
print(a1[:, 2])

# Getting elements 1 - 5 of the first row skipping one at a time (every other)   [start_index:end_index:stepsize]
print(a1[0, 1:6:2])

# Can modify values
a1[1, 5] = 20
print(a1)

# can modify column (column gets all same value in this case)
a1[:, 2] = 5
print(a1)

# can modify column (give array of column size to set each to different value)
a1[:, 2] = [1, 2]
print(a1)

b1 = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
print(b1)
print(b1.shape)

# Gest specific element  (work outside in)
print(b1[0, 1, 1])

# Gest specific inner row  (work outside in)
print(b1[0, 1, :])
# returns "[3, 4]"

# Gest specific column  (work outside in)
print(b1[0, :, 1])
# return "[2, 4, 6, 8]"

# Gest all rows at same level  (work outside in)
print(b1[:, 1, :])
# Ends up being same as two above, but only because there is only one outermost "row"
# prints [[3 4]]