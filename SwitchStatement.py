# switch statement like C++ or Java. Instead, starting with Python 3.10, it uses a much more powerful feature called structural pattern matching via the match and case keywords.
# Que --> Given a number n, use a switch statement to return "One" if the given number is equal to 1, "Two" if the number is 2 and so on till 9 ("Nine") else return "Unknown"(without quotes). 

n = int(input("Enter a number : "))


match n :
    case 1:
            print("One")
    case 2:
            print("Two")
    case 3:
            print("Three")
    case 4:
            print("Four")
    case 5:
            print("Five")
    case 6:
            print("Six")
    case 7:
            print("Seven")
    case 8:
            print("Eight")
    case 9:
            print("Nine")
    case _:
            print("Unknown")