import numpy as np

array1 = np.array([2, 12, 3 ,15, 25, 45, 30, 33])
print('Array 1 = \n', array1)

roots = np.sqrt(array1)
print('roots', roots)

exponentials = np.exp(array1)
print('exponentials', exponentials)

print('Element at index 3 = ', array1[3])

array2 = array1[1:15]
print("sliced array", array2)
