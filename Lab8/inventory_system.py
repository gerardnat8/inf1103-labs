import json
import os

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct

INVENTORY_FILE = "inventory.json"


def product_to_dict(product):
    """Turn one product into a dictionary, including its type identifier."""
    common = {
        "id": product.get_product_id(),
        "name": product.get_name(),
        "price": product.get_price(),
        "stock": product.get_stock(),
    }
    if isinstance(product, PhysicalProduct):
        return {"type": "physical", **common, "weight": product.get_weight()}
    if isinstance(product, DigitalProduct):
        return {"type": "digital", **common, "download_size": product.get_download_size()}
    raise ValueError("Unknown product type.")


def dict_to_product(item):
    """Use the type identifier to build the right kind of product."""
    kind = item["type"]
    if kind == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"],
                               item["stock"], item["weight"])
    if kind == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"],
                              item["stock"], item["download_size"])
    raise ValueError(f"Unknown product type: {kind}")


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
            product = dict_to_product(item)
        except (KeyError, TypeError, ValueError):
            skipped += 1
            continue
        if not inventory.add_product(product):
            skipped += 1

    print("Inventory loaded successfully.")
    if skipped:
        print(f"Warning: {skipped} invalid or duplicate record(s) were skipped.")
    return inventory


def save_inventory(inventory):
    """Turn every Product into a dictionary and write the list to inventory.json."""
    data = [product_to_dict(product) for product in inventory.get_all_products()]
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


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


def read_product_type():
    """Ask the user for a product type. Returns 'physical' or 'digital'."""
    while True:
        text = input("Product Type (1 = Physical, 2 = Digital): ").strip()
        if text == "1":
            return "physical"
        if text == "2":
            return "digital"
        print("Input Error: Please enter 1 or 2.")


def ask_for_product():
    """Ask the user for the details of a new product and return the Product object."""
    product_type = read_product_type()
    product_id = read_text("Product ID: ")
    name = read_text("Product Name: ")
    price = read_float("Price: ")
    stock = read_int("Stock Quantity: ")
    if product_type == "physical":
        weight = read_float("Weight (kg): ")
        return PhysicalProduct(product_id, name, price, stock, weight)
    download_size = read_float("Download Size (MB): ")
    return DigitalProduct(product_id, name, price, stock, download_size)


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
            inventory.display_all()

        elif choice == "2":
            print("Add New Product")
            product = ask_for_product()
            if inventory.add_product(product):
                print("Product added successfully!")
            else:
                print(f"Error: Product ID {product.get_product_id()} already exists.")

        elif choice == "3":
            print("Update Stock")
            product_id = read_text("Enter Product ID: ")
            product = inventory.find_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found:")
                print(f"Name: {product.get_name()}")
                print(f"Current Stock: {product.get_stock()}")
                new_stock = read_int("New Stock Quantity: ")
                if product.update_stock(new_stock):
                    print("Stock updated successfully!")
                else:
                    print("Input Error: Stock was not updated.")

        elif choice == "4":
            print("Search Product")
            product_id = read_text("Enter Product ID: ")
            product = inventory.find_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                print("Product Found")
                product.display_details()

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


if __name__ == "__main__":
    main()