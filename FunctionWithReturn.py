# Que --> Given an integer n, You need to use the return keyword to return twice the value of n.

class Solution:
    def returnValueFunction(self, n):
        return 2*n
    
s = Solution()
p = s.returnValueFunction(5) # write any number at the place of 5 u want.......
print(p)



"""
Que --> Why We Use return in a Function?
Ans --> We use return so that the program can save and use the result of a function for other operations. 
"""

'''
Que --> Why We Do Not Use print Inside a Function
Ans --> Using print inside a function makes the result useless for the rest of your code.
print only displays text on your screen for a human to see. It does not give any data back to the computer. If you try to save the result of a function that only uses print, your variable will end up empty (None).
'''
