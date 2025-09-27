#Program to Check Prime Number

def check_prime(number):
    if number <= 1:
            return f"{number} is not a Prime Number"
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is not a Prime Number"
    return f"{number} is a Prime Number"

user_input = int(input("Enter a number:- "))

result = check_prime(user_input)

print(result)
