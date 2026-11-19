def atm_system():
    balance = 5000
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("\nEnter Your Choice: "))
        if choice == 1:
            print("\nAvailable Balance:", balance)
        elif choice == 2:
            deposit_amount = int(input("Enter Deposit Amount: "))
            if deposit_amount > 0:
                balance = balance + deposit_amount
                print("\nDeposit Successful!")
                print("Updated Balance:", balance)
            else:
                print("Invalid Deposit Amount!")
        elif choice == 3:
            withdraw_amount = int(input("Enter Withdraw Amount: "))
            if withdraw_amount <= 0:
                print("Invalid Withdraw Amount!")
            elif withdraw_amount <= balance:
                balance = balance - withdraw_amount
                print("\nWithdrawal Successful!")
                print("Updated Balance:", balance)
            else:
                print("\nInsufficient Balance!")
                print("Available Balance:", balance)
        elif choice == 4:
            print("\nThank You! Visit Again.")
            break
        else:
            print("\nInvalid Choice! Please Try Again.")
atm_system()