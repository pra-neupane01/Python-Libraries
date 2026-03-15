import numpy as np

array0 = np.array('A')
array1 = np.array(['A','B','C'])
array2 = np.array([['A','B','C'],
                   ['D','E','F'],
                   ['G','H','I']])
array3 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                   [['J','K','L'],['M','N','O'],['P','Q','R']],
                   [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
print(array0.ndim)
print(array1.ndim)
print(array2.ndim)
print(array3.ndim)

my_name = print(array3[1][2][0] + array3[1][2][2] + array3[0][0][0] + array3[1][0][1] + array3[0][0][0] + array3[2][0][0] + array3[0][2][1] )
