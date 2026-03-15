import numpy as np

#scalar math

arr1 = np.array([1,2,3])

print(arr1 + 1)
print(arr1 - 2)
print(arr1 * 3)
print(arr1 / 4)
print(arr1 ** 2)

#vectorized maths funcs

arr2 = np.array([1.2, 2.5, 3.99])
print(np.sqrt(arr2))
print(np.round(arr2))
print(np.floor(arr2))
print(np.ceil(arr2))
print(np.pi)

#area of circle
radii = np.array([1,2,3])
area =  np.pi * radii ** 2
print(area)

#Element wise operations
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 - array2)
print(array1 / array2)
print(array1 * array2)
print(array1 ** array2)


#comparison operators 
scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores >= 60)
print(scores <= 60)

scores[scores < 60 ] = 0 
print(scores)

