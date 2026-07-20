# CONDITIONAL STATEMENTS
# statement which check whether the given statement is true or not

# TYPES
# 1. if...statement
# 2. if...else statement
# 3. elif.. else statement
# 4. Nested...if statement


# 1. if..statement
#def : excutes the block only the condition is TRUE.
#Syntax
# if (condition):
# {
#     statement
# }
# example
# age = int(input("Enter age: ")) #47
# if (18 <= age <= 65): #condition
#     {
#         print("age : ", age)    #statement
#     }
# print ("Nandri")



# 1. if..else statement
#def : excutes the if block when the condition is TRUE, otherwise False
#Syntax
# if (condition):
# {
#     statement
# }
# else:
# {
#     statement
# }
# example
# age = int(input("Enter age: ")) #47
# if (1 <= age <= 18) or (25 < age <= 50): #condition
#     {
#         print("age : ", age)    #statement
#     }
# else:
#     {
#         print("Enter right age", age,"❌")
#     }
# print ("Nandri")




# 1. if..elif..else statement
# def : excutes the if block when the condition is TRUE, if it is false, elif statement will be executed. if ELIF is false, else part will be executed.

# Syntax
# if (condition):
# {
#     statement
# }
# elif(condition):
# {
#     statement
# }
# else:
# {
#     statement
# }

# example
# age = int(input("Enter age: ")) #47
# if (10 < age < 20): #condition
#     {
#         print("If age : ", age)    #statement
#     }
# elif(20 < age < 30):
#     {
#         print("Elif Your age: ", age)
#     }
# else:
#     {
#         print("Else Not eligible")
#     }
# print ("Nandri")



# 1. Nested..if statement
# def : A if block nested inside a another if
# Syntax
# if (condition):
#   if(condition):
#     {
#     statement
#     }
#   else:
#   {
#     statement
#   }
# else:
# {
# statement
# }

# example
username = input("Enter Username: ")
if(username == "Ragav"):
    password = input("Enter Password: ")
    if(password == "3143"):
        {
            print("Login Success")
        }
    else:{
        print("Wrong password")
    }
else:{
    print("Wrong Username")
}
    