# "while loop" -- in Python is used to repeatedly execute a block of code as long as a specific condition remains True. It is ideal for situations where you do not know in advance how many times you will need to repeat a task.
#writing reverse countiong using while loop


x = int(input("Enter a number : "))

# code here
while x >= 0:
    print(x , end = " ")
    x = x - 1 