Home Inventory System

The Home Inventory System is a command-line interface (CLI) application designed to manage items within a home for insurance claims. It allows users to add, list, search, update, and remove items from their inventory, keeping track of purchase dates, prices, warranty expiration dates, and quantities.

Features

Add Item: Add new items to the inventory with details such as name, purchase date, price, warranty expiration date, and quantity.
List Items: Display a list of all items currently in the inventory.
Search Items: Search for items by name.
Update Item: Update the price and quantity of an existing item.
Remove Item: Remove an item from the inventory.
Installation

To run the Home Inventory System, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your_username/home_inventory_system.git
cd home_inventory_system
Setup Virtual Environment:

bash
Copy code
python -m venv venv
Activate Virtual Environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Initialize Database:

bash
Copy code
python setup.py
This command initializes the SQLite database (inventory.db) with necessary tables.

Usage

Once the environment is set up, you can use the CLI commands to interact with the Home Inventory System:

Add Item:

bash
Copy code
python -m inventory.cli add_item
Follow the prompts to enter item details.

List Items:

bash
Copy code
python -m inventory.cli list_items
Display all items currently in the inventory.

Search Items:

bash
Copy code
python -m inventory.cli search_items
Search for items by name.

Update Item:

bash
Copy code
python -m inventory.cli update_item
Update the price and quantity of an existing item.

Remove Item:

bash
Copy code
python -m inventory.cli remove_item
Remove an item from the inventory.

Additional Notes

Ensure the virtual environment (venv) is activated before running any commands.
Modify inventory.db directly only if necessary; prefer using CLI commands for data manipulation.
For development and testing, consider adding unit tests to ensure the application functions correctly across different scenarios.
