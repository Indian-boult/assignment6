import numpy as np
arr = np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
n = len(arr)
k = 3
for i in range(n-k+1):
    res = 0
    for t in range(i,i+k):
        res += arr[t]
    res = res/k
    print("Moving average",(i+1), "is", res)