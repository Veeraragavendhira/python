print("========== ONLINE SHOPPING SYSTEM ==========")

# 1. Customer Details

name = input("Enter Customer Name: ")
age = int(input("Enter Customer Age: "))
phone = input("Enter Phone Number: ")

if age < 18:
    print("Not Eligible to Purchase")

else:

    print("\nCustomer Details Verified Successfully!")

    # 2. Product Selection

    print("\n========== PRODUCT LIST ==========")
    print("1. Mobile       - Rs.15000")
    print("2. Laptop       - Rs.45000")
    print("3. Headphones   - Rs.2000")
    print("4. Smart Watch  - Rs.5000")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        product = "Mobile"
        price = 15000
        stock = 5

    elif choice == 2:
        product = "Laptop"
        price = 45000
        stock = 0

    elif choice == 3:
        product = "Headphones"
        price = 2000
        stock = 10

    elif choice == 4:
        product = "Smart Watch"
        price = 5000
        stock = 3

    else:
        product = ""
        price = 0
        stock = 0
        print("Invalid Product Selection")

    # 3. Stock Availability

    if product != "":

        print("\nSelected Product:", product)
        print("Product Price: Rs.", price)
        print("Available Stock:", stock)

        if stock == 0:
            print("Out of Stock")

        else:

            # 4. Quantity Selection

            quantity = int(input("\nEnter Quantity: "))

            if quantity <= 0:
                print("Invalid Quantity")

            elif quantity > stock:
                print("Insufficient Stock")

            else:

                # Calculate Product Total

                total = price * quantity

                # 5. Discount Calculation

                if total >= 50000:
                    discount = total * 20 / 100

                elif total >= 20000:
                    discount = total * 15 / 100

                elif total >= 10000:
                    discount = total * 10 / 100

                else:
                    discount = 0

                amount = total - discount

                # 6. Delivery Charges

                if amount >= 5000:
                    delivery = 0
                    print("\nFree Delivery!")

                else:
                    delivery = 100

                # 7. Payment Method

                print("\n========== PAYMENT METHOD ==========")
                print("1. UPI")
                print("2. Credit Card")
                print("3. Debit Card")
                print("4. Cash on Delivery")

                payment = int(input("\nSelect Payment Method: "))

                cod = 0
                payment_method = ""
                verified = False

                if payment == 1:
                    payment_method = "UPI"
                    pin = input("Enter UPI PIN: ")

                    if len(pin) == 4 and pin.isdigit():
                        verified = True

                elif payment == 2:
                    payment_method = "Credit Card"
                    pin = input("Enter Card PIN: ")

                    if len(pin) == 4 and pin.isdigit():
                        verified = True

                elif payment == 3:
                    payment_method = "Debit Card"
                    pin = input("Enter Card PIN: ")

                    if len(pin) == 4 and pin.isdigit():
                        verified = True

                elif payment == 4:
                    payment_method = "Cash on Delivery"
                    cod = 50
                    verified = True

                else:
                    print("Invalid Payment Method")

                # 8. Final Bill Generation

                if verified:

                    final_amount = amount + delivery + cod

                    print("\nPayment Verified Successfully!")

                    print("\n========== FINAL BILL ==========")
                    print("Customer Name    :", name)
                    print("Product Name     :", product)
                    print("Quantity         :", quantity)
                    print("Product Total    : Rs.", total)
                    print("Discount Amount  : Rs.", discount)
                    print("Delivery Charge  : Rs.", delivery)
                    print("COD Charge       : Rs.", cod)
                    print("Final Amount     : Rs.", final_amount)
                    print("Payment Method   :", payment_method)
                    print("Order Status     : ORDER PLACED SUCCESSFULLY")

                    print("\n ================================")
                    print("     THANK YOU FOR SHOPPING!")
                    print("================================")

                else:
                    print("\n Payment Failed!")
                    print("Order Status: PAYMENT FAILED")
