# Item class definition
class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return (f"ID: {self.item_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Price: P{self.price:.2f}\n{'=' * 30}")

# CRUD Application
items = {}

def add_item():
    print("===== ADD ITEM =====")
    try:
        item_id = input("Enter Item ID: ").strip()
        if item_id in items:
            print("Error: ID already exists.")
            return

        name = input("Enter Item Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return

        description = input("Enter Item Description: ").strip()
        if not description:
            print("Error: Description cannot be empty.")
            return

        price = float(input("Enter Item Price: ").strip())
        if price < 0:
            print("Error: Price cannot be negative.")
            return

        items[item_id] = Item(item_id, name, description, price)
        print("\nItem added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid price.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_items():
    print("===== VIEW ALL ITEMS =====")
    if not items:
        print("\nNo items found.")
        return

    print("\n=== ITEM LIST ===")
    for item in items.values():
        print(item)

def update_item():
    print("===== UPDATE ITEM =====")
    item_id = input("Enter Item ID: ").strip()
    if item_id not in items:
        print("Error: Item not found.")
        return

    item = items[item_id]

    print("Keep blank to keep the existing value.")
    name = input(f"New Name [{item.name}]: ").strip() or item.name
    description = input(f"New Description [{item.description}]: ").strip() or item.description

    price_input = input(f"New Price [{item.price}]: ").strip()
    
    try:
        price = item.price if not price_input else float(price_input)
        if price < 0:
            print("Error: Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price input.")
        return

    # Update item details
    item.name = name
    item.description = description
    item.price = price

    print("\nItem updated successfully!")

def del_item():
    print("===== DELETE ITEM =====")
    item_id = input("Enter Item ID: ").strip()

    if item_id in items:
        del items[item_id]
        print("\nItem deleted successfully!")
    else:
        print("Error: Item not found.")

def main_menu():
    while True:
        print("=== ITEM MANAGEMENT MENU ===")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        print("============================")
        opt = int(input("Choose an option: "))

        if opt == 1:
            add_item()
        elif opt == 2:
            view_items()
        elif opt == 3:
            update_item()
        elif opt == 4:
            del_item()
        elif opt == 5:
            print("Exiting program....")
            break
        else:
            print("Invalid option. Please try again.")


# Run the application
if __name__ == "__main__":
    main_menu()
