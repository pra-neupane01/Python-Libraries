import numpy as np


array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])



#array[start:end:step]

#accessing row
print(array[0])
print(array[-1])
print(array[::1])
print(array[::-2])
print(array[0:4:2])

#accessing column 
print(array[0,0])
print(array[:,:])
print(array[:,0])
print(array[:,0:4:2])
print(array[:,::-1])
print(array[:,::-2])
print(array[:,:3:2])

#accessing matrix
print(array[:2:,:2:])
print(array[:3:2,1:3:])
print(array[2:,2:])

