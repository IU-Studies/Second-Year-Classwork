#Program to Generate a Random Number

import random

def random_number_generator(start,end):
    return f"Random number is:- {random.randint(start,end)}"

start_range = int(input("Enter start range:- "))

end_range = int(input("Enter end range:- "))

random_number = random_number_generator(start_range, end_range)

print(random_number)
