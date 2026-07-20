#LOOPING STATEMENTS
# Run the statement or condition untill it gets false
#while loop
#for loop

#while loop
# excutes the block untill the condition gets FALSE
#syntax:
# while(condition):
# {
#     statement
# }

# Example:
# a = int(input("Enter a : ")) 
# b = int(input("Enter b : ")) 
# while (a <= b): 
#         print ("b is Big", a, b) 
#         a -= 1 # a = a+1 ====> 0+1 =1
# print ("The End Game")



#infinite loop
# a = 1
# while(a > 0):
#     print(a)
#     a += 1



# RANGE
# range() is a built-in function used to get a certain amt of values or sequence of numbers
#syntax:
# range(start, stop, step)
    # statemtnt


# example: 
# s = range(10, 25, 2 )
# # s = range(3,5)
# print(list(s))
# print(s)
# print(type(s))


# for loop
# repeating the sequence of values
#syntax:
# for variable in sequence:


# for i in range(10):
#     print(i)


# for i in range(0, 50, 2):
#     print(i)
# print("END")


# for i in range(0, -10, -2):
#     print(i)
# print("EXITED THE LOOP")

# list = ["parthiban", "senthil" , "guna", "rajan", "anbu", "leo", "sopanasundari"]
# for deepak in list:
#             print(deepak) 
        

# for in string
# str = "string i @"
# for i in str:
#     print (i)

# break
# stops the loops on particular iteration
# for i in range (10):
#     if i == 7:
#         print(i)
#     break
#     if i <= 7:
#         print(i)
# print("done")


# a = 1
# while(a > 0):
#     print(a)
#     a += 1
#     # if  a >= 100:
        # break
    
# a = 0
# while True:
#     print (a)
#     if (a == 100):
#         break
#     a += 1


# continue
# Skips the current iteration and continues the loop
# for i in range (13):
#     if i == 11:
#         continue
#     print(i)
        

#pass
# need space for code (nothing happen just an empty block)
# for i in range (12):
#     if i == 1:
#         pass
#     print(i)


# # for using *(Multiple)
# for i in range (7):
#     print (i, " Mohana " * i)


# for using +(ADD)
# a = 0
# for i in range (7):
#     a = a + 1
#     # print(a)
# print("a=",a)







# #NESTED FOR
# for i in range(3): #0, 1, 2
#     for j in range(3): #0, 1, 2
#         for k in range (3): #0, 1, 2
#             print(i,j, k)


# 1     * * * * *
# 2     * * * * *
# 3     * * * * *
# 4     * * * * *
# 5     * * * * *



# for i in range(5):
#     print(" * " * 5)



#MATCH CASE
# Match case in python act as a switch case. 

#syntax:
# match value:
#     case 1:
#         print("one")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _(default):
#         print("None")


# Ex:
# a = input("Enter a : ")
# b = input("Enter b : ")
# case = input("Enter +, -, *, / :" )
# match case:
#     case "+":
#         print("+ case = ",a + b )
#     case "-":
#         print("- case = ",a - b )
#     case "*":
#         print("* case = ",a * b )
#     case "/":
#         print("/ case = ",a / b )
#     case _: #default
#         print("ERROR")



case = input("Enter Admin, HR, emp, stu : " )
match case:
    case "Admin":
        print("FULL ACCESS" )
    case "HR":
        print("ADD & DELETE EMPLOYEES")
    case "emp":
        print("VIEW & DO TASKS")
    case "stu":
        print("SIMPLY WATCH")
    case _: #default
        print("OUT OF COMPANY")



