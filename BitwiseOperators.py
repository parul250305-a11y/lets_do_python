''' Que --> Given three positive integers a, b and c. Perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = ~ e
Note: ^ is for xor.
Then print d e f g space seperately. Move the cursor to the next line after printing.'''

# Bitwise operators in Python are used to perform bit-level operations directly on the binary representations of integers. Python automatically handles integers with arbitrary precision, meaning your operations will not suffer from traditional overflow limits seen in lower-level languages like C or Java.

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

d = a ^ a
e = c ^ b
f = a & b
g = ~ e
print(d, e, f, g)