def display_menu(items):
    print("\nWelcome to the Vending Machine!")
    print("Here are the available items:")
    for code, (name, price, stock) in items.items():
        status = f"(${price:.2f}) - In Stock: {stock}" if stock > 0 else "(Out of Stock)"
        print(f"{code}: {name} {status}")


def check_availability(item_code, items):
    if item_code in items and items[item_code][2] > 0:  # Check stock
        return True
    return False


def process_payment(price):
    print(f"The item costs ${price:.2f}.")
    inserted_amount = 0.0
    while inserted_amount < price:
        try:
            amount = float(input(f"Insert money (${price - inserted_amount:.2f} remaining): "))
            if amount > 0:
                inserted_amount += amount
            else:
                print("Please insert a valid amount.")
        except ValueError:
            print("Invalid input. Please insert money in numerical format.")

    change = inserted_amount - price
    if change > 0:
        print(f"Returning change: ${change:.2f}")
    return True


def vending_machine():
    # Inventory: code -> (name, price, stock)
    items = {
        "A1": ("Chips", 1.50, 5),
        "B1": ("Soda", 2.00, 3),
        "C1": ("Candy", 1.00, 2),
        "D1": ("Water", 1.25, 0),  # Out of stock
    }

    while True:
        display_menu(items)
        item_code = input("\nEnter the code of the item you want to buy (or 'exit' to quit): ").upper()
        
        if item_code == "EXIT":
            print("Thank you for using the vending machine. Goodbye!")
            break

        if check_availability(item_code, items):
            item_name, item_price, item_stock = items[item_code]
            if process_payment(item_price):
                print(f"Dispensing {item_name}...")
                items[item_code] = (item_name, item_price, item_stock - 1)  # Adjust inventory
        else:
            print("Item is either out of stock or invalid. Please choose a different item.")

        another_item = input("\nWould you like to buy another item? (yes/no): ").lower()
        if another_item != "yes":
            print("Thank you for using the vending machine. Goodbye!")
            break


# Run the vending machine
vending_machine()