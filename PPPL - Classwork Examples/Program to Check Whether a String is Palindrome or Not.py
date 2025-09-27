#Program to Check Whether a String is Palindrome or Not

def check_palindrome(string):
    if string == string[::-1]:
        return f"{string} is a Palindrome"
    else:
        return f"{string} is not a Palindrome"

user_string = input("Enter a string:- ")

result = check_palindrome(user_string)

print(result)
