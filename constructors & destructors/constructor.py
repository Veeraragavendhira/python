# class Demo:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
# d = Demo()
# del d

a = 10 #public
def deepak():
    # global a 
    a = 10
    print("a = ",a )
deepak()
a = 20
print("a = ",a)