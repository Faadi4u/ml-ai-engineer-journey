import numpy as np
## Splitting- Splitting takes one array and divides it into multiple smaller arrays.

## 1. np.split() - It's used when we need equal-size pieces of array.

array_1 = np.arange(15);

parts = np.split(array_1, 5) ## Make sure the size should be equal as we are giving 3 which is 5 x3 = 15 is doable
## If the size of arrays are not equal like 4x4 = 16 we can get value error

for part in parts:
    print(part);

# Output
# [0 1 2]
# [3 4 5]
# [6 7 8]
# [ 9 10 11]
# [12 13 14]

## 2. np.array_spllit - In this we don't need equal pieces, uneven pieces are acceptable

array_2 = np.arange(17);

parts = np.array_split(array_2, 7) ## we cant get and error it will auto adjust each array with uneven data.

for part in parts:
    print(part)

# Output:

# [0 1 2]
# [3 4 5]
# [6 7 8]
# [ 9 10]
# [11 12]
# [13 14]
# [15 16]


## 3. np.hsplit vs np.vsplit - 

array_3 = np.arange(24).reshape(6,4);
parts = np.hsplit(array_3, 2) ## it is equals to -> np.split(arr, 2, axis=1)
parts = np.vsplit(array_3, 2)