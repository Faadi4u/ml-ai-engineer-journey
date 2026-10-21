import numpy as np
## 1. Asignment
## Because b = a does not create a new array. Both variables refer to the same ndarray object
## Therefore, modifying the array through b also affects what you see through a.
a = np.array([10, 20, 30, 40])

b = a

b[0] = 999

print(a)
print(b)
print(a is b)

## 2. View

a = np.array([10, 20, 30, 40])

b = a.view()

print(a is b)
print(np.shares_memory(a, b))

## a is b is False: they are different ndarray objects.
## np.shares_memory(a, b) is True: they share underlying data.
## Even though a and b are different objects, changing shared data through b affects a.
## A view lets you work with the same underlying data without creating an independent data copy.
# This can save memory, especially with large arrays.

## 3. Copy

a = np.array([10, 20, 30, 40])

b = a.copy()

b[0] = 999

print(a)
print(b)
print(a is b)
print(np.shares_memory(a, b))

## In copy they both have there own dataset and sperate ndarray objects.
## Means if we change one it cant effect to other so here they both have there own world.
