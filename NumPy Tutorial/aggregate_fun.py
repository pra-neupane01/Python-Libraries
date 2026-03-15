import numpy as np

arr = np.array([[10,9,8,7,6],
                  [5,4,3,2,1]])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))

print(np.sum(arr, axis=0)) # sum columns 
print(np.sum(arr, axis = 1)) # sum rows

