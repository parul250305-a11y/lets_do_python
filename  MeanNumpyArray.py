# Que --> Given a 1-dimensional NumPy array arr of size n, find the mean of all elements present in the array.

import numpy as np 
class Solution:
    def arrayMean(self, arr):
        return np.mean(arr)
        

s = Solution()
array = np.array([1, 2, 3, 4])  # write your own array here.....
y = s.arrayMean(array)
print(y)