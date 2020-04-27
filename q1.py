import numpy as np
arr = np.array([1,2,3,4,5])
N = 4
required_array = np.vander(arr, N)
print(required_array)