import numpy as np

# 1. Arithmetic and comparisons
  ## In Numpy therer is basically an element-wise operations.
  ## And make sure when adding array with array make sure there shape would be match. Otherwise you get an error.

 ## Scalar Arithmetic - "+" , "-", "*" , "/" , "**":


scalar_arth = np.array([12,35,46,79,7,78,9]);
addition = scalar_arth + 10 ## Here 10 is scalar , And also it will be added to each elemenet bcz it is element-wise.
Substract = scalar_arth - 4  # Output is : [ 8 31 42 75  3 74  5]
Multiply = scalar_arth * 3
divide = scalar_arth / 2
Square  = scalar_arth ** 2

print(addition,Multiply,Substract,divide,Square);


 ## Element-wise comparison: > , < , >= , <= , == , !=

scalar_arth = np.array([1,35,46,79,7,78,9]);
GreaterThan = scalar_arth > 10 ## Here 10 is scalar , The answer will be in boolean and also it is in element-wise.
LessThan = scalar_arth < 4  # Output is : [ True False False False False False False ]
GreaterThanEqual = scalar_arth >= 3
LessThanEqual = scalar_arth <= 2
Equal  = scalar_arth == 2
NotEqual = scalar_arth != 3

print(GreaterThan,GreaterThanEqual,LessThan,LessThanEqual,Equal,NotEqual)

#...............................................................................................................................

# 2. Matrix multiplication ( @ )
    # It is basically dot/matrix product in mathematic term.
    # It combines rows from the first matrix with the columns of the second matrix.
    # In this the column of first matrix must be matched with the rows of second matrix.

A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[2, 0], 
              [1, 3]])

print(A @ B ) # The output is calculated liek that : (1x2 + 2x1) (1x0 + 2x3) =   [4   6
                                                    #(3x2 + 4x1) (3x0 + 4x3) =    10  12]

#....................................................................................................................

# 3. Vectorization:
  # It is refers to aplly or perform arithmetic operation on an array at once instead of using python loops( For or while )
  # it is faster bcz as the array data type saved in a single block of memory so it is easy to perform any operation on that dtype of array which is..
  # way faster than python bcz python datatype of an array scattered on the memory so they explicitly do across all the elemsnts which is way more time consuming 
  # for largest dataset liek we just use as an example below:
   

arr = np.arange(1000000)
result = arr * 2  # No loop required!
print(result)
