import numpy as np
## 1. Aggregation
## Aggregation means summarizing multiple values into one value, or a smaller array of summary values.

##Suppose you have exam scores:
scores = np.array([70, 80, 90, 60, 100])

## You want to know the average score, highest score, total, or spread of the scores.
print(np.sum(scores))    # 400
print(np.mean(scores))   # 80.0
print(np.min(scores))    # 60
print(np.max(scores))    # 100
print(np.std(scores))   # 14.142135...
## This process is often called a reduction because multiple values are reduced to a smaller result.

## 2. Axis

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [90, 95, 85]
])

## axis=0: aggregate down the rows - Means horizontally 
print(marks.mean(axis=0))
## Output should be: [76.66666667 83.33333333 83.33333333]

## It calculates the average for each subject:
# Math: (80 + 60 + 90) / 3
# Physics: (70 + 85 + 95) / 3
# CS: (90 + 75 + 85) / 3
# The original shape was (3, 3). The result shape is (3,).

# Why? Axis 0, the row dimension, has been aggregated away. The column dimension remains.

## axis=1: aggregate across the columns
print(marks.mean(axis=1))

## Output: [80. 73.33333333 90.]
# Now NumPy calculates one average per student:
# Student A: (80 + 70 + 90) / 3
# Student B: (60 + 85 + 75) / 3
# Student C: (90 + 95 + 85) / 3
# The output shape is again (3,), but the values mean something different.


## keepdims=True: preserve the reduced dimension
## Sometimes you want the aggregation result to retain the axis with a size of 1.

#Consider:
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

means = arr.mean(axis=0)

print(means)
print(means.shape)

##  Output: [25. 35. 45.]
#           (3,)

## With keepdims=True
means = arr.mean(axis=0, keepdims=True)

print(means)
print(means.shape)

##  Output: [25. 35. 45.]
#           (1,3)
# The aggregated axis remains, but its length becomes 1.