import sys
from getpass import getpass  # Import getpass for secure password input
from datetime import datetime
from .models import Item
from .orm import Database

db = Database()

def add_item_interactive():
    print("Adding a new item:")
    name = input("Enter item name: ")
    purchase_date_str = input("Enter purchase date (YYYY-MM-DD): ")
    price = float(input("Enter price: "))
    warranty_expiry_date_str = input("Enter warranty expiry date (YYYY-MM-DD): ")
    quantity = int(input("Enter quantity: "))

    try:
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        warranty_expiry_date = datetime.strptime(warranty_expiry_date_str, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return
    
    item = Item(name, purchase_date, price, warranty_expiry_date, quantity)
    db.add_item(item)
    print(f"Item '{name}' added successfully!")

def list_items():
    items = db.get_items()
    if not items:
        print("No items found.")
    else:
        for item in items:
            print(f"Item: {item.name}, Quantity: {item.quantity}, Purchase Date: {item.purchase_date.strftime('%Y-%m-%d')}, Warranty Expiry Date: {item.warranty_expiry_date.strftime('%Y-%m-%d')}, Price: {item.price}")

def search_items():
    search_term = input("Enter item name to search: ")
    items = db.search_item_by_name(search_term)
    if not items:
        print(f"No items found with name '{search_term}'.")
    else:
        print(f"Items found matching '{search_term}':")
        for item in items:
            print(f"Item: {item.name}, Quantity: {item.quantity}, Purchase Date: {item.purchase_date.strftime('%Y-%m-%d')}, Warranty Expiry Date: {item.warranty_expiry_date.strftime('%Y-%m-%d')}, Price: {item.price}")

def remove_item():
    name = input("Enter item name to remove: ")
    db.remove_item_by_name(name)
    print(f"Item '{name}' removed successfully!")

def update_item():
    name = input("Enter item name to update: ")
    new_price = float(input("Enter new price: "))
    new_quantity = int(input("Enter new quantity: "))

    db.update_item(name, new_price, new_quantity)
    print(f"Item '{name}' updated successfully!")

def authenticate_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Implement your authentication logic here
    # Example: Validate username and password against a stored record or database

    if username == "admin" and password == "password":
        print("Authentication successful!")
    else:
        print("Authentication failed. Please try again.")

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else None
    
    if command == "add_item":
        add_item_interactive()
    elif command == "list_items":
        list_items()
    elif command == "search_items":
        search_items()
    elif command == "remove_item":
        remove_item()
    elif command == "update_item":
        update_item()
    elif command == "authenticate":
        authenticate_user()
    else:
        print("Invalid command. Use 'add_item', 'list_items', 'search_items', 'remove_item', 'update_item', or 'authenticate'.")






# import sys
# from datetime import datetime
# from .models import Item
# from .orm import Database

# db = Database()

# def add_item_interactive():
#     print("Adding a new item:")
#     name = input("Enter item name: ")
#     purchase_date_str = input("Enter purchase date (YYYY-MM-DD): ")
#     price = float(input("Enter price: "))
#     warranty_expiry_date_str = input("Enter warranty expiry date (YYYY-MM-DD): ")
#     quantity = int(input("Enter quantity: "))

#     try:
#         purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
#         warranty_expiry_date = datetime.strptime(warranty_expiry_date_str, "%Y-%m-%d")
#     except ValueError:
#         print("Error: Invalid date format. Please use YYYY-MM-DD.")
#         return
    
#     item = Item(name, purchase_date, price, warranty_expiry_date, quantity)
#     db.add_item(item)
#     print(f"Item '{name}' added successfully!")

# def list_items():
#     items = db.get_items()
#     if not items:
#         print("No items found.")
#     else:
#         for item in items:
#             print(f"Item: {item.name}, Quantity: {item.quantity}, Purchase Date: {item.purchase_date.strftime('%Y-%m-%d')}, Warranty Expiry Date: {item.warranty_expiry_date.strftime('%Y-%m-%d')}, Price: {item.price}")

# def search_items():
#     search_term = input("Enter item name to search: ")
#     items = db.search_item_by_name(search_term)
#     if not items:
#         print(f"No items found with name '{search_term}'.")
#     else:
#         print(f"Items found matching '{search_term}':")
#         for item in items:
#             print(f"Item: {item.name}, Quantity: {item.quantity}, Purchase Date: {item.purchase_date.strftime('%Y-%m-%d')}, Warranty Expiry Date: {item.warranty_expiry_date.strftime('%Y-%m-%d')}, Price: {item.price}")

# def remove_item():
#     name = input("Enter item name to remove: ")
#     db.remove_item_by_name(name)
#     print(f"Item '{name}' removed successfully!")

# def update_item():
#     name = input("Enter item name to update: ")
#     new_price = float(input("Enter new price: "))
#     new_quantity = int(input("Enter new quantity: "))

#     db.update_item(name, new_price, new_quantity)
#     print(f"Item '{name}' updated successfully!")

# if __name__ == "__main__":
#     command = sys.argv[1] if len(sys.argv) > 1 else None
    
#     if command == "add_item":
#         add_item_interactive()
#     elif command == "list_items":
#         list_items()
#     elif command == "search_items":
#         search_items()
#     elif command == "remove_item":
#         remove_item()
#     elif command == "update_item":
#         update_item()
#     else:
#         print("Invalid command. Use 'add_item', 'list_items', 'search_items', 'remove_item', or 'update_item'.")



# #  Add an item interactively
# python -m inventory.cli add_item

# # List all items
# python -m inventory.cli list_items

# # Search items by name
# python -m inventory.cli search_items

# # Remove an item
# python -m inventory.cli remove_item

# Update an item
# python -m inventory.cli update_item



# cd /Users/tkmuigai/Development/code/home_inventory_system

# source venv/bin/activate
