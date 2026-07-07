#Create a numpy Array
#Arrays are created using the np.array() function.

import numpy as np
# Define the array 

#one-dimensional array
array1 = np.array([1, 2, 3, 4, 5])
print(array1)

#two dimensional array
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)

#three-dimensional array
array3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array3)

#one-dimensional array from a tuple
array4 = np.array((1, 2, 3, 4, 5))
print(array4)

#accessing elements in a one-dimensional array
print(array1[0])
#accessing elements in a two-dimensional array
print(array2[0, 1])