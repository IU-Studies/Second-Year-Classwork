#Program to Convert Celsius To Fahrenheit

def celsius_to_fahrenheit(celsius):
    return f"Celsius To Fahrenheit conversion of {celsius} degree is {celsius+273} degree"

user_input = int(input("Enter degree in celsius:- "))

conversion = celsius_to_fahrenheit(user_input)

print(conversion)
