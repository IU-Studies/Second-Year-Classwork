#Program to Find Factorial of Number Using Recursion

def factorial(n):
    fact = 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

user_input = int(input("Enter a number:- "))

result = factorial(user_input)

print("Factorial of",user_input,"is",result)
