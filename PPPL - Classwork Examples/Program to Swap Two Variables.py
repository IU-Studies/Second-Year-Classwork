#Program to Swap Two Variables

num1 = int(input("Enter first number:- "))

num2 = int(input("Enter second number:- "))

print("Value of first number is", num1,"Value of second number is", num2, "before swpping")

num1, num2 = num2 , num1

print("Value of first number is", num1,"Value of second number is", num2, "after swpping")
