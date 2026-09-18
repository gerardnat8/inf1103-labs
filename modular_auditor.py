print("=============================")
print('New Smart Inventory Auditor')
print("=============================")

    
def get_valid_input():
    # Prompt once. Return an int, the string 'quit', or None if invalid.
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
    # Add the new delivery to the running total and return the new total.
    return current_total + new_value

def calculate_tax(amount):
    # return 10% tax on a delivery amount 
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    # Print the final summary.
    print("\n" + "=" * 38)
    print("FINAL AUDIT METRICS REPORT")
    print("=" * 38)
    print(f"Total Units Processed: {total_units} units")
    print(f"Number of Failed Entries: {failed_attempts} entries")
    print("=" * 38 + "\n")



            

