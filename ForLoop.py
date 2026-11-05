# Que ---> Given a number n, print the first n positive even numbers in increasing order in a single line using a for loop.

if __name__ == "__main__":
  n = int(input("enter a number:"))

  end_value = 2 * n

  for i in range(2, end_value + 1, 2):
    # Check if this is the absolute last number in the sequence
    if i == end_value:
      print(i, end="")  # No space after the last number
    else:
      print(i, end=" ")  # Normal space separator for the others


"""This code give same kind of output . find the differance in both code output and which one is wrong """

n = int(input("enter a number:"))
for i in range(1 ,n+1):
  print(2*i , end=" ")

