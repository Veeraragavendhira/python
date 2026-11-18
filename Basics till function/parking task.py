vehicle_numbers = []
customer_names = []
vehicle_types = []
parking_hours = []
parking_amounts = []

total_slots = 10
available_slots = 10
total_revenue = 0

while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Available Slots")
    print("4. Search Vehicle")
    print("5. Exit Application")

    choice = int(input("Enter your choice: "))

    # VEHICLE ENTRY
    if choice == 1:

        if available_slots == 0:
            print("Parking Full!")
            continue

        name = input("Enter Customer Name: ")
        number = input("Enter Vehicle Number: ")
        
        if number in vehicle_numbers:
            print("Vehicle Already Parked!")
            continue

        print("\n1. Bike")
        print("2. Car")
        print("3. Van")

        v_choice = int(input("Select Vehicle Type: "))

        if v_choice == 1:
            v_type = "Bike"
        elif v_choice == 2:
            v_type = "Car"
        elif v_choice == 3:
            v_type = "Van"
        else:
            print("Invalid Vehicle Type!")
            continue

        vehicle_numbers.append(number)
        customer_names.append(name)
        vehicle_types.append(v_type)
        parking_hours.append(0)
        parking_amounts.append(0)

        available_slots -= 1

        print("\nVehicle Parked Successfully!")
        print("Vehicle Number:", number)
        print("Vehicle Type:", v_type)
        print("Available Slots:", available_slots)

    # VEHICLE EXIT
    elif choice == 2:

        number = input("Enter Vehicle Number: ")

        if number not in vehicle_numbers:
            print("Vehicle Not Found!")
            continue

        index = vehicle_numbers.index(number)

        hours = int(input("Enter Parking Hours: "))

        if hours <= 0:
            print("Invalid Parking Hours!")
            continue

        if vehicle_types[index] == "Bike":
            rate = 20
        elif vehicle_types[index] == "Car":
            rate = 50
        else:
            rate = 80

        amount = hours * rate

        if hours > 10:
            discount = amount * 20 / 100
        elif hours > 5:
            discount = amount * 10 / 100
        else:
            discount = 0

        final_amount = amount - discount

        parking_hours[index] = hours
        parking_amounts[index] = final_amount

        print("\n===== PARKING BILL =====")
        print("Customer Name:", customer_names[index])
        print("Vehicle Number:", number)
        print("Vehicle Type:", vehicle_types[index])
        print("Parking Hours:", hours)
        print("Base Amount: Rs.", amount)
        print("Discount: Rs.", discount)
        print("Final Amount: Rs.", final_amount)

        total_revenue += final_amount

        # Remove exited vehicle
        vehicle_numbers.pop(index)
        customer_names.pop(index)
        vehicle_types.pop(index)
        parking_hours.pop(index)
        parking_amounts.pop(index)

        available_slots += 1

        print("\nVehicle Exited Successfully!")

    # AVAILABLE SLOTS
    elif choice == 3:

        print("\nTotal Slots:", total_slots)
        print("Available Slots:", available_slots)
        print("Occupied Slots:", total_slots - available_slots)

        if available_slots == 0:
            print("Parking Full!")
        else:
            print("Parking Available!")

    # SEARCH VEHICLE
    elif choice == 4:

        number = input("Enter Vehicle Number: ")

        if number in vehicle_numbers:

            index = vehicle_numbers.index(number)

            print("\nVehicle Found!")
            print("Customer:", customer_names[index])
            print("Vehicle:", vehicle_numbers[index])
            print("Type:", vehicle_types[index])

        else:
            print("Vehicle Not Found!")

    # EXIT APPLICATION
    elif choice == 5:

        print("\n===== PARKING SUMMARY =====")
        print("Total Vehicles Currently Parked:", len(vehicle_numbers))
        print("Available Slots:", available_slots)
        print("Total Revenue: Rs.", total_revenue)

        print("\nThank You! Visit Again.")
        break

    else:
        print("Invalid Choice! Try Again.")
        continue