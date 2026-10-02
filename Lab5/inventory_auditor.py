print("=============================")
print('Persistent Smart Inventory Auditor')
print("=============================")

import json
import os

INVENTORY_FILE = "data/inventory.json"
 
 
def load_inventory():
    total = 0
    history = []

    try:
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)

        total = int(data["total"])
        history = [int(x) for x in data["history"]]

        print("\nCurrent Inventory:")
        print(f"Running Total: {total}\n")
        if history:
            print("Past Transactions:")
            for i, amount in enumerate(history, start=1):
                print(f"{i}. {amount}")
        print()

    except FileNotFoundError:
        print("No previous inventory file found. Starting fresh.\n")
        total = 0
        history = []

    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Inventory file could not be read. Starting fresh.\n")
        total = 0
        history = []

    return total, history
 
def save_inventory(total, history):
    """Write the final total and transaction history list to INVENTORY_FILE as JSON."""
    folder = os.path.dirname(INVENTORY_FILE)
    if folder:
        os.makedirs(folder, exist_ok=True)

    data = {"total": total, "history": history}

    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nInventory successfully saved to {INVENTORY_FILE}")


def get_valid_input():
    user_input = input("Enter stock quantity: ").strip()
 
    if user_input.lower() == "quit":
        return "quit"
    if not user_input.isdigit():
        if user_input.startswith('-') and user_input[1:].isdigit():
            print("Input Error: Negative numbers are not allowed.\n")
        else:
            print(f"Input Error: {user_input} is not a valid integer.\n")
        return None
 
    return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("\n" + "=" * 38)
    print("FINAL AUDIT METRICS REPORT")
    print("=" * 38)
    print(f"Total Units Processed: {total_units} units")
    print(f"Number of Failed Entries: {failed_attempts} entries")
    print("=" * 38 + "\n")

def main():
    total_inventories, transaction_history = load_inventory()
    total_tax = 0
    failed_entries = 0
    deliveries_processed = 0
 
    print("Smart Inventory Auditor Initialised")
    print("Enter stock quantities to add. Type 'quit' to exit.\n")
 
    while True:
        result = get_valid_input()
 
        if result == "quit":
            print("Leaving system due to user command.\n")
            break
 
        if result is None:
            failed_entries += 1
            continue
 
        quantity = result
        total_inventories = process_delivery(total_inventories, quantity)
        transaction_history.append(quantity)
        tax = calculate_tax(quantity)
        total_tax += tax
        deliveries_processed += 1
 
        print(f"Success: Added {quantity} to total inventory. "
              f"Tax for this delivery: {tax:.2f}. "
              f"Current total: {total_inventories}\n")
 
        if total_inventories > 500:
            print(f"\nTotal units {total_inventories} has exceeded the maximum of 500")
            print("Loop has terminated due to overstock. ")
            break
        elif total_inventories == 500:
            print(f"\nTotal units {total_inventories} is at maximum capacity\n")
 
    save_inventory(total_inventories, transaction_history) 
    generate_report(total_inventories, failed_entries)
    print(f"Deliveries Processed: {deliveries_processed}")
    print(f"Total Tax Collected: {total_tax:.2f}\n")

main()
            

