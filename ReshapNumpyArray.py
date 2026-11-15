# Ques --> Given a 1-dimensional NumPy array arr of size n and two integers rows and cols, convert the array into a 2-dimensional array of size rows × cols.

class Solution:
    def reshapeArray(self, arr, rows, cols):
        return arr.reshape(rows,cols)
    
    