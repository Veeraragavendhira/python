a=["Gopika","Kiruba","Mohana", "Deepa", "Hema", "Swetha"]
b=["g@1","k@1","m@1","d@1","h@1","s@1"]
c=[1000, 2000,6000, 5000, 3000, 5600]
un=input("Enter username: ")
if(un in a):
    pw=input("Enter password: ")
    if(pw in b) and ((un==a[0] and pw==b[0])or(un==a[1] and pw==b[1])or(un==a[2] and pw==b[2])or(un==a[3] and pw==b[3])or(un==a[4] and pw==b[4])or(un==a[5] and pw==b[5])):
        {
         print("""login successful
               select any one
               --------------
         * 1 - deposit  
         * 2 - withdraw
         * 3 - check balance
         * 4 - change pin""")
        }
        bank=[1,2,3,4]
        select=input("Enter your need: ")
        if(un==a[0] and pw==b[0]):
            bal=c[0]
        if(un==a[1] and pw==b[1]):
            bal=c[1]
        if(un==a[2] and pw==b[2]):
            bal=c[2]
        if(un==a[3] and pw==b[3]):
            bal=c[3]
        if(un==a[4] and pw==b[4]):
            bal=c[4]
        if(un==a[5] and pw==b[5]):
            bal=c[5]

        if(select == bank[0]):
            amount=int(input("Enter amount: "))
            depbal=amount+bal 
            {
               print("available balance: ",depbal)  
            }
        if(select == bank[1]): 
            amount=int(input("Enter amount: "))  
            if(amount<500):      
                withbal=bal-amount
                {
                    print("available balance: ",withbal)
                }
            
            else:{
                    print("amount not available")
                }
        if(select == bank[2]):{          
                print("available balance: ",bal)
            }               
        if(select == bank[3]):
            old=(input("Enter old PIN: "))
            if(old==pw):
                new=(input("Enter new PIN: "))
                if(new not in b):
                    {
                        print("PIN changed successfully")
                    }
                else:{
                        print("""create strong PIN
                              INVALID PIN""")
                    }
            else:{
                    print("wrong PIN")
                }
    else:{
         print("wrong password")
        }
else:{
     print("wrong username")
    }





# ATM Program

# 
# print("Insufficient Balance")balance = 20000
# pin = "2029"

# userpin = input("Enter ATM PIN: ")

# if userpin == pin:
#     print("Login Successful")
#     print("1. Balance Check")
#     print("2. Withdraw")
#     print("3. Deposit")
#     print("4. Change PIN")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Your Balance is:", balance)

#     elif choice == 2:
#         withdraw = int(input("Enter Withdraw Amount: "))
#         if withdraw <= balance:
#             balance = balance - withdraw
#             print("Please collect your cash")
#             print("Remaining Balance:", balance)
#         else:

#     elif choice == 3:
#         deposit = int(input("Enter Deposit Amount: "))
#         balance = balance + deposit
#         print("Amount Deposited Successfully")
#         print("Total Balance:", balance)

#     elif choice == 4:
#         newpin = input("Enter New PIN: ")
#         pin = newpin
#         print("PIN Changed Successfully")

#     else:
#         print("Invalid Choice")
# else:
#     print("Wrong PIN")