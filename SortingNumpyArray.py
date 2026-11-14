#  Que --> Given a 1-dimensional NumPy array arr, sort its elements in ascending order.
import numpy as np 
class Solution:
    def sortArray(self, arr):
        return np.sort(arr)
    

s = Solution()
array = np.array([1, 2, 3, 4])  # write your own array here.....
y = s.sortArray(array)
print(y)    