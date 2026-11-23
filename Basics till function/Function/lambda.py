# Lambda Function
    # One-line function

# Normal Function
def func_name(a):
    return a * a 
func_name(5)


# Using Lambda
#             lambda parameter(a): expression 
# func_name = lambda a: (a*a, a+a, a-a, a/a, a==a)  
# print("EXECUTED")
# print(func_name(5))
# print(func_name(3))


# ODD / EVEN
# def numbers():
#     n = int(input("enter n : "))
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(numbers())

# numbers = lambda n : "Even" if n % 2 == 0 else "Odd"
# n = int(input("enter n : "))
# print(numbers(10))
# f"{a[0]} is the first letter of {a}"

# print greatest of 2 numbers(a > b print(a)) using if  else
# greatest = lambda a, b: (a, "a is Greater") if a > b else (b, "b is Greater")
# a = (input("Enter a : "))
# b = (input("Enter b : "))
# print(greatest(a, b))


# print first letter of a name using index 
# name = lambda a : (a[0] , 'is the first letter of', a )
# a = input("Enter a : " )
# print(name(a))


# Map() 
# This is a Built-in function which applies a function to every item in an iterable
# map() ===> Built-in function
# oru list la iruka values ah ovovoru time um check & run pannum
# num = [1, 2, 3, 4, 5, 6]
# abc = (map(lambda a: a % 3 , num)) 
# print(list(abc)) 

# num = [" abcd ", "efgh ", "ijkl "]
# abc = (map(lambda a: a[0] , num)) 
# print(list(abc)) 



# filter()
# returns the values which satisfy the condition
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# abc = (filter(lambda a: a % 2 == 1  , num)) 
# print(list(abc)) 


# num = [" Anbu ", "Arivu ", "arivu ", "Baskar", "Anna", "Chandru", "surya"]
# abc = (filter(lambda a: a.startswith("A") , num)) 
# print(list(abc)) 

# square = lambda x: x + x
# print(square(5))


# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x: x % 2 == 1, numbers))
# print(even)

# try:
#     a = 10
#     b = 0
#     print(a / b)
# except:
#     print("Cannot divide by zero")


# try:
#     print(10 / 0)
# except:
#     print("Error")
# finally:
#     print("Program Finished")

# age = 17
# assert age >= 18, "Age is not more than 18"
# print("Eligible")
