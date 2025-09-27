#Program to Solve Quadratic Equation
import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "No solution (a and b cannot both be zero)."
        else:
            return "Linear solution: x = " + str(-c / b)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Two distinct real roots: x1 = " + str(root1) + ", x2 = " + str(root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return "One real root (repeated): x = " + str(root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return ("Two complex roots: x1 = " + str(real_part) + " + " + str(imaginary_part) + "i, "
                "x2 = " + str(real_part) + " - " + str(imaginary_part) + "i")

user_input_a = float(input("Enter coefficient a: "))
user_input_b = float(input("Enter coefficient b: "))
user_input_c = float(input("Enter coefficient c: "))

print(solve_quadratic(user_input_a, user_input_b, user_input_c))
