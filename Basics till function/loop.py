#LOOPING STATEMENTS
# Run the statement or condition untill it gets false
# 1. for loop 
# 2. while loop
# 3. range()  function
# 4. Nested loops
# 5. break
# 6. continue
# 7. pass


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
# c = int(input("Enter c : "))
# while ((a + b) < c): 
#         print (a, b, c, " condition passed ") 
#         a += 2 # a = a-2
# print ("The End Game")



#infinite loop
# a = -1
# while(a < 0):
#     print(a)
#     a -= 1



# RANGE
# range() is a built-in function used to get a certain amt of values or sequence of numbers
# default start value 0
# end value should be before value
#syntax:
# range(start, stop, step)
    # statement

# example: 
# s = range(0,25,3)
# print(s)
# print(list(s))
# print(type(s))



# for loop
# repeating the sequence of values
#syntax:
# for variable in sequence:

# for i in range(0,10, 4):
#     print(i)
# print("mudinchuu")


# for i in range(0, 50, 10):
#     print(i)
# print("END")

# for i in range(0, -10, -2):
#     print(i)
# print("EXITED THE LOOP")


# list = ["parthiban", "senthil" , "guna", "rajan", "anbu", "leo", "sopanasundari"]
# # print(list[6])
# for deepak in list:
#             print(deepak) 
        
# str = "string i @"
# for string in str:
#     print (string)


# break
# stops the loops on particular iteration
# for i in range (13):
#     print(i)
#     if i == 11:
#         print("break", i)
#         break


# a = 1
# while(a > 0):
#     print(a)
#     a += 1
#     if  a >= 100:
#         break
    
# a = 0
# while True:
#     print (a)
#     if (a == 100):
#         break
#     a += 1


# continue
# Skips the current iteration and continues the loop
# for i in range (13):
#     if i == 10:
#         continue
#     print(i)
        

#pass
# need space for code (nothing happen just an empty block)
# for i in range (12):
#     if i == 1121321:
#         pass
#     print(i)


# for using *(Multiple)
# for i in range (8):
#     print (i, " StrinG " * i)


# for using +(ADD)
# a = 0
# for i in range (7):
#     a = a + 1
#     print(a)
# print("a=",a)







# #NESTED FOR
# for i in range(3): #0, 1
#     for j in range(3): #0, 1
#         for k in range(3):
#             print("*")
# print("EXECUTED")
# 0,0
# 0,1
# 1,0
# 1,1

# 1     * * * * *
# 2     * * * * *
# 3     * * * * *
# 4     * * * * *
# 5     * * * * *



# for i in range(1):
#     print(" * " * 6)



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




# for i in range(5):
#     for j in range(5):
#         print(i,j ,"*", end=" ")
#     print()

# Ex:
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

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



# case = input("Enter Admin, HR, emp, stu : " )
# match case:
#     case "Admin":
#         print("FULL ACCESS" )
#     case "HR":
#         print("ADD & DELETE EMPLOYEES")
#     case "emp":
#         print("VIEW & DO TASKS")
#     case "stu":
#         print("SIMPLY WATCH")
#     case _: #default
#         print("OUT OF COMPANY")


# initial_balance = 5000
# total_deposits = 0

# deposit = int(input("Enter Deposit Amount: "))

# while deposit != 0:

#     if deposit < 0:
#         print("Invalid Deposit!")
#     else:
#         total_deposits += deposit

#     deposit = int(input("Enter Deposit Amount (0 to Stop): "))

# final_balance = initial_balance + total_deposits

# print("\n===== BANK STATEMENT =====")
# print("Initial Balance:", initial_balance)
# print("Total Deposits:", total_deposits)
# print("Final Balance:", final_balance)



# total = 0
# passed = 0
# failed = 0
# students = ["raja", "pooja", "hema", "booma", "Kooma"]
# for i in students:
#     mark = int(input("Student Mark", i))
#     total += mark
#     if mark >= 35:
#         print("Student", i, ": Pass")
#         passed += 1
#     else:
#         print("Student", i, ": Fail")
#         failed += 1
# print("\n===== STUDENT REPORT =====")
# print("Total Marks:", total)
# print("Passed Students:", passed)
# print("Failed Students:", failed)


# total = 0
# passed = 0
# failed = 0

# for i in range(1, 6):
#     mark = int(input("Student " + str(i) + " Mark: "))

#     total += mark

#     if mark >= 35:
#         result = "Pass"
#         passed += 1
#     else:
#         result = "Fail"
#         failed += 1

#     print("Student", i, ":", result)

# print("\n===== STUDENT REPORT =====")
# print("Total Marks:", total)
# print("Passed Students:", passed)
# print("Failed Students:", failed)



# number = 12345
# print(type(number))

# number=(str(number))
# print(len(number))

for i in range(1,101):
    print(i,"* 25 =", i*25 )