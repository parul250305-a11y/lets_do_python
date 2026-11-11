'''
Given a number n, print your answer according to the following conditions:

If the number is divisible by 3, you print Fizz
If the number is divisible by 5, you print Buzz
If the number is divisible by both 3 and 5, you print FizzBuzz
In any other case, you print the number itself
'''

n = int(input("Enter a number : "))

if n % 3 == 0 and n % 5 == 0:
      print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)





