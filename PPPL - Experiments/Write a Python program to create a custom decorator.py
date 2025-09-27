#Write a Python program to create a custom decorator that logs the name and execution time of a function.

import time

def decorator(func):
    def gx(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("executed in", end - start, "seconds.")
        return result
    return gx

@decorator
def demo():
    name = input("Enter name: ")
    print("Hello", name)

demo()
