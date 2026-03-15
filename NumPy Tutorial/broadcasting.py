
#compatible only when 
# The dimensions have the same size or, 
# one of the dimensions has size of 1.

import numpy as np

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],
                   [2],
                   [3],
                   [4],
                   [5],
                   [6],
                   [7],
                   [8],
                   [9],
                   [10]])
print(array1.shape)
print(array2.shape)

print(array1 * array2)