import numpy as np

arr1 = np.arange(12)

arr2 = arr1.reshape(-2, 6)
arr3 = arr1.reshape(6, -2)
arr4 = arr1.reshape(3, 4)
arr5 = arr1.reshape(12, 1)

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5) 