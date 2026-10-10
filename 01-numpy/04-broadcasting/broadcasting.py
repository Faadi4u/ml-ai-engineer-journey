import numpy as np

## 1. Broadcasting With Scalar
    # Both shape must be same or on eof them have 1, For example : 
    # shape A: (3, 4) shape B: (4,)  here we have  (3,4)(1,4) means 3 = 1 and 4 = 4 it is compatible
    # What if (3,4)(4,4) here 3 = 4 is not equal while 4 = 4 is executable but we get an erro 3 is not equal to 4 it must should have 1 or 3 in opposite side

A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[2, 0], 
              [1, 3]])

## Is this is compatible? Yeah bcz both have (2,2)(2,2) so they are equal but what about that

A = np.array([1, 2, 4])
B = np.array([[2, 0], 
              [1, 3]])

## Is this is ? NOPE bcz A(1,3) B(2,2) so the 2 = 1 but 3 = 2 is the problem it shoulde be 1 or 3 then it wil be executable.


## 2. Broadcasting with scalar
    ## It is basically simple as heck, bcz here all the scalars would be worked simply without the shape rule

A = np.array([1, 2, 4])
scalar = A * 10
## scalar is basically consonant means the array rules doesn't apply on that. And it performed like basic arithmetic operation.
## Bcz scalar hasn't any dimensions



