def decorator(fx):
    def gx(a,b):
        if a > b:
            print(a-b)
        else:
            print(b-a)
    return gx

@decorator
def subtract(a,b):
    return a-b

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

subtract(x,y)
