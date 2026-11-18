def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
# @decorator
def display():
    print("Welcome")
display()
decorator(10)