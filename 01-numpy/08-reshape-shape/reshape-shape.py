import numpy as np


## Shape:

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr.shape)
print(arr.ndim)
print(arr.size)

## Output: 
# (6,)
# 1
# 6

##What does (6,) mean?
## The array has one dimension containing six elements.
##The comma matters: (6,) is a one-element tuple describing a 1D array's shape. It does not mean the array contains only one value.

## flatten(), ravel() and reshape(-1):

# Flatten:
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
flat = arr.flatten()

## Output: [1 2 3 4 5 6]
#flatten() always returns a copy.
#That means modifying flat will not change the original array's elements.
#.............................................................................................................................

# Ravel:
flat = arr.ravel()

# It also returns a flattened array, but it returns a view when possible and a copy otherwise
#..................................................................................................................................

# Reshape(-1):
flat = arr.reshape(-1)

## This reshapes the array into one dimension. Like ravel(), it may return a view or a copy depending on the layout.
#...................................................................................................................................................

## Reshape:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
## Shape is (2,3)

print(arr.reshape(3, 2))

# Output
# [[1 2]
# [3 4]
# [5 6]]
