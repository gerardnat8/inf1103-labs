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

def update_stock(inventory, product_id, new_stock):
    """Set the stock of an existing product. Returns True if updated."""
    product = find_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return False

    product["stock"] = new_stock
    print("Stock updated successfully!")
    return True


def search_product(inventory, product_id):
    """Return the matching product dictionary, or None if not found."""
    return find_product(inventory, product_id)

def save_inventory(inventory):
    """Write the whole inventory list to inventory.json."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

def read_float(prompt):
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
            if value < 0:
                print("Input Error: Value cannot be negative.")
                continue
            return value
        except ValueError:
            print(f"Input Error: {text} is not a valid number.")


def read_int(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            return int(text)
        if text.startswith("-") and text[1:].isdigit():
            print("Input Error: Negative numbers are not allowed.")
        else:
            print(f"Input Error: {text} is not a valid whole number.")


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input Error: This field cannot be empty.")


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            print("Add New Product")
            product_id = read_text("Product ID: ")
            name = read_text("Product Name: ")
            price = read_float("Price: ")
            stock = read_int("Stock Quantity: ")
            add_product(inventory, product_id, name, price, stock)

        elif choice == "3":
            print("Update Stock")
            product_id = read_text("Enter Product ID: ")
            product = find_product(inventory, product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found:")
                print(f"Name: {product['name']}")
                print(f"Current Stock: {product['stock']}")
                new_stock = read_int("New Stock Quantity: ")
                update_stock(inventory, product_id, new_stock)

        elif choice == "4":
            print("Search Product")
            product_id = read_text("Enter Product ID: ")
            product = search_product(inventory, product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                print("-" * 48)
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("-" * 48)

        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")

        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated")
            break

        else:
            print("Invalid option. Please choose 1 to 6.")


main()