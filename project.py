inventory = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"Item '{name}' added successfully!")


def update_item():
    name = input("Enter item name to update: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            item["price"] = float(input("Enter new price: "))
            item["quantity"] = int(input("Enter new quantity: "))
            item["category"] = input("Enter new category: ")
            print(f"Item '{name}' updated successfully!")
            return

    print("Item not found.")


def remove_item():
    name = input("Enter item name to remove: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed successfully!")
            return

    print("Item not found.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return


    for item in inventory:
        print(
            f"Name: {item['name']}, "
            f"Price: ${item['price']:.2f}, "
            f"Quantity: {item['quantity']}, "
            f"Category: {item['category']}"
        )


def search_by_category():
    category = input("Enter category to search: ")
    found = False

    for item in inventory:
        if item["category"].lower() == category.lower():
            print(
                f"{item['name']} - ${item['price']:.2f} - "
                f"{item['quantity']} units"
            )
            found = True

    if not found:
        print("No items found in this category.")


def menu():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
