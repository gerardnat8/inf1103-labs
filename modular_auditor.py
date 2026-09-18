print("=============================")
print('Smart Inventory Auditor')
print("=============================")

total_inventories = 0

failed_entries = 0 

print("Smart Inventory Auditor Initialised")
print("Enter stock quantities to add. Type 'quit' to exit.\n")

while True:
    user_input = input("Enter stock quantity: ").strip()

    if user_input.lower() == "quit":
        print("Leaving system due to user command.\n")
        break

    if not user_input.isdigit():
            if user_input.startswith('-') and user_input[1:].isdigit():
                 print("Input Error: Negative numbers are not allowed.\n")
            else:
                 print(f"Input Error: {user_input} is not a valid integer.\n")
            failed_entries += 1
            continue 

    quantity = int(user_input)
    total_inventories += quantity
    print(f"Success: Added {quantity} to total inventory. Current total: {total_inventories}\n")

    if total_inventories > 500:
         print(f"\nTotal units {total_inventories} has exceeded the maximum of 500")
         print("Loop has terminated due to overstock. ")
         break 
    elif total_inventories == 500:
         print(f"\nTotal units {total_inventories} is at maximum capacity\n")
    else:
         pass
        

print("\n" + "="*38)
print("FINAL AUDIT METRICS REPORT")
print("="*38)
print(f"Total Units Processed: {total_inventories} units")
print(f"Number of Failed Entries: {failed_entries} entries")
print("="*38 + "\n")

    



            

