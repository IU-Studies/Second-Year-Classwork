#Program to Find the Largest Among Three Numbers

def check_largest(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print("Number one is greater i.e.", num1)
        else:
            print("Number three is greater i.e.", num3)
    elif num2 > num3:
            print("Number two is greater i.e.", num2)
    else:
        print("Number three is greater i.e.", num3)


check_largest(1,2,3)
check_largest(2,3,1)
check_largest(3,2,1)
