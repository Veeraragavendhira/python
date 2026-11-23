# FUNCTION
# FUNCTION is a set of code which is defined under a name(Function name)
# Resuable of code

# Declaration of a FUNCTION
# def function_name()


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
#     car()
# car()
# bus()



# #ADD
# def add():
#     a = int(input("Enter a: "))  # variable declaration 
#     b = int(input("Enter b: "))  # variable declaration 
#     print(a + b)
#     # return add()
# print("ADD WILL BE CALLED")
# input("Wait for a click....")
# add()
# print("ADD EXECUTED")
# a = 10
# b = 20
# print(a - b)
# print(b)
# add()




# type()
# len()
# print()
# Types of Functions
# 1. No parameter & No return
# 2. With parameter & No return
# 3. No parameter & With return
# 4. With parameter & With return


# 1. No parameter & No return
# def CM():
#     print("one")
# CM()
# CM()


# 2. With parameter & No return
# def CM(a,b,c):
#     print("one", a, b, c)
# CM(10,20,30)
# CM(1,2,3)


# 3. No parameter & With return
# def CM():
#     a = 10
#     b = 20
#     print(a + b)
#     return a
# # CM()
# print(CM())


# 4. With parameter & With return
# def CM(a, b):
#     print(a + b)    
#     return a , b
# CM(25,0)
# CM(15, 5)
# print(CM(1,2))



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
# b = 21
# print(b)
# def friday():
#     # global b
#     b = 20  #Local
#     print(a)
#     print(b)
#     print("Function executed, Variable printed")
# friday()
# print(a)
# b = 19
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
# def default(name = "Friend", age = 18):    #default
#     print("Hello" , name, age) 
# default("ram", 20)
# default(18, "thiyagu")
# default()
# print("End...✌️")


#Positional Arguments :
#   assign the data on a order
# def argu(name ,age):    #default
#     print("Hello" , name , age) 
# argu(20, "RAJA")  #positional
# argu("Ragu", 11)
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
    

