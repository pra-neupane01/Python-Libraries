
import numpy as np
#CREATING ARRAYS
# arr0 = np.zeros((2,3))
# arr1 = np.ones((3,3))
# arr2 = np.full((2,2),2)
# arr3 = np.arange(2,10,2)
# arr4 = np.linspace(0,10,5)
# arr5 = np.array([1,2,3,4,5,6]).reshape((3,2))
# print(arr0)
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)
# print(arr5.T)

#---join an array 
A = np.array([1,2,3,4,5])
B = np.array([6,7,8,9,10])
print(np.vstack((A,B)))
print(np.hstack((A,B)))

#--splitting an array
arr = np.array([[1,2,3,4],
                [5,6,7,8]])
[A,B] = np.hsplit(arr,2)
print(A)
print(B)
