#Program to Count the Number of Each Vowel

def count_vowel(string):
    vowel = "AEIOUaeiou"
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    return f"Number of vowels present in {string} are {count}"

user_string = input("Enter a string:- ")

result = count_vowel(user_string)

print(result)
