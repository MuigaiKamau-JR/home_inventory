import sqlite3
from datetime import datetime
from .models import Item

class Database:
    def __init__(self, db_file="inventory.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS items (
                     name TEXT,
                     purchase_date TEXT,
                     price REAL,
                     warranty_expiry_date TEXT,
                     quantity INTEGER
                     )''')
        self.conn.commit()

    def add_item(self, item: Item):
        c = self.conn.cursor()
        c.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?)", (item.name, item.purchase_date.strftime("%Y-%m-%d"), item.price, item.warranty_expiry_date.strftime("%Y-%m-%d"), item.quantity))
        self.conn.commit()

    def get_items(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM items")
        rows = c.fetchall()
        items = []
        for row in rows:
            name, purchase_date_str, price, warranty_expiry_date_str, quantity = row
            purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
            warranty_expiry_date = datetime.strptime(warranty_expiry_date_str, "%Y-%m-%d")
            item = Item(name, purchase_date, price, warranty_expiry_date, quantity)
            items.append(item)
        return items

    def search_item_by_name(self, name: str):
        c = self.conn.cursor()
        c.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + name + '%',))
        rows = c.fetchall()
        items = []
        for row in rows:
            name, purchase_date_str, price, warranty_expiry_date_str, quantity = row
            purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
            warranty_expiry_date = datetime.strptime(warranty_expiry_date_str, "%Y-%m-%d")
            item = Item(name, purchase_date, price, warranty_expiry_date, quantity)
            items.append(item)
        return items

    def remove_item_by_name(self, name: str):
        c = self.conn.cursor()
        c.execute("DELETE FROM items WHERE name=?", (name,))
        self.conn.commit()

    def update_item(self, name: str, new_price: float, new_quantity: int):
        c = self.conn.cursor()
        c.execute("UPDATE items SET price=?, quantity=? WHERE name=?", (new_price, new_quantity, name))
        self.conn.commit()
