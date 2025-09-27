#Program to Find the Factorial of a Number

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

user_input = int(input("Enter a number:- "))

calculate_factorial = factorial(user_input)

print("Factorial of",user_input,"is",calculate_factorial)
