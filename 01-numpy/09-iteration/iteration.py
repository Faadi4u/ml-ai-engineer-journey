import numpy as np


X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
## Its shape is (2,3)

for item in X:
    print(item)

## Output
# [10 20 30]
# [40 50 60]

## But we wanna iterate it to every single elements of that array. For that we need to use nested loop in python

for item in X:
    for value in item:
        print (value) 

# now the output:
# 10
# 20
# 30
# 40
# 50
# 60
## Thats what we want. So if we have 3d array we have to nested our loop 3 times which will be frustrating if we have 50D array.
## So here numpy's function is used called nditer:

for value in np.nditer(X):
    print(value)

# 10
# 20
# 30
# 40
# 50
# 60

## So with nditer we dont need to do use nested loop we only need to use np.nditter and it will iterate to every elements ...
## Even if it has 50D array.