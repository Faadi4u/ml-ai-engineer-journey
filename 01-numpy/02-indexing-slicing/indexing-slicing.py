import numpy as np

## What is indexing? 
## It is basically used to get the specific chunk/element from the array
## For example: [1,2,3,4,5,78,5] -> we want to get 5 from that array so :

arr_index = np.array([1,2,3,4,5,78,5])
sum_array = arr_index + [1,2,3,4,6,7,5]
result = arr_index[4]
print(result) # output -> would be 5 

## 2D array indexing

arr_2d = np.array([[1,2,3,4],
                   [5,7,7,8]]);

print(arr_2d[1,3]) ## getting 8 from the second row
print(arr_2d[:, 2]) ## Getting all rows by using (:) the output should be (3 7) 
print(arr_2d[1,]) ## getting 2nd array


## 3D array indexing

arr_3d = np.array([[[1,2,3,5,4,6],
                    [3,45,67,78,8,9]],
                   [[1,2,3,5,4,456],
                    [3,45,67,78,8,81]]])

print(arr_3d[1,0,5]) ## Gettingthe 2nd group 1st row 456 element. 

## -----------------------------------------------------------------------------------------------

## Slicing
## what is slicing?
## It is basically different from indexing in this we can set the range to get elements
## In which we have start and stop, Start is included and stop is exluded
## For example:
slicing_arr = np.array([1,2,3,98,4,5,56,66]) 
print(slicing_arr[3:7]) ## Getting the elements from 98 to 56, here (3:7) is the range 7 is 66 but as we say last one is excluded thats how it stop at 56.

## 2D array 
arr_2d_slcing = np.array([[1,2,3,4],
                          [5,7,7,8]]);

print(arr_2d_slcing[:,2:4]) ## Lets get the 2nd square (3,4,and 7,8)

## Start : Stop : Step

# 1. [:] - Select entire array
array = np.array([1,2,4,45,56])
print(array[:]);

# 2. [start:] sum_array = data + [1,2,3,4,6,7]- Select from start to the end
array_2 = np.array([1,2,34,78,45,56,])
print(array_2[2:]);

# 3. [:stop] - Select from start to the end but exclude the last element
array_3 = np.array([89,32,56,7,78,90])
print(array_3[:3]) 

#4 [start: stop] - Select from start to stop in which stop is excluded
array_4 = np.array([1,3,4,46,55,7,56,8])
print(array_4[2:6])

#5 [start : stop : step] - start and stop same concept but step is basically means skip the elements.
array_5 = np.array([14,3,5,76,6,7,8,89]);
print(array_5[2:6:2]) ## Here (2:6:2) means: 2 is for start index and 6 is stop index while the last 2 is for skip 1 element
## So the outpput with [2:6] - would be [5,76,6,7] , but with [2:6:2] it would be - [5,6]  so it skip 1 elements
