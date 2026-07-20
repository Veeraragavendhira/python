# LOGICAL OPERATORS
# compares two  or more values based on the conditions and returns T/F

#and
#or
#not

#and
#returns TRUE only both conditions are same only +ve.
# T and T   T             
# T   F     F   
# F   T     F
# F   F     F
# a = int(input("Enter Num1: "))
# b = int(input("Enter Num2: "))
# print(a>100)
# print(b>-200)
# print ((a>100) and (b>-200))
        



#or
#returns TRUE if any one is true
# T or T    T           
# T   F     T 
# F   T     T
# F   F     F
# a = int(input("Enter Num1: "))
# b = int(input("Enter Num2: "))
# print(a>5)
# print(b>=5)
# print ((5 < a < 7) or (b>=5))




#not
#reverse the data using one variable
#   input   output
    #T      F
    #F      T
# a = not False
# # a = not True
# print(a)

a = int(input("num : "))
print((a>=10987654323456)) # T
print(not(a>=10)) # F