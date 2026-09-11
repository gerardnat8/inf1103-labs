print("=============================")
print('Smart Inventory Auditor')
print("=============================")

total_inventories = 0

failed_inventories = 0 

print("Smart Inventory Auditor Initialised")
print("Enter stock quantities to add. Type 'quit' to exit.\n")

while True:
    user_input = input("Enter stock quantity: ").strip()

    if user_input.lower() == "quit":
        print("/nLeaving system due to user command.")
        break

    if not user_input.isdigit():
        if user_input.startswith('-') and user_input[1:].isdigit():

