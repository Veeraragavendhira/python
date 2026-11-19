#Return
# stops the function & Returns the value to the function

def add():  #function definition
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Inside Function", a + b)
    print(a,b)
    return a , b
add()
# print("c = " ,c)