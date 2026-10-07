import numpy as np

## What is indexing? 
## It is basically used to get the specific chunk/element from the array
## For example: [1,2,3,4,5,78,5] -> we want to get 5 from that array so :

arr_index = np.array([1,2,3,4,5,78,5])

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