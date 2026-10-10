import numpy as np
# Ufuncs 
    ## unievrsal functions are operates on ndarrays as element-wise. It act as a vectorized wrapper around a function.
    ## It has stndard array functions like np.add , np.multiply etc..
    ## It has also Trignometric functions like np.sin , np.cos 
    ## Means we can do most of the method by using ufuncs

A = np.array([1,98,4,-46,89,67,7,8,]);

print(np.add(A,5)) ## Addition
print(np.abs(A)) ## All the negative values converted in positive 
print(np.sqrt(A)) ## Square root
print(np.log(A)) ## Natural log 
print(np.add.reduce(A)) ## It add all the elements and give one value. In this output should be: 228
## It also handle the broadcasting error(If the shapes of arrays are not matching) behind the computation 
## It has many more functions BUt for this file is ok for the basic idea.
