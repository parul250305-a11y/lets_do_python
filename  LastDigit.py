# Given an integer n. Write a program to print the last digit of n.

number = int(input("Enter a number: "))
lst_dig = abs(number)%10
print(lst_dig)