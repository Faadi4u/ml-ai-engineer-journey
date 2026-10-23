import numpy as np

# Element-wise multiplication and Matrix multiplication		

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [10, 20],
    [30, 40]
]);

print(A * B)
# It should be multiplied like this in Element Wise:
# 1 × 10 = 10
# 2 × 20 = 40
# 3 × 30 = 90
# 4 × 40 = 160 

print(A @ B) 
# output: 
# [[ 70 100]
#  [150 220]]

# It should be multiplied like this in Matrix multiplication:

## Rows of A with coloumn of B:
# For the first row:
#   (1 x 10) + (2 x 30) = 70
#   (1 x 20) + (2 x 40) = 100
## The remaining values are calculated like the same way.
## The number of elements in both shoudl be same...


#..............................................................................................................................................


# Dot product
# A dot product multiplies corresponding vector elements and then sums the products.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))
# Output: 32

#................................................................................................................................

# Transpose	

# Transposing exchanges the axes of a matrix.
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])


print(A.shape)    # (2, 3)
print(A.T.shape)  # (3, 2)



