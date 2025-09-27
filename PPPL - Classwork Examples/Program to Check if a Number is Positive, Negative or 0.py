#Program to Check if a Number is Positive, Negative or 0

def integer_check(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    else:
        return "Negative"

user_input = int(input("Enter a number:- "))

result = integer_check(user_input)

print(result)
