# Simple Inventory Store Manager - Menu Driven

inventory = [
    {
        "item_id": "I001",
        "item_name": "Apple",
        "stock_count": 50,
        "price": 10.5
    },
    {
        "item_id": "I002",
        "item_name": "Milk",
        "stock_count": 100,
        "price": 25.0
    },
    {
        "item_id": "I003",
        "item_name": "Rice",
        "stock_count": 25,
        "price": 40.0
    }
]

def add_item():
    item_id = input("Enter Item ID: ")
    item_name = input("Enter Item Name: ")
    stock_count = int(input("Enter Stock Count: "))
    price = float(input("Enter Price: "))
    item = {
        "item_id": item_id,
        "item_name": item_name,
        "stock_count": stock_count,
        "price": price
    }
    inventory.append(item)
    print("Item added successfully.\n")

def view_items():
    if not inventory:
        print("No items in inventory.\n")
        return
    print("List of Inventory Items:")
    for i, item in enumerate(inventory, 1):
        print(f"{i}. ID: {item['item_id']}, Name: {item['item_name']}, Stock: {item['stock_count']}, Price: {item['price']}")
    print()

def update_item():
    item_id = input("Enter the Item ID to update: ")
    for item in inventory:
        if item['item_id'] == item_id:
            print("Enter new details (leave blank to keep current value):")
            new_name = input(f"Current Item Name ({item['item_name']}): ")
            new_stock = input(f"Current Stock ({item['stock_count']}): ")
            new_price = input(f"Current Price ({item['price']}): ")
            if new_name:
                item['item_name'] = new_name
            if new_stock:
                item['stock_count'] = int(new_stock)
            if new_price:
                item['price'] = float(new_price)
            print("Item updated successfully.\n")
            return
    print("Item not found.\n")

def delete_item():
    item_id = input("Enter the Item ID to delete: ")
    for i, item in enumerate(inventory):
        if item['item_id'] == item_id:
            inventory.pop(i)
            print("Item deleted successfully.\n")
            return
    print("Item not found.\n")

def main_menu():
    while True:
        print("Inventory Store Manager")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
