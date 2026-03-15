import numpy as np 

# rng = np.random.default_rng(seed=1) 
# -->| it will keeep the same random num 

rng = np.random.default_rng() 
print(rng.integers(low=1,high=7, size=(3,2)))

print(np.random.uniform(low = 1, high = 2, size=3))

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple","banana","pineapple","guava","litchi"])
fruits = rng.choice(fruits, size=(3,2))
print(fruits)


