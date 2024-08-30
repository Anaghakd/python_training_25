import numpy as np

arr1 = np.full((1, 5), 15)
print(arr1)

print(arr1[0])
print(arr1[0][1])
print(arr1[1][0]) #Error. There is no second list in arr1
