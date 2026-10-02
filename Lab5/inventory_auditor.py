import json
import os

INVENTORY_FILE = "inventory.json"
 
 
def find_product(inventory, product_id):
    """Return the product dictionary with this ID, or None."""
    for product in inventory:
        if product["id"].upper() == product_id.upper():
            return product
    return None
            
def add_product(inventory, product_id, name, price, stock):
    """Add a new product. Returns True if added, False if the ID already exists."""
    if find_product(inventory, product_id):
        print(f"Error: Product ID {product_id} already exists.")
        return False

    inventory.append({
        "id": product_id.upper(),
        "name": name,
        "price": price,
        "stock": stock
    })
    print("Product added successfully!")
    return True

def print_product(product):
    print(f"ID: {product['id']} | Name: {product['name']} | "
          f"Price: ${product['price']:.2f} | Stock: {product['stock']}")


def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    if not inventory:
        print("No products in inventory.")
    for product in inventory:
        print_product(product)
    print("-" * 48)


def load_inventory():
    """Load products from inventory.json if it exists, otherwise start empty."""
    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return []

    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as f:
            inventory = json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Could not read the file. Starting with an empty inventory.")
        return []

    if not isinstance(inventory, list):
        print("File format not recognised. Starting with an empty inventory.")
        return []

    print("Inventory loaded successfully.")
    return inventory

inventory = load_inventory()
display_all(inventory)