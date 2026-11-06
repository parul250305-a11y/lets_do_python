# Que --> Given two integers a and b. The given input and its values are passed as arguments to the function argumentFunction. The argumentFunction is responsible to return (a+b). You need to write this function.

''' Write the complete argumentFunction below.
 The function should take two arguments a and b
 The function should return a+b'''


class Solution:
    def argumentFunction(self ,a , b):
        self.a = a
        self.b = b
        return a+b

c = Solution()
d = c.argumentFunction(5,5) # you can change the values and try it by ur self.....
print(d)
