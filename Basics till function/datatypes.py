# type()
# To identify the type of the data
# a = 100.55
# print(type(a))

# Data types:

# Two types:
    # 1. Monomorphic data type
    # 2. Polymorphic data type

# 1. Mono
        # 1. integer
                # the whole numbers both have +Ve & -ve 
                # -100, 200, 0,100,1000,212091202
# Example:
# a = 0
# print(a)
# print(type(a))

        # 2. float
 # the whole numbers with decimal values having +Ve & -ve 
                # -100.098765, 200.7654, 0.0,100.00,1000.99,21209.1202
# a = -.000055
# print(a)
# print(type(a))

# 3. string
#   ->data should be in single or double quotes (''  ,  "") 
#   numbers, letter, special characters, space       
# example
# a = 10
# print ("a= ", a) 
# print(type(a))

# a = "ragav@123. 321"
# print("a= ", a)
# print(type(a))
# b = 10
# c = 100
# print(a)


# 4. Boolean (Bool)
# returns True(0) or False(0)
# a = 10
# b = 20
# print(a > b)
# print(a < b)


# 2. Polymorphic
# 1. list (list)
# Store multiple values in a variable
# Mutable (change values)
# Ordered - vales order arrangements irrukum
# Allow duplicates 
# allow different data types
# []

# index values
# 0,1,2,3,4
# a = [20, -20, 20, 20 ,"dasdasdas", False]
# print(a[3])
# print(type(a[2]))
# print(type(a))


# 2. tuple (tuple)
# Store multiple values in a variable
# ImMutable (cannot change values)
# Ordered - vales order arrangements irrukum
# Allow duplicates 
# allow different data types
# a = (0, -20, 20, 20 ,"dasdasdas", False)
# print(a)
# print(type(a))
# print(type(a[2]))

# 3. set {set}
# to store only Unique values
# Store multiple values in a variable
# Mutable (can change values)
# unOrdered - vales order arrangements irrukadhu
# do not Allow duplicates 
# allow different data types
# No indexing 
# a = {0, -20, -20, -20 ,"string" ,"dasdasdas", False,0, True, 1, 21}
# print(a)
# print(type(a))


# 4. dictionary (dict)
# storing values in Key & values pair
# student = {
#     "name" : "ragul", #name is the key
#     "age" : "21",   # 21 value 
#     "place" : "Karur"
# }
# print(student)
# print(student["name"])
# print(student["age"])

# student = {
#     "name" : ["ragul", "ragu", "ragav"], #name is the key
#     "age" : "21",   # 21 value 
#     "place" : "Karur"
# }
# print(student)
# print(student["name"])
# print(student["age"])





# List _ values
# tuples -  fixed values
# set - Unique values
# dict - key + value



# Typecasting
# Changing one datatype to another datatype
# a = 10
# print(type(a), "a=",a)
# a = str(a)
# print(type(a))
# print("final = ",a)
# print(a)
