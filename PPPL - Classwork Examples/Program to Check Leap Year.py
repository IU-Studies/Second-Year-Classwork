#Program to Check Leap Year

def check_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

user_input = int(input("Enter a year: "))

print(check_leap(user_input))
