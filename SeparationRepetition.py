# Que --> Given three inputs a, b, and c, print a exactly a times and b exactly b times in the same line, with c printed between them.
a = input("Enter a number: ")
b = input("Enter a number: ")
c = input("Enter a special char: ")

print(a*int(a)+c+b*int(b))
