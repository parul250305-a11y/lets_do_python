# Que --> Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a.

a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))

a , b = b , a
print(f"value of a is {a} and value of b is {b}")

