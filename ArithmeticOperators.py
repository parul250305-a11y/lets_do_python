''' Que --> Given two integer variables x and y, perform the following operations:

p: Addition of x and y
q: Subtraction of y from x
r: Multiplication of x and y
s: Floating-point division of x by y
t: Integer division of x by y
u: Modulo (remainder when x is divided by y)'''

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

p = x+y
q = x-y
r = x*y 
s = x/y
t = x//y
u = x%y
print(p, q, r, f"{s:.3f}", t, u)








'''
Python supports seven arithmetic operators to perform standard mathematical calculations on numbers:

Op|erator  |         Name	    |         Description	                                   |       Example  |	Result
+         |       Addition	    |   Adds two values together	                           |       10 + 5	|     15
-         |      Subtraction	|       Subtracts the right value from the left	           |       10 - 5	|      5
*         |     Multiplication  |    Multiplies two values	                               |       10 * 5	|     50
/         |        Division     |    Divides and always returns a float	                   |       10 / 5	|     2.0
//        |     Floor Division	|   Divides and rounds down to the nearest whole integer   |       10 // 3  |     33
%         |        Modulus	    |   Returns the remainder after division	               |       10 % 3	|      1
**        |     Exponentiation	|   Raises the first number to the power of the second	   |        2 ** 3  |      8
'''