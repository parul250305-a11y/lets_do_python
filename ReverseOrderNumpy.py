# Que -- > Given a 2D NumPy array arr, reverse the order of its rows and return the resulting array.

class Solution:
    def reverseRows(self, arr):
        return np.flip(arr , axis = 0)