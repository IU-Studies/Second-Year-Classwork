import time

def decorator(fx):
    def gx():
        print("Program Start")
        time.sleep(2)
        fx()
        print("Program End")
    return gx
    
@decorator
def hello():
    print("Hello")

hello()
