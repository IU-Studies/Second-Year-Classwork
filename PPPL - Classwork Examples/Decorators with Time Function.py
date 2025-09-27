import time

def decorator(fx):
    def gx():
        start = time.time()
        print("Program Start")
        time.sleep(2)
        fx()
        end = time.time()
        print("Program End in",round(end - start, 2), "Seconds")
    return gx
    
@decorator
def hello():
    print("Hello")

hello()
