#Program to Calculate the Area of a Triangle

def calculate_area_triangle(base, height):
    return f"Area of triange is {(1/2) * base * height}"

user_input_base = int(input("Enter base:- "))
user_input_height = int(input("Enter height:- "))

calculate_area = calculate_area_triangle(user_input_base, user_input_height)

print(calculate_area)
