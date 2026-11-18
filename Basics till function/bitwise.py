#Bitwise operators
# allow you to perform calculations on integers by manipulating their individual bits (0s and 1s)
# print(bin(52))

# print(bin(28))
# print(bin(11))
# print(bin(999))


#Binary AND &
# both bit 1 returns 1 otherwise 0
# 1     1   1
# 1     0   0
# 0     1   0   
# 0     0   0
#example:
# a = 50  
# b = 40
# print (a & b)


#Binary OR |
# Any one bit 1 returns 1 otherwise 0 
# 1     1   1
# 1     0   1
# 0     1   1   
# 0     0   0
#example:
# a = 50   #1	1	0	0	1	0
# b = 40   #1	0	1	0	0	0
#          #1 1   1   0   1   0 
# print (a | b)


#XOR ^
#same 0     different 1
# 1     1   0
# 1     0   1
# 0     1   1   
# 0     0   0
# a = 50   # 0111
# b = 40  # 1011
#         # 1100
# print (a ^ b)


#NOT ~
# reverse of 1 & 0
# 1 0
# 0 1
#Example
# a = int(input("Enter a : "))
# a = -(a+1)
# print (~a)


# LEFT shift ( << )
# moves the bits of an integer to the left by a specified number of positions.
# a = 10     
# b = 2 # 101
# c = a << b
# print(bin(a))
# print(bin(c))
# print("Left Shift:" , c)
# Math: 5 * (2^4) = 5 * 4 = 20
# Binary: 101 becomes 10100


# Right Shift ( >> ) 
# That shifts the bits of a number to the right by a specified number of positions.
# a = 100   # 1	1	0	0	1	1	0
# b = 2
# c = a >> b  # 110
# print(bin(c))
# print("Right Shift:", c)
# Math: 101 // (2^4) = 40 // 8 = 5
# Binary: 101000 becomes 101






#BITWISE OPERATORS
# a = 12
# b = 7
# And = print(a & b) # and   4
# Or = print(a | b) # or    4, 15
# Xor = print(a ^ b) #xor  11
# Not = print(~a)   #not  -13
# print(a << b) #left shift    1664
# print(a >> b) #right shift
