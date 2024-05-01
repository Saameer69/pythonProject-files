def display_lands(lands):
    print("Land Details:")
    for land in lands:
        print("Land ID: {}, City: {}, Direction: {}, Ana: {}, Price: Rs. {}, Availability: {}".format(land['land_id'], land['city'], land['direction'], land['ana'], land['price'], land['availability']))

def return_land(lands, land_id):
    for land in lands:
        if land['land_id'] == land_id:
            if land['availability'] == "Not Available":
                actual_months = int(input("Enter the actual number of months rented: "))
                if actual_months <= 0:
                    print("Invalid input. Please enter a valid number of months.")
                    return

                if actual_months > 0:
                    if actual_months > land['months_rented']:
                        extra_months = actual_months - land['months_rented']
                        fine = extra_months * 20000 
                        

                        print("You rented the land for {} months, exceeding the agreed-upon period. "
                              "Fine of Rs. {} will be applied.".format(actual_months, fine))
                    else:
                        print("Land {} has been returned.".format(land_id))

                    land['availability'] = "Available"
            else:
                print("Land {} is not currently rented.".format(land_id))
            break
    else:
        print("Land ID not found!")


def rent_land(lands, land_id):
    for land in lands:
        if land['land_id'] == land_id:
            if land['availability'] == "Available":

                # Prompt for customer details and rental period
                while True:
                    try:
                        customer_name = input("Enter customer name: ")
                        customer_number = input("Enter phone number: ")
                        ana = int(input("Enter the area (Ana) of the land: "))
                        months = int(input("Enter number of months to rent: "))
                        if ana > 0 and months > 0:
                            break
                        else:
                            print("Area and months should be greater than 0. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                # Update land availability and months rented
                land['availability'] = "Not Available"
                land['months_rented'] = months

                # Calculate total price
                total_price = land['price'] * ana * months

                # Generate invoice
                invoice = "==========================\n"
                invoice += "Invoice\n"
                invoice += "Customer Name: {}\n".format(customer_name)
                invoice += "Phone Number: {}\n".format(customer_number)
                invoice += "Land ID: {}\n".format(land_id)
                invoice += "City: {}\n".format(land['city'])
                invoice += "Direction: {}\n".format(land['direction'])
                invoice += "Land Area: {} Ana\n".format(ana)
                invoice += "Total Months: {}\n".format(months)
                invoice += "Total Price: Rs. {}\n".format(total_price)
                invoice += "==========================\n"

                # Save invoice to a text file
                file_name = "invoice_land_{}.txt".format(land_id)
                with open(file_name, 'w') as file:
                    file.write(invoice)
                print("Invoice has been generated and saved in {}".format(file_name))
            else:
                print("Land {} is already rented.".format(land_id))
            break
    else:
        print("Land ID not found!")


def main():
    lands = []

    try:
        with open("land_info.txt", "r") as file:
            for line in file:
                land_info = line.strip().split(',')
                if len(land_info) == 6:
                    try:
                        land_id = int(land_info[0])
                        ana = int(land_info[3])
                        price = int(land_info[4])
                    except ValueError:
                        print("Invalid data format in land_info.txt:", line)
                        continue

                    land = {
                        'land_id': land_id,
                        'city': land_info[1],
                        'direction': land_info[2],
                        'ana': ana,
                        'price': price,
                        'availability': land_info[5]
                    }
                    lands.append(land)
                else:
                    print("Invalid data format in land_info.txt:", line)

    except FileNotFoundError:
        print("Error: land_info.txt not found.")

    print("-" * 184)
    print("\t\t\t\t\t\t\t\t\t\t\tProperty Rental Nepal")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\tRamkot, Kathmandu | Phone no: 98526718912")
    print("\n")
    print("-" * 184)
    print("\t\t\t\t\t\t\t\t\t\tWelcome to the system. We hope you have a good experience.")
    print("-" * 184)

    while True:
        print("\n1. Show land details")
        print("2. Rent Land to customer")
        print("3. Return land from customer")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_lands(lands)

        elif choice == '2':
            display_lands(lands)
            land_id = int(input("Enter Land ID: "))

            rent_land(lands, land_id)

        elif choice == '3':
            land_id = int(input("Enter Land ID to return: "))
            return_land(lands, land_id)

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
