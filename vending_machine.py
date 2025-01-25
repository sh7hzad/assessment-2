# Simple Vending Machine Code

def display_menu():
    print("\nWelcome to the Vending Machine!")
    print("Please select a category:")
    print("1. Snacks")
    print("2. Drinks")
    print("3. Sweets")
    print("4. Exit")


def display_items(category, items):
    print(f"\n{category} Menu:")
    for code, (name, price) in items.items():
        print(f"{code}: {name} - ${price:.2f}")


def vending_machine():
  
    snacks = {
        "S1": ("Chips", 1.50),
        "S2": ("Cookies", 2.00),
        "S3": ("Nuts", 1.75),
    }

    drinks = {
        "D1": ("Water", 1.00),
        "D2": ("Soda", 1.50),
        "D3": ("Juice", 2.00),
    }

    sweets = {
        "SW1": ("Chocolate", 1.25),
        "SW2": ("Candy", 0.75),
        "SW3": ("Gum", 0.50),
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_items("Snacks", snacks)
            code = input("Enter the code of the item you want to buy: ").upper()
            if code in snacks:
                print(f"You selected {snacks[code][0]}. Please pay ${snacks[code][1]:.2f}.")
            else:
                print("Invalid code. Please try again.")

        elif choice == "2":
            display_items("Drinks", drinks)
            code = input("Enter the code of the item you want to buy: ").upper()
            if code in drinks:
                print(f"You selected {drinks[code][0]}. Please pay ${drinks[code][1]:.2f}.")
            else:
                print("Invalid code. Please try again.")

        elif choice == "3":
            display_items("Sweets", sweets)
            code = input("Enter the code of the item you want to buy: ").upper()
            if code in sweets:
                print(f"You selected {sweets[code][0]}. Please pay ${sweets[code][1]:.2f}.")
            else:
                print("Invalid code. Please try again.")

        elif choice == "4":
            print("Thank you for using the vending machine. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


vending_machine()
