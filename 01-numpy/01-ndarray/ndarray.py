import numpy as np

# Creating 1D arrays
# 1D array means it has one dimension and only one axis and the output of this shoudl be in this format (7,)
# (7,) it means it has only 7 elements not rows and column in that.
arr_1d = np.array([12,3,4,5,6,7,17]);

# Creating 2D arrays
# 2D array means it has 2 dimensions and 2 axis, though its Example output should be (2,3). 2 is rows and 3 is column
# and also axis=0 is 2 and axis =1 is 3

arr_2d = np.array([[1,2,3,4],
                   [5,7,7,8]]);



# Creating 3D arrays
# 3d array have 3 dimensions and 3 axis. Example output -> (2,2,3)
# Here axis=0 is 2, axis=1 is 2 and axis=2 is 3. Basically the axis start from 0, thats why axis 1 is 0.

arr_3d = np.array([[[1,2,3,5,4,6],
                    [3,45,67,78,8,9]],
                   [[1,2,3,5,4,456],
                    [3,45,67,78,8,81]]])

# shape
# It basically tell us the shape of the array. Example: (2,3) it means it has 2 axis so it is 2D.
# and Also the 2 represent rows and 3 for columns

print(arr_3d.shape) # Output: (2,2,6) . It has 3 axis axis 0 is 2 , 1 is 2 and the 2 is 6.


# ndim
# Now this is the one who tells us the dimensions of the array. Like is it 1D,2D,3D or nD
print(arr_3d.ndim) # Output: 3. Bcz the shape of its is (2,2,6) or we can say it has 3 axis

# size
# Here we can find the size of array. It basically multiply the rows with coloumn and the result is the size.
# For example: (2,4). It has 2 rows and 4 columns, so 2x4 = 8 the size can be 8. 
# We can either add all the elements of that specific array
# for nDimension multiply all dimensions. Example (2,2,3,5) -> 2x2x3x5 = 60 is size
print(arr_1d.size) # output: 7

# dtype
# dtype tells us the data type of the array elements.
# int64 means 64-bit integer (8 bytes per element).
# int8 means 8-bit integer (1 byte per element).

print(arr_2d.dtype) 


# basic arithmetic
# It is Addition, Substration, Multiplication and more. The main things the numpy follows the BODMAS rule.
# It can be performed on both scalar or an array
# And also the operation is performed by element-wise For Example

data = np.array([1,2,3,4,4,56,5]) 
sum_scalar = data + 5 # here 5 is scalar and it will performed on all the element the output should be: [6,7,9,9,61,10]
sum_array = data + [1,2,3,4,6,7] # Output : Error, Why? Because the array that we are adding have 6 element while our data array is 7. So in array the element must be match in 1D or in nD.
sum_array_Final = data + [1,2,3,4,6,8,4] # Output is [2,4,6.8,12,64,9]. As you see it performed element wise even for array it is in numpy not in basic python. Thats the power of numpy. 
print (sum_array_Final)


