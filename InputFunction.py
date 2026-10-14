''' You need to perform three separate tasks based on the given input:
         1.  String Input and Print: Read a string s (which may contain spaces) and print it as it is.
         2.Integer Input and Print: Read an integer n and print it without any change.
         3.Float Input and floor Print: Read a floating-point number as input, take its floor value, and print as an integer. '''


import math
s = str(input("Type value of s : "))
n = int(input("Type value of n : "))
f = float(input("Type value of f : "))
a = math.floor(f)
print(s)
print(n)
print(a)