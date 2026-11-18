#identity  
# ID is a in-built function which holds a different ID for a data.
# a = 10
# b = 10.0
# print(a, id(a))     
# print(b, id(b))     
# print(a is b)



#Identity Operator
# is =========> same ID returns TRUE
# is not ========> Different ID returns TRUE

# x = [1, 2]
# y = [1, 2]
# print(type(x))
# print(type(y))
# print(x, id(x))    #3051039209152
# print(y, id(y))      #3051039092672
# print(x == y)
# print(x is y)
# print(x is not y)



a = {10, 1}
b = {10, 1}
print(id(a))
print(id(b))
print(a is b)
print(a is not b)








# a = 10
# b = 10
# print(a is b)
# print(id(a))
# print(id(b))
