from datetime import datetime

class Item:
    def __init__(self, name: str, purchase_date: datetime, price: float, warranty_expiry_date: datetime, quantity: int):
        self.name = name
        self.purchase_date = purchase_date
        self.price = price
        self.warranty_expiry_date = warranty_expiry_date
        self.quantity = quantity

class Room:
    def __init__(self, name: str):
        self.name = name








# from datetime import datetime
# from typing import List, Dict, Any

# class Item:
#     def __init__(self, name: str, value: float, acquisition_date: datetime):
#         self.name = name
#         self.value = value
#         self.acquisition_date = acquisition_date

# class Room:
#     def __init__(self, name: str):
#         self.name = name
#         self.items: List[Item] = []

#     def add_item(self, item: Item):
#         self.items.append(item)

#     def serialize(self) -> Dict[str, Any]:
#         return {
#             "name": self.name,
#             "items": [
#                 {"name": item.name, "value": item.value, "acquisition_date": item.acquisition_date}
#                 for item in self.items
#             ]
#         }
