#Basic Programs Program to Find the Square Root

def sq_root(num):
    return num ** (1/2)

user_input = int(input("Enter a number:- "))

calculate_sqrt = sq_root(user_input)

print("Square root of",user_input,"is",calculate_sqrt)
