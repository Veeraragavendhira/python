# FUNCTION
# FUNCTION is a set of code which is defined under a name(Function name)
# Resuable of code

# Declaration of a FUNCTION
    #  def function_name():

# Syntax :
# def function_name():   #defining a function
    #statements       #content of the function 
# function_name()       #function call

# def car():
#     print("TATA")
#     print("MAHINDRA")
#     print("BIKE")


# def bus():
#     print("VOLVO")
#     print("SCANIA")

# bus()
# car()



# #ADD
# def add():
#     a = int(input("Enter a: "))  # variable declaration 
#     b = int(input("Enter b: "))  # variable declaration 
#     print(a + b)
#     return add()
# print("ADD WILL BE CALLED")
# add()
# print("ADD EXECUTED")
# print(a - b)
# print(b)
# print(add())


#Return
# stops the function & Returns the value to the function

# def add():  #function definition
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     print("Inside Function", a + b)
#     return a , b
# c = add()
# print("c = " ,c)

# Types of Functions
# 1. No parameter & No return
# 2. With parameter & No return
# 3. No parameter & With return
# 4. With parameter & With return


# 1. No parameter & No return

# def CM():
#     print("one")
# CM()


# 2. With parameter & No return
# def CM(a):
#     print("one", a)
# CM(10)
# CM(2000)


# 3. No parameter & With return
# def CM():
#     a = 10
#     b = 20
#     print(a + b)
#     return a
# CM()
# print(CM())


# 4. With parameter & With return
# def CM(a, b):
#     print(a + b)    
#     return a , b
# CM(25, 10)
# print(CM(15, 5))



#SCOPE OF VARIABLES
#   defines the power of the variable where can we use or where we cannot
#   Types
#   1. Global Variables
#   2. Local Variables


#   1. Global variable
#   The variable which can be used over the program is know as Global variables.
#   Local variable
#   The variable which can be used only inside the block is know as Local variables.

#   Example:
# a = 11  #Global
# def friday():
#     b = 20  #Local
#     print(a)
#     print(b)
#     print("Function executed, Variable printed")
# friday()
# print(a)
# print(b)

# global Keyword:
# a = 11  #Global
# def friday():
#     global b 
#     b = 20
#     print(a)
#     print(b)
#     print("Function executed, Variable printed")
# friday()
# print(a)
# print(b)



#Default Arguments :
# if user does not provide the arguments it automatically takes the backup values stored 
# def argu(name = "Friend", age = 18):    #default
#     print("Hello" , name, age) 
# argu("ram", 20)
# argu()
# print("End...✌️")


#Positional Arguments :
#   assign the data on a order
# def argu(name = "Friend", age = 18):    #default
#     print("Hello" , name, age) 
# argu(20, "RAJA")  #positional
# argu("Ragu")
# print("End...✌️")


# #Keyword Arguments :
# #   assign the arguments based on the parameters(keyword)
# # Ex
# def argu(name = "Friend", age = 18):    #default
#     print("Hello" , name, age) 
# argu(name = "raja", age = 21)   #keyword
# argu(age = 20, name = "ram" )
# argu("Ragu")
# print("End...✌️")
    

# Lambda Function
    # One-line function

# Normal Function
# def func_name(a):
#     return a * a 
# print(func_name(5))


# Using Lambda
#             lambda parameter(a): expression 
# func_name = lambda a: (a*a, a+a, a-a, a/a, a==a)  
# print("EXECUTED")
# func_name(5)
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


numbers = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x % 2 == 1, numbers))
print(even)
