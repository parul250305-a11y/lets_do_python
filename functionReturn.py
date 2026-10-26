# Que --> Take an integer n, You need to use the return keyword to return twice the value of n.
n = int(input("Enter a number: "))
class Solution:
    def returnValueFunction(self, n):
        return 2*n

s = Solution()
result = s.returnValueFunction(n)
print(result)