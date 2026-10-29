import json
import os
 
from inventory import Inventory
from product import Product
 
INVENTORY_FILE = "inventory.json"
 
 

def load_inventory():
    """Read inventory.json and return an Inventory full of Product objects."""
    inventory = Inventory()
 
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return inventory
 
    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Could not read the file. Starting with an empty inventory.")
        return inventory
 
    if not isinstance(data, list):
        print("File format not recognised. Starting with an empty inventory.")
        return inventory
 
    skipped = 0
    for item in data:
        try:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
        except (KeyError, TypeError, ValueError):
            skipped += 1
            continue
        if not inventory.add_product(product):
            skipped += 1
 
    print("Inventory loaded successfully.")
    if skipped:
        print(f"Warning: {skipped} invalid or duplicate record(s) were skipped.")
    return inventory
 