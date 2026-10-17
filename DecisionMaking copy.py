# A decision-making statement (also known as a conditional statement) is a programming construct that controls the flow of execution in a program based on whether a given condition evaluates to true or false. Instead of running code strictly from top to bottom in a straight line, these statements allow the program to make logical choices and execute specific code blocks dynamically
#  Decision making statements are  --> if - elif - else 


n = int(input())
m = int(input())

if n == m :
    print("equal")
elif n > m :
    print("greater")
else :
    print("less")