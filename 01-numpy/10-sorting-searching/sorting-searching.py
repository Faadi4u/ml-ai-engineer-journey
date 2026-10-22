import numpy as np
## Sorting: How do I arrange data into a useful order?
## Searching: How do I find a value, locate its position, or identify elements that match a condition?


## Sorting: np.sort() vs sort():

## np.sort() - It makes a copy and sort it not the original array
scores = np.array([0.72, 0.35, 0.91, 0.64, 0.83])
sorted_scores = np.sort(scores)

print(sorted_scores)
# [0.35 0.64 0.72 0.83 0.91]

print(scores)
# [0.72 0.35 0.91 0.64 0.83]


## sort()- It changes the original dataset
scores.sort()

print(scores)
# [0.35 0.64 0.72 0.83 0.91]

## Descending Sort - As np.sort() sort in ascending order by default for descending we have to use [::-1] ...
# It basically reverse the array as we already do that in slicing
  
scores = np.array([72, 35, 91, 64, 83])

ascending = np.sort(scores)
descending = np.sort(scores)[::-1] ## Here :: set the all rows and columns and -1 set the step backwards(Reverse array) 

print(ascending)
# [35 64 72 83 91]

print(descending)
# [91 83 72 64 35]

## Sorting along Axis:
arr = np.array([
    [90, 10, 80],
    [30, 70, 20]
])
print(np.sort(arr, axis=1))

# axis=1 sorts horizontally across each row, and axis=0 will be sort that vertically top to bottom 

## Argsort():

import numpy as np
scores = np.array([0.72, 0.35, 0.91, 0.64])
sample_ids = np.array(["S1", "S2", "S3", "S4"])

order = np.argsort(scores)[::-1]

print(sample_ids[order])
# ['S3' 'S1' 'S4' 'S2']

print(scores[order])
# [0.91 0.72 0.64 0.35]
# This ranks the samples from highest score to lowest.


##..............................................................................................................................................................



## Searching: 
# Find matching values with Boolean conditions

scores = np.array([45, 78, 91, 62, 91, 35])

print(scores == 91)
# [False False  True False  True False]
print(scores[scores == 91]) ## Get all the 91 matches in the array and it return all the values
# [91 91]


# np.where()  locate matching positions
# Suppose you need the positions of every score equal to 91.

scores = np.array([45, 78, 91, 62, 91, 35])

indices = np.where(scores == 91)

print(indices)
# (array([2, 4]),)

## You can choose between two resulst:

scores = np.array([45, 78, 91, 62])

labels = np.where(scores >= 60, "pass", "fail")
# Here, np.where(condition, value_if_true, value_if_false) makes an element-wise choice.
print(labels)
# ['fail' 'pass' 'pass' 'pass']